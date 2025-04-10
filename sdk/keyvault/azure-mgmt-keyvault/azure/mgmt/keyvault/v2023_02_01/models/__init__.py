# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models_py3 import (  # type: ignore
    AccessPolicyEntry,
    Action,
    Attributes,
    CheckMhsmNameAvailabilityParameters,
    CheckMhsmNameAvailabilityResult,
    CheckNameAvailabilityResult,
    CloudErrorBody,
    DeletedManagedHsm,
    DeletedManagedHsmListResult,
    DeletedManagedHsmProperties,
    DeletedVault,
    DeletedVaultListResult,
    DeletedVaultProperties,
    DimensionProperties,
    Error,
    IPRule,
    Key,
    KeyAttributes,
    KeyCreateParameters,
    KeyListResult,
    KeyProperties,
    KeyReleasePolicy,
    KeyRotationPolicyAttributes,
    LifetimeAction,
    LogSpecification,
    MHSMGeoReplicatedRegion,
    MHSMIPRule,
    MHSMNetworkRuleSet,
    MHSMPrivateEndpoint,
    MHSMPrivateEndpointConnection,
    MHSMPrivateEndpointConnectionItem,
    MHSMPrivateEndpointConnectionsListResult,
    MHSMPrivateLinkResource,
    MHSMPrivateLinkResourceListResult,
    MHSMPrivateLinkServiceConnectionState,
    MHSMRegionsListResult,
    MHSMVirtualNetworkRule,
    ManagedHSMSecurityDomainProperties,
    ManagedHsm,
    ManagedHsmAction,
    ManagedHsmError,
    ManagedHsmKey,
    ManagedHsmKeyAttributes,
    ManagedHsmKeyCreateParameters,
    ManagedHsmKeyListResult,
    ManagedHsmKeyProperties,
    ManagedHsmKeyReleasePolicy,
    ManagedHsmKeyRotationPolicyAttributes,
    ManagedHsmLifetimeAction,
    ManagedHsmListResult,
    ManagedHsmProperties,
    ManagedHsmResource,
    ManagedHsmRotationPolicy,
    ManagedHsmSku,
    ManagedHsmTrigger,
    MetricSpecification,
    NetworkRuleSet,
    Operation,
    OperationDisplay,
    OperationListResult,
    Permissions,
    PrivateEndpoint,
    PrivateEndpointConnection,
    PrivateEndpointConnectionItem,
    PrivateEndpointConnectionListResult,
    PrivateLinkResource,
    PrivateLinkResourceListResult,
    PrivateLinkServiceConnectionState,
    ProxyResourceWithoutSystemData,
    Resource,
    ResourceListResult,
    RotationPolicy,
    Secret,
    SecretAttributes,
    SecretCreateOrUpdateParameters,
    SecretListResult,
    SecretPatchParameters,
    SecretPatchProperties,
    SecretProperties,
    ServiceSpecification,
    Sku,
    SystemData,
    Trigger,
    Vault,
    VaultAccessPolicyParameters,
    VaultAccessPolicyProperties,
    VaultCheckNameAvailabilityParameters,
    VaultCreateOrUpdateParameters,
    VaultListResult,
    VaultPatchParameters,
    VaultPatchProperties,
    VaultProperties,
    VirtualNetworkRule,
)

from ._key_vault_management_client_enums import (  # type: ignore
    AccessPolicyUpdateKind,
    ActionsRequired,
    ActivationStatus,
    CertificatePermissions,
    CreateMode,
    DeletionRecoveryLevel,
    GeoReplicationRegionProvisioningState,
    IdentityType,
    JsonWebKeyCurveName,
    JsonWebKeyOperation,
    JsonWebKeyType,
    KeyPermissions,
    KeyRotationPolicyActionType,
    ManagedHsmSkuFamily,
    ManagedHsmSkuName,
    NetworkRuleAction,
    NetworkRuleBypassOptions,
    PrivateEndpointConnectionProvisioningState,
    PrivateEndpointServiceConnectionStatus,
    ProvisioningState,
    PublicNetworkAccess,
    Reason,
    SecretPermissions,
    SkuFamily,
    SkuName,
    StoragePermissions,
    VaultProvisioningState,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AccessPolicyEntry",
    "Action",
    "Attributes",
    "CheckMhsmNameAvailabilityParameters",
    "CheckMhsmNameAvailabilityResult",
    "CheckNameAvailabilityResult",
    "CloudErrorBody",
    "DeletedManagedHsm",
    "DeletedManagedHsmListResult",
    "DeletedManagedHsmProperties",
    "DeletedVault",
    "DeletedVaultListResult",
    "DeletedVaultProperties",
    "DimensionProperties",
    "Error",
    "IPRule",
    "Key",
    "KeyAttributes",
    "KeyCreateParameters",
    "KeyListResult",
    "KeyProperties",
    "KeyReleasePolicy",
    "KeyRotationPolicyAttributes",
    "LifetimeAction",
    "LogSpecification",
    "MHSMGeoReplicatedRegion",
    "MHSMIPRule",
    "MHSMNetworkRuleSet",
    "MHSMPrivateEndpoint",
    "MHSMPrivateEndpointConnection",
    "MHSMPrivateEndpointConnectionItem",
    "MHSMPrivateEndpointConnectionsListResult",
    "MHSMPrivateLinkResource",
    "MHSMPrivateLinkResourceListResult",
    "MHSMPrivateLinkServiceConnectionState",
    "MHSMRegionsListResult",
    "MHSMVirtualNetworkRule",
    "ManagedHSMSecurityDomainProperties",
    "ManagedHsm",
    "ManagedHsmAction",
    "ManagedHsmError",
    "ManagedHsmKey",
    "ManagedHsmKeyAttributes",
    "ManagedHsmKeyCreateParameters",
    "ManagedHsmKeyListResult",
    "ManagedHsmKeyProperties",
    "ManagedHsmKeyReleasePolicy",
    "ManagedHsmKeyRotationPolicyAttributes",
    "ManagedHsmLifetimeAction",
    "ManagedHsmListResult",
    "ManagedHsmProperties",
    "ManagedHsmResource",
    "ManagedHsmRotationPolicy",
    "ManagedHsmSku",
    "ManagedHsmTrigger",
    "MetricSpecification",
    "NetworkRuleSet",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "Permissions",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionItem",
    "PrivateEndpointConnectionListResult",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkServiceConnectionState",
    "ProxyResourceWithoutSystemData",
    "Resource",
    "ResourceListResult",
    "RotationPolicy",
    "Secret",
    "SecretAttributes",
    "SecretCreateOrUpdateParameters",
    "SecretListResult",
    "SecretPatchParameters",
    "SecretPatchProperties",
    "SecretProperties",
    "ServiceSpecification",
    "Sku",
    "SystemData",
    "Trigger",
    "Vault",
    "VaultAccessPolicyParameters",
    "VaultAccessPolicyProperties",
    "VaultCheckNameAvailabilityParameters",
    "VaultCreateOrUpdateParameters",
    "VaultListResult",
    "VaultPatchParameters",
    "VaultPatchProperties",
    "VaultProperties",
    "VirtualNetworkRule",
    "AccessPolicyUpdateKind",
    "ActionsRequired",
    "ActivationStatus",
    "CertificatePermissions",
    "CreateMode",
    "DeletionRecoveryLevel",
    "GeoReplicationRegionProvisioningState",
    "IdentityType",
    "JsonWebKeyCurveName",
    "JsonWebKeyOperation",
    "JsonWebKeyType",
    "KeyPermissions",
    "KeyRotationPolicyActionType",
    "ManagedHsmSkuFamily",
    "ManagedHsmSkuName",
    "NetworkRuleAction",
    "NetworkRuleBypassOptions",
    "PrivateEndpointConnectionProvisioningState",
    "PrivateEndpointServiceConnectionStatus",
    "ProvisioningState",
    "PublicNetworkAccess",
    "Reason",
    "SecretPermissions",
    "SkuFamily",
    "SkuName",
    "StoragePermissions",
    "VaultProvisioningState",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
