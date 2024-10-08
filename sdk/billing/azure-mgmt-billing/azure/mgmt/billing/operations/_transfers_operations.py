# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Iterable, Optional, Type, TypeVar, Union, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_request(
    billing_account_name: str, billing_profile_name: str, invoice_section_name: str, transfer_name: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-04-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/transfers/{transferName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "billingAccountName": _SERIALIZER.url(
            "billing_account_name",
            billing_account_name,
            "str",
            pattern=r"^([0-9]+|([Pp][Cc][Nn]\.[A-Za-z0-9]+)|[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}(:[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}_[0-9]{4}(-[0-9]{2}){2})?)$",
        ),
        "billingProfileName": _SERIALIZER.url(
            "billing_profile_name", billing_profile_name, "str", pattern=r"^[a-zA-Z\d-_]{1,128}$"
        ),
        "invoiceSectionName": _SERIALIZER.url(
            "invoice_section_name", invoice_section_name, "str", pattern=r"^[a-zA-Z\d-_]{1,128}$"
        ),
        "transferName": _SERIALIZER.url("transfer_name", transfer_name, "str", pattern=r"^[a-z0-9]*$"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_initiate_request(
    billing_account_name: str, billing_profile_name: str, invoice_section_name: str, transfer_name: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-04-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/transfers/{transferName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "billingAccountName": _SERIALIZER.url(
            "billing_account_name",
            billing_account_name,
            "str",
            pattern=r"^([0-9]+|([Pp][Cc][Nn]\.[A-Za-z0-9]+)|[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}(:[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}_[0-9]{4}(-[0-9]{2}){2})?)$",
        ),
        "billingProfileName": _SERIALIZER.url(
            "billing_profile_name", billing_profile_name, "str", pattern=r"^[a-zA-Z\d-_]{1,128}$"
        ),
        "invoiceSectionName": _SERIALIZER.url(
            "invoice_section_name", invoice_section_name, "str", pattern=r"^[a-zA-Z\d-_]{1,128}$"
        ),
        "transferName": _SERIALIZER.url("transfer_name", transfer_name, "str", pattern=r"^[a-z0-9]*$"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_cancel_request(
    billing_account_name: str, billing_profile_name: str, invoice_section_name: str, transfer_name: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-04-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/transfers/{transferName}/cancel",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "billingAccountName": _SERIALIZER.url(
            "billing_account_name",
            billing_account_name,
            "str",
            pattern=r"^([0-9]+|([Pp][Cc][Nn]\.[A-Za-z0-9]+)|[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}(:[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}_[0-9]{4}(-[0-9]{2}){2})?)$",
        ),
        "billingProfileName": _SERIALIZER.url(
            "billing_profile_name", billing_profile_name, "str", pattern=r"^[a-zA-Z\d-_]{1,128}$"
        ),
        "invoiceSectionName": _SERIALIZER.url(
            "invoice_section_name", invoice_section_name, "str", pattern=r"^[a-zA-Z\d-_]{1,128}$"
        ),
        "transferName": _SERIALIZER.url("transfer_name", transfer_name, "str", pattern=r"^[a-z0-9]*$"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_request(
    billing_account_name: str, billing_profile_name: str, invoice_section_name: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-04-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/transfers",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "billingAccountName": _SERIALIZER.url(
            "billing_account_name",
            billing_account_name,
            "str",
            pattern=r"^([0-9]+|([Pp][Cc][Nn]\.[A-Za-z0-9]+)|[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}(:[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}_[0-9]{4}(-[0-9]{2}){2})?)$",
        ),
        "billingProfileName": _SERIALIZER.url(
            "billing_profile_name", billing_profile_name, "str", pattern=r"^[a-zA-Z\d-_]{1,128}$"
        ),
        "invoiceSectionName": _SERIALIZER.url(
            "invoice_section_name", invoice_section_name, "str", pattern=r"^[a-zA-Z\d-_]{1,128}$"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class TransfersOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.billing.BillingManagementClient`'s
        :attr:`transfers` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get(
        self,
        billing_account_name: str,
        billing_profile_name: str,
        invoice_section_name: str,
        transfer_name: str,
        **kwargs: Any
    ) -> _models.TransferDetails:
        """Gets a transfer request by ID. The operation is supported only for billing accounts with
        agreement type Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing profile. Required.
        :type billing_profile_name: str
        :param invoice_section_name: The ID that uniquely identifies an invoice section. Required.
        :type invoice_section_name: str
        :param transfer_name: The ID that uniquely identifies a transfer request. Required.
        :type transfer_name: str
        :return: TransferDetails or the result of cls(response)
        :rtype: ~azure.mgmt.billing.models.TransferDetails
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.TransferDetails] = kwargs.pop("cls", None)

        _request = build_get_request(
            billing_account_name=billing_account_name,
            billing_profile_name=billing_profile_name,
            invoice_section_name=invoice_section_name,
            transfer_name=transfer_name,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("TransferDetails", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def initiate(
        self,
        billing_account_name: str,
        billing_profile_name: str,
        invoice_section_name: str,
        transfer_name: str,
        parameters: _models.InitiateTransferRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.TransferDetails:
        """Sends a request to a user in another billing account to transfer billing ownership of their
        subscriptions. The operation is supported only for billing accounts with agreement type
        Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing profile. Required.
        :type billing_profile_name: str
        :param invoice_section_name: The ID that uniquely identifies an invoice section. Required.
        :type invoice_section_name: str
        :param transfer_name: The ID that uniquely identifies a transfer request. Required.
        :type transfer_name: str
        :param parameters: Request parameters that are provided to the initiate transfer operation.
         Required.
        :type parameters: ~azure.mgmt.billing.models.InitiateTransferRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: TransferDetails or the result of cls(response)
        :rtype: ~azure.mgmt.billing.models.TransferDetails
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def initiate(
        self,
        billing_account_name: str,
        billing_profile_name: str,
        invoice_section_name: str,
        transfer_name: str,
        parameters: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.TransferDetails:
        """Sends a request to a user in another billing account to transfer billing ownership of their
        subscriptions. The operation is supported only for billing accounts with agreement type
        Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing profile. Required.
        :type billing_profile_name: str
        :param invoice_section_name: The ID that uniquely identifies an invoice section. Required.
        :type invoice_section_name: str
        :param transfer_name: The ID that uniquely identifies a transfer request. Required.
        :type transfer_name: str
        :param parameters: Request parameters that are provided to the initiate transfer operation.
         Required.
        :type parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: TransferDetails or the result of cls(response)
        :rtype: ~azure.mgmt.billing.models.TransferDetails
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def initiate(
        self,
        billing_account_name: str,
        billing_profile_name: str,
        invoice_section_name: str,
        transfer_name: str,
        parameters: Union[_models.InitiateTransferRequest, IO[bytes]],
        **kwargs: Any
    ) -> _models.TransferDetails:
        """Sends a request to a user in another billing account to transfer billing ownership of their
        subscriptions. The operation is supported only for billing accounts with agreement type
        Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing profile. Required.
        :type billing_profile_name: str
        :param invoice_section_name: The ID that uniquely identifies an invoice section. Required.
        :type invoice_section_name: str
        :param transfer_name: The ID that uniquely identifies a transfer request. Required.
        :type transfer_name: str
        :param parameters: Request parameters that are provided to the initiate transfer operation. Is
         either a InitiateTransferRequest type or a IO[bytes] type. Required.
        :type parameters: ~azure.mgmt.billing.models.InitiateTransferRequest or IO[bytes]
        :return: TransferDetails or the result of cls(response)
        :rtype: ~azure.mgmt.billing.models.TransferDetails
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.TransferDetails] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "InitiateTransferRequest")

        _request = build_initiate_request(
            billing_account_name=billing_account_name,
            billing_profile_name=billing_profile_name,
            invoice_section_name=invoice_section_name,
            transfer_name=transfer_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("TransferDetails", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def cancel(
        self,
        billing_account_name: str,
        billing_profile_name: str,
        invoice_section_name: str,
        transfer_name: str,
        **kwargs: Any
    ) -> _models.TransferDetails:
        """Cancels a transfer request. The operation is supported only for billing accounts with agreement
        type Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing profile. Required.
        :type billing_profile_name: str
        :param invoice_section_name: The ID that uniquely identifies an invoice section. Required.
        :type invoice_section_name: str
        :param transfer_name: The ID that uniquely identifies a transfer request. Required.
        :type transfer_name: str
        :return: TransferDetails or the result of cls(response)
        :rtype: ~azure.mgmt.billing.models.TransferDetails
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.TransferDetails] = kwargs.pop("cls", None)

        _request = build_cancel_request(
            billing_account_name=billing_account_name,
            billing_profile_name=billing_profile_name,
            invoice_section_name=invoice_section_name,
            transfer_name=transfer_name,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("TransferDetails", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list(
        self, billing_account_name: str, billing_profile_name: str, invoice_section_name: str, **kwargs: Any
    ) -> Iterable["_models.TransferDetails"]:
        """Lists the transfer requests for an invoice section. The operation is supported only for billing
        accounts with agreement type Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing profile. Required.
        :type billing_profile_name: str
        :param invoice_section_name: The ID that uniquely identifies an invoice section. Required.
        :type invoice_section_name: str
        :return: An iterator like instance of either TransferDetails or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.billing.models.TransferDetails]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.TransferDetailsListResult] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_request(
                    billing_account_name=billing_account_name,
                    billing_profile_name=billing_profile_name,
                    invoice_section_name=invoice_section_name,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("TransferDetailsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)
