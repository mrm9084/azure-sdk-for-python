# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.workloadssapvirtualinstance import WorkloadsSapVirtualInstanceMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestWorkloadsSapVirtualInstanceMgmtSAPDatabaseInstancesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(WorkloadsSapVirtualInstanceMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_sap_database_instances_get(self, resource_group):
        response = self.client.sap_database_instances.get(
            resource_group_name=resource_group.name,
            sap_virtual_instance_name="str",
            database_instance_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_sap_database_instances_begin_create(self, resource_group):
        response = self.client.sap_database_instances.begin_create(
            resource_group_name=resource_group.name,
            sap_virtual_instance_name="str",
            database_instance_name="str",
            resource={
                "location": "str",
                "id": "str",
                "name": "str",
                "properties": {
                    "databaseSid": "str",
                    "databaseType": "str",
                    "errors": {"properties": {"code": "str", "details": [...], "message": "str"}},
                    "ipAddress": "str",
                    "loadBalancerDetails": {"id": "str"},
                    "provisioningState": "str",
                    "status": "str",
                    "subnet": "str",
                    "vmDetails": [{"status": "str", "storageDetails": [{"id": "str"}], "virtualMachineId": "str"}],
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
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_sap_database_instances_update(self, resource_group):
        response = self.client.sap_database_instances.update(
            resource_group_name=resource_group.name,
            sap_virtual_instance_name="str",
            database_instance_name="str",
            properties={"tags": {"str": "str"}},
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_sap_database_instances_begin_delete(self, resource_group):
        response = self.client.sap_database_instances.begin_delete(
            resource_group_name=resource_group.name,
            sap_virtual_instance_name="str",
            database_instance_name="str",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_sap_database_instances_list(self, resource_group):
        response = self.client.sap_database_instances.list(
            resource_group_name=resource_group.name,
            sap_virtual_instance_name="str",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_sap_database_instances_begin_start(self, resource_group):
        response = self.client.sap_database_instances.begin_start(
            resource_group_name=resource_group.name,
            sap_virtual_instance_name="str",
            database_instance_name="str",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_sap_database_instances_begin_stop(self, resource_group):
        response = self.client.sap_database_instances.begin_stop(
            resource_group_name=resource_group.name,
            sap_virtual_instance_name="str",
            database_instance_name="str",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
