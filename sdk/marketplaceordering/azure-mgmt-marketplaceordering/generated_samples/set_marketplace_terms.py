# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.marketplaceordering import MarketplaceOrderingAgreements

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-marketplaceordering
# USAGE
    python set_marketplace_terms.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MarketplaceOrderingAgreements(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.marketplace_agreements.create(
        offer_type="virtualmachine",
        publisher_id="pubid",
        offer_id="offid",
        plan_id="planid",
        parameters={
            "properties": {
                "accepted": False,
                "licenseTextLink": "test.licenseLink",
                "marketplaceTermsLink": "test.marketplaceTermsLink",
                "plan": "planid",
                "privacyPolicyLink": "test.privacyPolicyLink",
                "product": "offid",
                "publisher": "pubid",
                "retrieveDatetime": "2017-08-15T11:33:07.12132Z",
                "signature": "ASDFSDAFWEFASDGWERLWER",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/marketplaceordering/resource-manager/Microsoft.MarketplaceOrdering/stable/2021-01-01/examples/SetMarketplaceTerms.json
if __name__ == "__main__":
    main()
