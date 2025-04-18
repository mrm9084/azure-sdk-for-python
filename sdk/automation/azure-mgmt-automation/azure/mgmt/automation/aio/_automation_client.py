# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING
from typing_extensions import Self

from azure.core.pipeline import policies
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from azure.mgmt.core.policies import AsyncARMAutoResourceProviderRegistrationPolicy

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import AutomationClientConfiguration
from .operations import (
    ActivityOperations,
    AgentRegistrationInformationOperations,
    AutomationAccountOperations,
    AutomationClientOperationsMixin,
    CertificateOperations,
    ConnectionOperations,
    ConnectionTypeOperations,
    CredentialOperations,
    DeletedAutomationAccountsOperations,
    DscCompilationJobOperations,
    DscCompilationJobStreamOperations,
    DscConfigurationOperations,
    DscNodeConfigurationOperations,
    DscNodeOperations,
    FieldsOperations,
    HybridRunbookWorkerGroupOperations,
    HybridRunbookWorkersOperations,
    JobOperations,
    JobScheduleOperations,
    JobStreamOperations,
    KeysOperations,
    LinkedWorkspaceOperations,
    ModuleOperations,
    NodeCountInformationOperations,
    NodeReportsOperations,
    ObjectDataTypesOperations,
    Operations,
    PrivateEndpointConnectionsOperations,
    PrivateLinkResourcesOperations,
    Python2PackageOperations,
    Python3PackageOperations,
    RunbookDraftOperations,
    RunbookOperations,
    ScheduleOperations,
    SoftwareUpdateConfigurationMachineRunsOperations,
    SoftwareUpdateConfigurationRunsOperations,
    SoftwareUpdateConfigurationsOperations,
    SourceControlOperations,
    SourceControlSyncJobOperations,
    SourceControlSyncJobStreamsOperations,
    StatisticsOperations,
    TestJobOperations,
    TestJobStreamsOperations,
    UsagesOperations,
    VariableOperations,
    WatcherOperations,
    WebhookOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class AutomationClient(
    AutomationClientOperationsMixin
):  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Automation Client.

    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.automation.aio.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.automation.aio.operations.PrivateLinkResourcesOperations
    :ivar agent_registration_information: AgentRegistrationInformationOperations operations
    :vartype agent_registration_information:
     azure.mgmt.automation.aio.operations.AgentRegistrationInformationOperations
    :ivar dsc_node: DscNodeOperations operations
    :vartype dsc_node: azure.mgmt.automation.aio.operations.DscNodeOperations
    :ivar node_reports: NodeReportsOperations operations
    :vartype node_reports: azure.mgmt.automation.aio.operations.NodeReportsOperations
    :ivar dsc_compilation_job: DscCompilationJobOperations operations
    :vartype dsc_compilation_job: azure.mgmt.automation.aio.operations.DscCompilationJobOperations
    :ivar dsc_compilation_job_stream: DscCompilationJobStreamOperations operations
    :vartype dsc_compilation_job_stream:
     azure.mgmt.automation.aio.operations.DscCompilationJobStreamOperations
    :ivar node_count_information: NodeCountInformationOperations operations
    :vartype node_count_information:
     azure.mgmt.automation.aio.operations.NodeCountInformationOperations
    :ivar watcher: WatcherOperations operations
    :vartype watcher: azure.mgmt.automation.aio.operations.WatcherOperations
    :ivar software_update_configurations: SoftwareUpdateConfigurationsOperations operations
    :vartype software_update_configurations:
     azure.mgmt.automation.aio.operations.SoftwareUpdateConfigurationsOperations
    :ivar webhook: WebhookOperations operations
    :vartype webhook: azure.mgmt.automation.aio.operations.WebhookOperations
    :ivar deleted_automation_accounts: DeletedAutomationAccountsOperations operations
    :vartype deleted_automation_accounts:
     azure.mgmt.automation.aio.operations.DeletedAutomationAccountsOperations
    :ivar automation_account: AutomationAccountOperations operations
    :vartype automation_account: azure.mgmt.automation.aio.operations.AutomationAccountOperations
    :ivar statistics: StatisticsOperations operations
    :vartype statistics: azure.mgmt.automation.aio.operations.StatisticsOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.automation.aio.operations.UsagesOperations
    :ivar keys: KeysOperations operations
    :vartype keys: azure.mgmt.automation.aio.operations.KeysOperations
    :ivar certificate: CertificateOperations operations
    :vartype certificate: azure.mgmt.automation.aio.operations.CertificateOperations
    :ivar connection: ConnectionOperations operations
    :vartype connection: azure.mgmt.automation.aio.operations.ConnectionOperations
    :ivar connection_type: ConnectionTypeOperations operations
    :vartype connection_type: azure.mgmt.automation.aio.operations.ConnectionTypeOperations
    :ivar credential: CredentialOperations operations
    :vartype credential: azure.mgmt.automation.aio.operations.CredentialOperations
    :ivar dsc_configuration: DscConfigurationOperations operations
    :vartype dsc_configuration: azure.mgmt.automation.aio.operations.DscConfigurationOperations
    :ivar dsc_node_configuration: DscNodeConfigurationOperations operations
    :vartype dsc_node_configuration:
     azure.mgmt.automation.aio.operations.DscNodeConfigurationOperations
    :ivar hybrid_runbook_workers: HybridRunbookWorkersOperations operations
    :vartype hybrid_runbook_workers:
     azure.mgmt.automation.aio.operations.HybridRunbookWorkersOperations
    :ivar hybrid_runbook_worker_group: HybridRunbookWorkerGroupOperations operations
    :vartype hybrid_runbook_worker_group:
     azure.mgmt.automation.aio.operations.HybridRunbookWorkerGroupOperations
    :ivar job: JobOperations operations
    :vartype job: azure.mgmt.automation.aio.operations.JobOperations
    :ivar job_stream: JobStreamOperations operations
    :vartype job_stream: azure.mgmt.automation.aio.operations.JobStreamOperations
    :ivar job_schedule: JobScheduleOperations operations
    :vartype job_schedule: azure.mgmt.automation.aio.operations.JobScheduleOperations
    :ivar linked_workspace: LinkedWorkspaceOperations operations
    :vartype linked_workspace: azure.mgmt.automation.aio.operations.LinkedWorkspaceOperations
    :ivar activity: ActivityOperations operations
    :vartype activity: azure.mgmt.automation.aio.operations.ActivityOperations
    :ivar module: ModuleOperations operations
    :vartype module: azure.mgmt.automation.aio.operations.ModuleOperations
    :ivar object_data_types: ObjectDataTypesOperations operations
    :vartype object_data_types: azure.mgmt.automation.aio.operations.ObjectDataTypesOperations
    :ivar fields: FieldsOperations operations
    :vartype fields: azure.mgmt.automation.aio.operations.FieldsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.automation.aio.operations.Operations
    :ivar python2_package: Python2PackageOperations operations
    :vartype python2_package: azure.mgmt.automation.aio.operations.Python2PackageOperations
    :ivar python3_package: Python3PackageOperations operations
    :vartype python3_package: azure.mgmt.automation.aio.operations.Python3PackageOperations
    :ivar runbook_draft: RunbookDraftOperations operations
    :vartype runbook_draft: azure.mgmt.automation.aio.operations.RunbookDraftOperations
    :ivar runbook: RunbookOperations operations
    :vartype runbook: azure.mgmt.automation.aio.operations.RunbookOperations
    :ivar test_job_streams: TestJobStreamsOperations operations
    :vartype test_job_streams: azure.mgmt.automation.aio.operations.TestJobStreamsOperations
    :ivar test_job: TestJobOperations operations
    :vartype test_job: azure.mgmt.automation.aio.operations.TestJobOperations
    :ivar schedule: ScheduleOperations operations
    :vartype schedule: azure.mgmt.automation.aio.operations.ScheduleOperations
    :ivar software_update_configuration_machine_runs:
     SoftwareUpdateConfigurationMachineRunsOperations operations
    :vartype software_update_configuration_machine_runs:
     azure.mgmt.automation.aio.operations.SoftwareUpdateConfigurationMachineRunsOperations
    :ivar software_update_configuration_runs: SoftwareUpdateConfigurationRunsOperations operations
    :vartype software_update_configuration_runs:
     azure.mgmt.automation.aio.operations.SoftwareUpdateConfigurationRunsOperations
    :ivar source_control: SourceControlOperations operations
    :vartype source_control: azure.mgmt.automation.aio.operations.SourceControlOperations
    :ivar source_control_sync_job: SourceControlSyncJobOperations operations
    :vartype source_control_sync_job:
     azure.mgmt.automation.aio.operations.SourceControlSyncJobOperations
    :ivar source_control_sync_job_streams: SourceControlSyncJobStreamsOperations operations
    :vartype source_control_sync_job_streams:
     azure.mgmt.automation.aio.operations.SourceControlSyncJobStreamsOperations
    :ivar variable: VariableOperations operations
    :vartype variable: azure.mgmt.automation.aio.operations.VariableOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = AutomationClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                AsyncARMAutoResourceProviderRegistrationPolicy(),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: AsyncARMPipelineClient = AsyncARMPipelineClient(base_url=base_url, policies=_policies, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.agent_registration_information = AgentRegistrationInformationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dsc_node = DscNodeOperations(self._client, self._config, self._serialize, self._deserialize)
        self.node_reports = NodeReportsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.dsc_compilation_job = DscCompilationJobOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dsc_compilation_job_stream = DscCompilationJobStreamOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.node_count_information = NodeCountInformationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.watcher = WatcherOperations(self._client, self._config, self._serialize, self._deserialize)
        self.software_update_configurations = SoftwareUpdateConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.webhook = WebhookOperations(self._client, self._config, self._serialize, self._deserialize)
        self.deleted_automation_accounts = DeletedAutomationAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.automation_account = AutomationAccountOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.statistics = StatisticsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.keys = KeysOperations(self._client, self._config, self._serialize, self._deserialize)
        self.certificate = CertificateOperations(self._client, self._config, self._serialize, self._deserialize)
        self.connection = ConnectionOperations(self._client, self._config, self._serialize, self._deserialize)
        self.connection_type = ConnectionTypeOperations(self._client, self._config, self._serialize, self._deserialize)
        self.credential = CredentialOperations(self._client, self._config, self._serialize, self._deserialize)
        self.dsc_configuration = DscConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dsc_node_configuration = DscNodeConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.hybrid_runbook_workers = HybridRunbookWorkersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.hybrid_runbook_worker_group = HybridRunbookWorkerGroupOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.job = JobOperations(self._client, self._config, self._serialize, self._deserialize)
        self.job_stream = JobStreamOperations(self._client, self._config, self._serialize, self._deserialize)
        self.job_schedule = JobScheduleOperations(self._client, self._config, self._serialize, self._deserialize)
        self.linked_workspace = LinkedWorkspaceOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.activity = ActivityOperations(self._client, self._config, self._serialize, self._deserialize)
        self.module = ModuleOperations(self._client, self._config, self._serialize, self._deserialize)
        self.object_data_types = ObjectDataTypesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.fields = FieldsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.python2_package = Python2PackageOperations(self._client, self._config, self._serialize, self._deserialize)
        self.python3_package = Python3PackageOperations(self._client, self._config, self._serialize, self._deserialize)
        self.runbook_draft = RunbookDraftOperations(self._client, self._config, self._serialize, self._deserialize)
        self.runbook = RunbookOperations(self._client, self._config, self._serialize, self._deserialize)
        self.test_job_streams = TestJobStreamsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.test_job = TestJobOperations(self._client, self._config, self._serialize, self._deserialize)
        self.schedule = ScheduleOperations(self._client, self._config, self._serialize, self._deserialize)
        self.software_update_configuration_machine_runs = SoftwareUpdateConfigurationMachineRunsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.software_update_configuration_runs = SoftwareUpdateConfigurationRunsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.source_control = SourceControlOperations(self._client, self._config, self._serialize, self._deserialize)
        self.source_control_sync_job = SourceControlSyncJobOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.source_control_sync_job_streams = SourceControlSyncJobStreamsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.variable = VariableOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(
        self, request: HttpRequest, *, stream: bool = False, **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> Self:
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
