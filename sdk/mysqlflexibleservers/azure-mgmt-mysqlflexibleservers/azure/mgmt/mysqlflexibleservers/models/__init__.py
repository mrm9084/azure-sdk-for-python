# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AdministratorListResult
from ._models_py3 import AdvancedThreatProtection
from ._models_py3 import AdvancedThreatProtectionForUpdate
from ._models_py3 import AdvancedThreatProtectionListResult
from ._models_py3 import AzureADAdministrator
from ._models_py3 import Backup
from ._models_py3 import BackupAndExportRequest
from ._models_py3 import BackupAndExportResponse
from ._models_py3 import BackupAndExportResponseType
from ._models_py3 import BackupRequestBase
from ._models_py3 import BackupSettings
from ._models_py3 import BackupStoreDetails
from ._models_py3 import CapabilitiesListResult
from ._models_py3 import Capability
from ._models_py3 import CapabilityProperties
from ._models_py3 import CapabilitySetsList
from ._models_py3 import Configuration
from ._models_py3 import ConfigurationForBatchUpdate
from ._models_py3 import ConfigurationListForBatchUpdate
from ._models_py3 import ConfigurationListResult
from ._models_py3 import DataEncryption
from ._models_py3 import Database
from ._models_py3 import DatabaseListResult
from ._models_py3 import DelegatedSubnetUsage
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import FeatureProperty
from ._models_py3 import FirewallRule
from ._models_py3 import FirewallRuleListResult
from ._models_py3 import FullBackupStoreDetails
from ._models_py3 import GetPrivateDnsZoneSuffixResponse
from ._models_py3 import HighAvailability
from ._models_py3 import HighAvailabilityValidationEstimation
from ._models_py3 import ImportFromStorageResponseType
from ._models_py3 import ImportSourceProperties
from ._models_py3 import LogFile
from ._models_py3 import LogFileListResult
from ._models_py3 import Maintenance
from ._models_py3 import MaintenanceListResult
from ._models_py3 import MaintenancePolicy
from ._models_py3 import MaintenanceUpdate
from ._models_py3 import MaintenanceWindow
from ._models_py3 import MySQLServerIdentity
from ._models_py3 import MySQLServerSku
from ._models_py3 import NameAvailability
from ._models_py3 import NameAvailabilityRequest
from ._models_py3 import Network
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OperationProgressResponseType
from ._models_py3 import OperationProgressResult
from ._models_py3 import OperationStatusExtendedResult
from ._models_py3 import OperationStatusResult
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import Provisioning
from ._models_py3 import ProxyResource
from ._models_py3 import Resource
from ._models_py3 import Server
from ._models_py3 import ServerBackup
from ._models_py3 import ServerBackupListResult
from ._models_py3 import ServerBackupV2
from ._models_py3 import ServerBackupV2ListResult
from ._models_py3 import ServerDetachVNetParameter
from ._models_py3 import ServerEditionCapability
from ._models_py3 import ServerEditionCapabilityV2
from ._models_py3 import ServerForUpdate
from ._models_py3 import ServerGtidSetParameter
from ._models_py3 import ServerListResult
from ._models_py3 import ServerRestartParameter
from ._models_py3 import ServerVersionCapability
from ._models_py3 import ServerVersionCapabilityV2
from ._models_py3 import SkuCapability
from ._models_py3 import SkuCapabilityV2
from ._models_py3 import Storage
from ._models_py3 import StorageEditionCapability
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import ValidateBackupResponse
from ._models_py3 import VirtualNetworkSubnetUsageParameter
from ._models_py3 import VirtualNetworkSubnetUsageResult

from ._my_sql_management_client_enums import AdministratorName
from ._my_sql_management_client_enums import AdministratorType
from ._my_sql_management_client_enums import AdvancedThreatProtectionName
from ._my_sql_management_client_enums import AdvancedThreatProtectionProvisioningState
from ._my_sql_management_client_enums import AdvancedThreatProtectionState
from ._my_sql_management_client_enums import BackupFormat
from ._my_sql_management_client_enums import BackupType
from ._my_sql_management_client_enums import ConfigurationSource
from ._my_sql_management_client_enums import CreateMode
from ._my_sql_management_client_enums import CreatedByType
from ._my_sql_management_client_enums import DataEncryptionType
from ._my_sql_management_client_enums import EnableStatusEnum
from ._my_sql_management_client_enums import HighAvailabilityMode
from ._my_sql_management_client_enums import HighAvailabilityState
from ._my_sql_management_client_enums import ImportSourceStorageType
from ._my_sql_management_client_enums import IsConfigPendingRestart
from ._my_sql_management_client_enums import IsDynamicConfig
from ._my_sql_management_client_enums import IsReadOnly
from ._my_sql_management_client_enums import MaintenanceProvisioningState
from ._my_sql_management_client_enums import MaintenanceState
from ._my_sql_management_client_enums import MaintenanceType
from ._my_sql_management_client_enums import ManagedServiceIdentityType
from ._my_sql_management_client_enums import ObjectType
from ._my_sql_management_client_enums import OperationStatus
from ._my_sql_management_client_enums import PatchStrategy
from ._my_sql_management_client_enums import PrivateEndpointConnectionProvisioningState
from ._my_sql_management_client_enums import PrivateEndpointServiceConnectionStatus
from ._my_sql_management_client_enums import ProvisioningState
from ._my_sql_management_client_enums import ReplicationRole
from ._my_sql_management_client_enums import ResetAllToDefault
from ._my_sql_management_client_enums import ServerSkuTier
from ._my_sql_management_client_enums import ServerState
from ._my_sql_management_client_enums import ServerVersion
from ._my_sql_management_client_enums import StorageRedundancyEnum
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AdministratorListResult",
    "AdvancedThreatProtection",
    "AdvancedThreatProtectionForUpdate",
    "AdvancedThreatProtectionListResult",
    "AzureADAdministrator",
    "Backup",
    "BackupAndExportRequest",
    "BackupAndExportResponse",
    "BackupAndExportResponseType",
    "BackupRequestBase",
    "BackupSettings",
    "BackupStoreDetails",
    "CapabilitiesListResult",
    "Capability",
    "CapabilityProperties",
    "CapabilitySetsList",
    "Configuration",
    "ConfigurationForBatchUpdate",
    "ConfigurationListForBatchUpdate",
    "ConfigurationListResult",
    "DataEncryption",
    "Database",
    "DatabaseListResult",
    "DelegatedSubnetUsage",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "FeatureProperty",
    "FirewallRule",
    "FirewallRuleListResult",
    "FullBackupStoreDetails",
    "GetPrivateDnsZoneSuffixResponse",
    "HighAvailability",
    "HighAvailabilityValidationEstimation",
    "ImportFromStorageResponseType",
    "ImportSourceProperties",
    "LogFile",
    "LogFileListResult",
    "Maintenance",
    "MaintenanceListResult",
    "MaintenancePolicy",
    "MaintenanceUpdate",
    "MaintenanceWindow",
    "MySQLServerIdentity",
    "MySQLServerSku",
    "NameAvailability",
    "NameAvailabilityRequest",
    "Network",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "OperationProgressResponseType",
    "OperationProgressResult",
    "OperationStatusExtendedResult",
    "OperationStatusResult",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateLinkServiceConnectionState",
    "Provisioning",
    "ProxyResource",
    "Resource",
    "Server",
    "ServerBackup",
    "ServerBackupListResult",
    "ServerBackupV2",
    "ServerBackupV2ListResult",
    "ServerDetachVNetParameter",
    "ServerEditionCapability",
    "ServerEditionCapabilityV2",
    "ServerForUpdate",
    "ServerGtidSetParameter",
    "ServerListResult",
    "ServerRestartParameter",
    "ServerVersionCapability",
    "ServerVersionCapabilityV2",
    "SkuCapability",
    "SkuCapabilityV2",
    "Storage",
    "StorageEditionCapability",
    "SystemData",
    "TrackedResource",
    "UserAssignedIdentity",
    "ValidateBackupResponse",
    "VirtualNetworkSubnetUsageParameter",
    "VirtualNetworkSubnetUsageResult",
    "AdministratorName",
    "AdministratorType",
    "AdvancedThreatProtectionName",
    "AdvancedThreatProtectionProvisioningState",
    "AdvancedThreatProtectionState",
    "BackupFormat",
    "BackupType",
    "ConfigurationSource",
    "CreateMode",
    "CreatedByType",
    "DataEncryptionType",
    "EnableStatusEnum",
    "HighAvailabilityMode",
    "HighAvailabilityState",
    "ImportSourceStorageType",
    "IsConfigPendingRestart",
    "IsDynamicConfig",
    "IsReadOnly",
    "MaintenanceProvisioningState",
    "MaintenanceState",
    "MaintenanceType",
    "ManagedServiceIdentityType",
    "ObjectType",
    "OperationStatus",
    "PatchStrategy",
    "PrivateEndpointConnectionProvisioningState",
    "PrivateEndpointServiceConnectionStatus",
    "ProvisioningState",
    "ReplicationRole",
    "ResetAllToDefault",
    "ServerSkuTier",
    "ServerState",
    "ServerVersion",
    "StorageRedundancyEnum",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
