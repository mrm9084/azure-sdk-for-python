# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.deviceregistry.aio import DeviceRegistryMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDeviceRegistryMgmtDiscoveredAssetsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(DeviceRegistryMgmtClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_discovered_assets_get(self, resource_group):
        response = await self.client.discovered_assets.get(
            resource_group_name=resource_group.name,
            discovered_asset_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_discovered_assets_begin_create_or_replace(self, resource_group):
        response = await (
            await self.client.discovered_assets.begin_create_or_replace(
                resource_group_name=resource_group.name,
                discovered_asset_name="str",
                resource={
                    "extendedLocation": {"name": "str", "type": "str"},
                    "location": "str",
                    "id": "str",
                    "name": "str",
                    "properties": {
                        "assetEndpointProfileRef": "str",
                        "discoveryId": "str",
                        "version": 0,
                        "datasets": [
                            {
                                "name": "str",
                                "dataPoints": [
                                    {
                                        "dataSource": "str",
                                        "name": "str",
                                        "dataPointConfiguration": "str",
                                        "lastUpdatedOn": "2020-02-20 00:00:00",
                                    }
                                ],
                                "datasetConfiguration": "str",
                                "topic": {"path": "str", "retain": "str"},
                            }
                        ],
                        "defaultDatasetsConfiguration": "str",
                        "defaultEventsConfiguration": "str",
                        "defaultTopic": {"path": "str", "retain": "str"},
                        "documentationUri": "str",
                        "events": [
                            {
                                "eventNotifier": "str",
                                "name": "str",
                                "eventConfiguration": "str",
                                "lastUpdatedOn": "2020-02-20 00:00:00",
                                "topic": {"path": "str", "retain": "str"},
                            }
                        ],
                        "hardwareRevision": "str",
                        "manufacturer": "str",
                        "manufacturerUri": "str",
                        "model": "str",
                        "productCode": "str",
                        "provisioningState": "str",
                        "serialNumber": "str",
                        "softwareRevision": "str",
                    },
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "tags": {"str": "str"},
                    "type": "str",
                },
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_discovered_assets_begin_update(self, resource_group):
        response = await (
            await self.client.discovered_assets.begin_update(
                resource_group_name=resource_group.name,
                discovered_asset_name="str",
                properties={
                    "properties": {
                        "datasets": [
                            {
                                "name": "str",
                                "dataPoints": [
                                    {
                                        "dataSource": "str",
                                        "name": "str",
                                        "dataPointConfiguration": "str",
                                        "lastUpdatedOn": "2020-02-20 00:00:00",
                                    }
                                ],
                                "datasetConfiguration": "str",
                                "topic": {"path": "str", "retain": "str"},
                            }
                        ],
                        "defaultDatasetsConfiguration": "str",
                        "defaultEventsConfiguration": "str",
                        "defaultTopic": {"path": "str", "retain": "str"},
                        "discoveryId": "str",
                        "documentationUri": "str",
                        "events": [
                            {
                                "eventNotifier": "str",
                                "name": "str",
                                "eventConfiguration": "str",
                                "lastUpdatedOn": "2020-02-20 00:00:00",
                                "topic": {"path": "str", "retain": "str"},
                            }
                        ],
                        "hardwareRevision": "str",
                        "manufacturer": "str",
                        "manufacturerUri": "str",
                        "model": "str",
                        "productCode": "str",
                        "serialNumber": "str",
                        "softwareRevision": "str",
                        "version": 0,
                    },
                    "tags": {"str": "str"},
                },
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_discovered_assets_begin_delete(self, resource_group):
        response = await (
            await self.client.discovered_assets.begin_delete(
                resource_group_name=resource_group.name,
                discovered_asset_name="str",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_discovered_assets_list_by_resource_group(self, resource_group):
        response = self.client.discovered_assets.list_by_resource_group(
            resource_group_name=resource_group.name,
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_discovered_assets_list_by_subscription(self, resource_group):
        response = self.client.discovered_assets.list_by_subscription()
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
