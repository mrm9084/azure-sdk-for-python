# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.carbonoptimization import CarbonOptimizationMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-carbonoptimization
# USAGE
    python query_carbon_emissions_resource_type_item_details_report.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CarbonOptimizationMgmtClient(
        credential=DefaultAzureCredential(),
    )

    response = client.carbon_service.query_carbon_emission_reports(
        query_parameters={
            "carbonScopeList": ["Scope1", "Scope3"],
            "categoryType": "ResourceType",
            "dateRange": {"end": "2024-05-01", "start": "2024-05-01"},
            "orderBy": "LatestMonthEmissions",
            "pageSize": 100,
            "reportType": "ItemDetailsReport",
            "sortDirection": "Desc",
            "subscriptionList": [
                "00000000-0000-0000-0000-000000000000",
                "00000000-0000-0000-0000-000000000001,",
                "00000000-0000-0000-0000-000000000002",
                "00000000-0000-0000-0000-000000000003",
                "00000000-0000-0000-0000-000000000004",
                "00000000-0000-0000-0000-000000000005",
                "00000000-0000-0000-0000-000000000006",
                "00000000-0000-0000-0000-000000000007",
                "00000000-0000-0000-0000-000000000008",
            ],
        },
    )
    print(response)


# x-ms-original-file: 2025-04-01/queryCarbonEmissionsResourceTypeItemDetailsReport.json
if __name__ == "__main__":
    main()
