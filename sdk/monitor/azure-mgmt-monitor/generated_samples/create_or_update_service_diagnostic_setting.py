# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.monitor import MonitorManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-monitor
# USAGE
    python create_or_update_service_diagnostic_setting.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MonitorManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.service_diagnostic_settings.create_or_update(
        resource_uri="/subscriptions/1a66ce04-b633-4a0b-b2bc-a912ec8986a6/resourcegroups/viruela1/providers/microsoft.logic/workflows/viruela6",
        parameters={
            "location": "",
            "properties": {
                "eventHubAuthorizationRuleId": "/subscriptions/1a66ce04-b633-4a0b-b2bc-a912ec8986a6/resourceGroups/montest/providers/microsoft.eventhub/namespaces/mynamespace/eventhubs/myeventhub/authorizationrules/myrule",
                "logs": [
                    {"category": "WorkflowRuntime", "enabled": True, "retentionPolicy": {"days": 0, "enabled": False}}
                ],
                "metrics": [{"enabled": True, "retentionPolicy": {"days": 0, "enabled": False}, "timeGrain": "PT1M"}],
                "serviceBusRuleId": "/subscriptions/b67f7fec-69fc-4974-9099-a26bd6ffeda3/resourceGroups/andy1101/providers/Microsoft.EventHub/namespaces/andy1101/authorizationrules/RootManageSharedAccessKey",
                "storageAccountId": "/subscriptions/df602c9c-7aa0-407d-a6fb-eb20c8bd1192/resourceGroups/apptest/providers/Microsoft.Storage/storageAccounts/appteststorage1",
                "workspaceId": "",
            },
        },
    )
    print(response)


# x-ms-original-file: specification/monitor/resource-manager/Microsoft.Insights/stable/2016-09-01/examples/createOrUpdateServiceDiagnosticSetting.json
if __name__ == "__main__":
    main()
