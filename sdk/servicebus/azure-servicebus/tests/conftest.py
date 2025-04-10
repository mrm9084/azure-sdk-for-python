# ------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -------------------------------------------------------------------------
import pytest
from devtools_testutils.sanitizers import (
    add_remove_header_sanitizer,
    add_general_regex_sanitizer,
    add_oauth_response_sanitizer,
)

collect_ignore = []


@pytest.fixture(scope="session", autouse=True)
def add_sanitizers(test_proxy):
    add_remove_header_sanitizer(headers="aeg-sas-key")
    add_remove_header_sanitizer(headers="aeg-sas-token")
    add_remove_header_sanitizer(headers="ServiceBusSupplementaryAuthorization")
    add_remove_header_sanitizer(headers="ServiceBusDlqSupplementaryAuthorization")
    add_general_regex_sanitizer(value="fakeresource", regex="(?<=\\/\\/)[a-z-]+(?=\\.servicebus\\.windows\\.net)")
    add_oauth_response_sanitizer()


# Note: This is duplicated between here and the basic conftest, so that it does not throw warnings if you're
# running locally to this SDK. (Everything works properly, pytest just makes a bit of noise.)
def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line("markers", "liveTest: mark test to be a live test only")
    config.addinivalue_line("markers", "live_test_only: mark test to be a live test only")
    config.addinivalue_line("markers", "playback_test_only: mark test to be a playback test only")
