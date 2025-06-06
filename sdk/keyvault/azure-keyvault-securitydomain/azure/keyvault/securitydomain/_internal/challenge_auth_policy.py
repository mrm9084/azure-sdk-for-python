# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Policy implementing Key Vault's challenge authentication protocol.

Normally the protocol is only used for the client's first service request, upon which:
1. The challenge authentication policy sends a copy of the request, without authorization or content.
2. Key Vault responds 401 with a header (the 'challenge') detailing how the client should authenticate such a request.
3. The policy authenticates according to the challenge and sends the original request with authorization.

The policy caches the challenge and thus knows how to authenticate future requests. However, authentication
requirements can change. For example, a vault may move to a new tenant. In such a case the policy will attempt the
protocol again.
"""

from copy import deepcopy
import time
from typing import Any, cast, Optional, Union
from urllib.parse import urlparse

from azure.core.credentials import (
    AccessToken,
    AccessTokenInfo,
    TokenCredential,
    TokenProvider,
    TokenRequestOptions,
    SupportsTokenInfo,
)
from azure.core.exceptions import ServiceRequestError
from azure.core.pipeline import PipelineRequest, PipelineResponse
from azure.core.pipeline.policies import BearerTokenCredentialPolicy
from azure.core.rest import HttpRequest, HttpResponse

from .http_challenge import HttpChallenge
from . import http_challenge_cache as ChallengeCache


def _enforce_tls(request: PipelineRequest) -> None:
    if not request.http_request.url.lower().startswith("https"):
        raise ServiceRequestError(
            "Bearer token authentication is not permitted for non-TLS protected (non-https) URLs."
        )


def _has_claims(challenge: str) -> bool:
    """Check if a challenge header contains claims.

    :param challenge: The challenge header to check.
    :type challenge: str

    :returns: True if the challenge contains claims; False otherwise.
    :rtype: bool
    """
    # Split the challenge into its scheme and parameters, then check if any parameter contains claims
    split_challenge = challenge.strip().split(" ", 1)
    return any("claims=" in item for item in split_challenge[1].split(","))


def _update_challenge(request: PipelineRequest, challenger: PipelineResponse) -> HttpChallenge:
    """Parse challenge from a challenge response, cache it, and return it.

    :param request: The pipeline request that prompted the challenge response.
    :type request: ~azure.core.pipeline.PipelineRequest
    :param challenger: The pipeline response containing the authentication challenge.
    :type challenger: ~azure.core.pipeline.PipelineResponse

    :returns: An HttpChallenge object representing the authentication challenge.
    :rtype: HttpChallenge
    """

    challenge = HttpChallenge(
        request.http_request.url,
        challenger.http_response.headers.get("WWW-Authenticate"),
        response_headers=challenger.http_response.headers,
    )
    ChallengeCache.set_challenge_for_url(request.http_request.url, challenge)
    return challenge


class ChallengeAuthPolicy(BearerTokenCredentialPolicy):
    """Policy for handling HTTP authentication challenges.

    :param credential: An object which can provide an access token for the vault, such as a credential from
        :mod:`azure.identity`
    :type credential: ~azure.core.credentials.TokenProvider
    :param str scopes: Lets you specify the type of access needed.
    """

    def __init__(self, credential: TokenProvider, *scopes: str, **kwargs: Any) -> None:
        # Pass `enable_cae` so `enable_cae=True` is always passed through self.authorize_request
        super(ChallengeAuthPolicy, self).__init__(credential, *scopes, enable_cae=True, **kwargs)
        self._credential: TokenProvider = credential
        self._token: Optional[Union["AccessToken", "AccessTokenInfo"]] = None
        self._verify_challenge_resource = kwargs.pop("verify_challenge_resource", True)
        self._request_copy: Optional[HttpRequest] = None

    def send(self, request: PipelineRequest[HttpRequest]) -> PipelineResponse[HttpRequest, HttpResponse]:
        """Authorize request with a bearer token and send it to the next policy.

        We implement this method to account for the valid scenario where a Key Vault authentication challenge is
        immediately followed by a CAE claims challenge. The base class's implementation would return the second 401 to
        the caller, but we should handle that second challenge as well (and only return any third 401 response).

        :param request: The pipeline request object
        :type request: ~azure.core.pipeline.PipelineRequest

        :return: The pipeline response object
        :rtype: ~azure.core.pipeline.PipelineResponse
        """
        self.on_request(request)
        try:
            response = self.next.send(request)
        except Exception:  # pylint:disable=broad-except
            self.on_exception(request)
            raise

        self.on_response(request, response)
        if response.http_response.status_code == 401:
            return self.handle_challenge_flow(request, response)
        return response

    def handle_challenge_flow(
        self,
        request: PipelineRequest[HttpRequest],
        response: PipelineResponse[HttpRequest, HttpResponse],
        consecutive_challenge: bool = False,
    ) -> PipelineResponse[HttpRequest, HttpResponse]:
        """Handle the challenge flow of Key Vault and CAE authentication.

        :param request: The pipeline request object
        :type request: ~azure.core.pipeline.PipelineRequest
        :param response: The pipeline response object
        :type response: ~azure.core.pipeline.PipelineResponse
        :param bool consecutive_challenge: Whether the challenge is arriving immediately after another challenge.
            Consecutive challenges can only be valid if a Key Vault challenge is followed by a CAE claims challenge.
            True if the preceding challenge was a Key Vault challenge; False otherwise.

        :return: The pipeline response object
        :rtype: ~azure.core.pipeline.PipelineResponse
        """
        self._token = None  # any cached token is invalid
        if "WWW-Authenticate" in response.http_response.headers:
            # If the previous challenge was a KV challenge and this one is too, return the 401
            claims_challenge = _has_claims(response.http_response.headers["WWW-Authenticate"])
            if consecutive_challenge and not claims_challenge:
                return response

            request_authorized = self.on_challenge(request, response)
            if request_authorized:
                # if we receive a challenge response, we retrieve a new token
                # which matches the new target. In this case, we don't want to remove
                # token from the request so clear the 'insecure_domain_change' tag
                request.context.options.pop("insecure_domain_change", False)
                try:
                    response = self.next.send(request)
                except Exception:  # pylint:disable=broad-except
                    self.on_exception(request)
                    raise

                # If consecutive_challenge == True, this could be a third consecutive 401
                if response.http_response.status_code == 401 and not consecutive_challenge:
                    # If the previous challenge wasn't from CAE, we can try this function one more time
                    if not claims_challenge:
                        return self.handle_challenge_flow(request, response, consecutive_challenge=True)
                self.on_response(request, response)
        return response

    def on_request(self, request: PipelineRequest) -> None:
        _enforce_tls(request)
        challenge = ChallengeCache.get_challenge_for_url(request.http_request.url)
        if challenge:
            # Note that if the vault has moved to a new tenant since our last request for it, this request will fail.
            if self._need_new_token:
                # azure-identity credentials require an AADv2 scope but the challenge may specify an AADv1 resource
                scope = challenge.get_scope() or challenge.get_resource() + "/.default"
                self._request_kv_token(scope, challenge)

            bearer_token = cast(Union["AccessToken", "AccessTokenInfo"], self._token).token
            request.http_request.headers["Authorization"] = f"Bearer {bearer_token}"
            return

        # else: discover authentication information by eliciting a challenge from Key Vault. Remove any request data,
        # saving it for later. Key Vault will reject the request as unauthorized and respond with a challenge.
        # on_challenge will parse that challenge, use the original request including the body, authorize the
        # request, and tell super to send it again.
        if request.http_request.content:
            self._request_copy = request.http_request
            bodiless_request = HttpRequest(
                method=request.http_request.method,
                url=request.http_request.url,
                headers=deepcopy(request.http_request.headers),
            )
            bodiless_request.headers["Content-Length"] = "0"
            request.http_request = bodiless_request

    def on_challenge(self, request: PipelineRequest, response: PipelineResponse) -> bool:
        try:
            # CAE challenges may not include a scope or tenant; cache from the previous challenge to use if necessary
            old_scope: Optional[str] = None
            old_tenant: Optional[str] = None
            cached_challenge = ChallengeCache.get_challenge_for_url(request.http_request.url)
            if cached_challenge:
                old_scope = cached_challenge.get_scope() or cached_challenge.get_resource() + "/.default"
                old_tenant = cached_challenge.tenant_id

            challenge = _update_challenge(request, response)
            # CAE challenges may not include a scope or tenant; use the previous challenge's values if necessary
            if challenge.claims and old_scope:
                challenge._parameters["scope"] = old_scope  # pylint:disable=protected-access
                challenge.tenant_id = old_tenant
            # azure-identity credentials require an AADv2 scope but the challenge may specify an AADv1 resource
            scope = challenge.get_scope() or challenge.get_resource() + "/.default"
        except ValueError:
            return False

        if self._verify_challenge_resource:
            resource_domain = urlparse(scope).netloc
            if not resource_domain:
                raise ValueError(f"The challenge contains invalid scope '{scope}'.")

            request_domain = urlparse(request.http_request.url).netloc
            if not request_domain.lower().endswith(f".{resource_domain.lower()}"):
                raise ValueError(
                    f"The challenge resource '{resource_domain}' does not match the requested domain. Pass "
                    "`verify_challenge_resource=False` to your client's constructor to disable this verification. "
                    "See https://aka.ms/azsdk/blog/vault-uri for more information."
                )

        # If we had created a request copy in on_request, use it now to send along the original body content
        if self._request_copy:
            request.http_request = self._request_copy

        # The tenant parsed from AD FS challenges is "adfs"; we don't actually need a tenant for AD FS authentication
        # For AD FS we skip cross-tenant authentication per https://github.com/Azure/azure-sdk-for-python/issues/28648
        if challenge.tenant_id and challenge.tenant_id.lower().endswith("adfs"):
            self.authorize_request(request, scope, claims=challenge.claims)
        else:
            self.authorize_request(request, scope, claims=challenge.claims, tenant_id=challenge.tenant_id)

        return True

    @property
    def _need_new_token(self) -> bool:
        now = time.time()
        refresh_on = getattr(self._token, "refresh_on", None)
        return not self._token or (refresh_on and refresh_on <= now) or self._token.expires_on - now < 300

    def _request_kv_token(self, scope: str, challenge: HttpChallenge) -> None:
        """Implementation of BearerTokenCredentialPolicy's _request_token method, but specific to Key Vault.

        :param str scope: The scope for which to request a token.
        :param challenge: The challenge for the request being made.
        :type challenge: HttpChallenge
        """
        # Exclude tenant for AD FS authentication
        exclude_tenant = challenge.tenant_id and challenge.tenant_id.lower().endswith("adfs")
        # The SupportsTokenInfo protocol needs TokenRequestOptions for token requests instead of kwargs
        if hasattr(self._credential, "get_token_info"):
            options: TokenRequestOptions = {"enable_cae": True}
            if challenge.tenant_id and not exclude_tenant:
                options["tenant_id"] = challenge.tenant_id
            self._token = cast(SupportsTokenInfo, self._credential).get_token_info(scope, options=options)
        else:
            if exclude_tenant:
                self._token = self._credential.get_token(scope, enable_cae=True)
            else:
                self._token = cast(TokenCredential, self._credential).get_token(
                    scope, tenant_id=challenge.tenant_id, enable_cae=True
                )
