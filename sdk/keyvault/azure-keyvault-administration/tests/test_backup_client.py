# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import time
from functools import partial
from unittest import mock

import pytest
from azure.core.exceptions import ResourceExistsError
from azure.keyvault.administration import KeyVaultBackupClient
from azure.keyvault.administration._internal import parse_folder_url
from devtools_testutils import recorded_by_proxy, set_bodiless_matcher

from _shared.test_case import KeyVaultTestCase
from _test_case import KeyVaultBackupClientPreparer, get_decorator

all_api_versions = get_decorator()


class TestBackupClientTests(KeyVaultTestCase):

    def create_key_client(self, vault_uri, **kwargs):
        from azure.keyvault.keys import KeyClient
        credential = self.get_credential(KeyClient)
        return self.create_client_from_credential(KeyClient, credential=credential, vault_url=vault_uri, **kwargs )

    @pytest.mark.parametrize("api_version", all_api_versions)
    @KeyVaultBackupClientPreparer()
    @recorded_by_proxy
    def test_full_backup_and_restore(self, client, **kwargs):
        set_bodiless_matcher()
        # backup the vault
        container_uri = kwargs.pop("container_uri")
        sas_token = kwargs.pop("sas_token")
        backup_poller = client.begin_backup(container_uri, sas_token)
        backup_operation = backup_poller.result()
        assert backup_operation.folder_url

        # restore the backup
        restore_poller = client.begin_restore(backup_operation.folder_url, sas_token)
        restore_poller.wait()
        if self.is_live:
            time.sleep(60)  # additional waiting to avoid conflicts with resources in other tests

    @pytest.mark.parametrize("api_version", all_api_versions)
    @KeyVaultBackupClientPreparer()
    @recorded_by_proxy
    def test_full_backup_and_restore_rehydration(self, client, **kwargs):
        set_bodiless_matcher()
        container_uri = kwargs.pop("container_uri")
        sas_token = kwargs.pop("sas_token")

        # backup the vault
        backup_poller = client.begin_backup(blob_storage_url=container_uri, sas_token=sas_token)

        # create a new poller from a continuation token
        # pass `sas_token` as a positional parameter to ensure backwards compatibility
        token = backup_poller.continuation_token()
        rehydrated = client.begin_backup(container_uri, sas_token, continuation_token=token)

        rehydrated_operation = rehydrated.result()
        assert rehydrated_operation.folder_url
        backup_operation = backup_poller.result()
        assert backup_operation.folder_url == rehydrated_operation.folder_url

        # restore the backup
        restore_poller = client.begin_restore(folder_url=backup_operation.folder_url, sas_token=sas_token)

        # create a new poller from a continuation token
        # pass `sas_token` as a positional parameter to ensure backwards compatibility
        token = restore_poller.continuation_token()
        rehydrated = client.begin_restore(backup_operation.folder_url, sas_token, continuation_token=token)

        rehydrated.wait()
        restore_poller.wait()
        if self.is_live:
            time.sleep(60)  # additional waiting to avoid conflicts with resources in other tests

    @pytest.mark.parametrize("api_version", all_api_versions)
    @KeyVaultBackupClientPreparer()
    @recorded_by_proxy
    def test_selective_key_restore(self, client, **kwargs):
        set_bodiless_matcher()
        # create a key to selectively restore
        managed_hsm_url = kwargs.pop("managed_hsm_url")
        key_client = self.create_key_client(managed_hsm_url)
        key_name = self.get_resource_name("selective-restore-test-key")
        key_client.create_rsa_key(key_name)


        # backup the vault
        container_uri = kwargs.pop("container_uri")
        sas_token = kwargs.pop("sas_token")
        backup_poller = client.begin_backup(container_uri, sas_token)
        backup_operation = backup_poller.result()

        # restore the key
        restore_poller = client.begin_restore(backup_operation.folder_url, sas_token, key_name=key_name)
        restore_poller.wait()

        # delete the key
        delete_function = partial(key_client.begin_delete_key, key_name)
        delete_poller = self._poll_until_no_exception(delete_function, ResourceExistsError)
        delete_poller.wait()
        key_client.purge_deleted_key(key_name)
        if self.is_live:
            time.sleep(60)  # additional waiting to avoid conflicts with resources in other tests

    @pytest.mark.parametrize("api_version", all_api_versions)
    @KeyVaultBackupClientPreparer()
    @recorded_by_proxy
    def test_backup_client_polling(self, client, **kwargs):
        set_bodiless_matcher()

        # backup the vault
        container_uri = kwargs.pop("container_uri")
        sas_token = kwargs.pop("sas_token")
        backup_poller = client.begin_backup(container_uri, sas_token)

        # create a new poller from a continuation token
        token = backup_poller.continuation_token()
        rehydrated = client.begin_backup(container_uri, sas_token, continuation_token=token)

        # check that pollers and polling methods behave as expected
        if self.is_live:
            assert backup_poller.status() == "InProgress"
            assert not backup_poller.done() or backup_poller.polling_method().finished()
            assert rehydrated.status() == "InProgress"
            assert not rehydrated.done() or rehydrated.polling_method().finished()

        backup_operation = backup_poller.result()
        assert backup_poller.status() == "Succeeded" and backup_poller.polling_method().status() == "Succeeded"
        rehydrated_operation = rehydrated.result()
        assert rehydrated.status() == "Succeeded" and rehydrated.polling_method().status() == "Succeeded"
        assert backup_operation.folder_url == rehydrated_operation.folder_url

        # rehydrate a poller with a continuation token of a completed operation
        late_rehydrated = client.begin_backup(container_uri, sas_token, continuation_token=token)
        assert late_rehydrated.status() == "Succeeded"
        late_rehydrated.wait()

        # restore the backup
        restore_poller = client.begin_restore(backup_operation.folder_url, sas_token)

        # create a new poller from a continuation token
        token = restore_poller.continuation_token()
        rehydrated = client.begin_restore(backup_operation.folder_url, sas_token, continuation_token=token)

        # check that pollers and polling methods behave as expected
        if self.is_live:
            assert restore_poller.status() == "InProgress"
            assert not restore_poller.done() or restore_poller.polling_method().finished()
            assert rehydrated.status() == "InProgress"
            assert not rehydrated.done() or rehydrated.polling_method().finished()

        rehydrated.wait()
        assert rehydrated.status() == "Succeeded" and rehydrated.polling_method().status() == "Succeeded"
        restore_poller.wait()
        assert restore_poller.status() == "Succeeded" and restore_poller.polling_method().status() == "Succeeded"

        if self.is_live:
            time.sleep(60)  # additional waiting to avoid conflicts with resources in other tests


def test_backup_restore_managed_identity():
    """Try first with a non-MI credential to authenticate the client."""
    # backup
    mock_client = mock.Mock()
    client = KeyVaultBackupClient("https://vault-url.vault.azure.net", mock.Mock())
    client._client = mock_client
    client.begin_backup("container_uri", use_managed_identity=True)

    called_with = mock_client.begin_full_backup.call_args
    assert "use_managed_identity" not in called_with[1]  # ensure we pop off the kwarg correctly
    sas_token_parameters = called_with[1]["azure_storage_blob_container_uri"]
    assert sas_token_parameters.use_managed_identity is True

    # full restore
    client.begin_restore("folder_uri", use_managed_identity=True)
    called_with = mock_client.begin_full_restore_operation.call_args
    assert "use_managed_identity" not in called_with[1]  # ensure we pop off the kwarg correctly
    restore_details = called_with[1]["restore_blob_details"]
    sas_token_parameters = restore_details.sas_token_parameters
    assert sas_token_parameters.use_managed_identity is True

    # selective restore
    client.begin_restore("folder_uri", use_managed_identity=True, key_name="key-name")
    called_with = mock_client.begin_selective_key_restore_operation.call_args
    assert "use_managed_identity" not in called_with[1]  # ensure we pop off the kwarg correctly
    assert called_with[1]["key_name"] == "key-name"
    restore_details = called_with[1]["restore_blob_details"]
    sas_token_parameters = restore_details.sas_token_parameters
    assert sas_token_parameters.use_managed_identity is True


@pytest.mark.parametrize(
    "url,expected_container_url,expected_folder_name",
    [
        (
            "https://account.blob.core.windows.net/backup/mhsm-account-2020090117323313",
            "https://account.blob.core.windows.net/backup",
            "mhsm-account-2020090117323313",
        ),
        ("https://account.storage/account/storage", "https://account.storage/account", "storage"),
        ("https://account.storage/a/b/c", "https://account.storage/a", "b/c"),
        ("https://account.storage/a/b-c", "https://account.storage/a", "b-c"),
    ],
)
def test_parse_folder_url(url, expected_container_url, expected_folder_name):
    container_url, folder_name = parse_folder_url(url)
    assert container_url == expected_container_url
    assert folder_name == expected_folder_name
