# ------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -------------------------------------------------------------------------

from azure.appconfiguration.provider import load, SettingSelector
from sample_utilities import get_client_modifications
import os

kwargs = get_client_modifications()
connection_string = os.environ["APPCONFIGURATION_CONNECTION_STRING"]

# Loading configuration settings from a snapshot
# Note: The snapshot must already exist in your App Configuration store
snapshot_name = "my-snapshot-name"
snapshot_selects = [SettingSelector(snapshot_name=snapshot_name)]
config = load(connection_string=connection_string, selects=snapshot_selects, **kwargs)

print("Configuration settings from snapshot:")
for key, value in config.items():
    print(f"{key}: {value}")

# You can also combine snapshot-based selectors with regular selectors
# The snapshot settings and filtered settings will be merged, with later selectors taking precedence
mixed_selects = [
    SettingSelector(snapshot_name=snapshot_name),  # Load all settings from snapshot
    SettingSelector(key_filter="override.*", label_filter="prod"),  # Also load specific override settings
]
config_mixed = load(connection_string=connection_string, selects=mixed_selects, **kwargs)

print("\nMixed configuration (snapshot + filtered settings):")
for key, value in config_mixed.items():
    print(f"{key}: {value}")

# Loading feature flags from a snapshot
# Feature flags in snapshots will be loaded just like regular configuration settings
feature_flag_selects = [SettingSelector(snapshot_name=snapshot_name)]
config_with_flags = load(
    connection_string=connection_string,
    selects=feature_flag_selects,
    feature_flag_enabled=True,
    feature_flag_selectors=feature_flag_selects,
    **kwargs,
)

print(
    f"\nConfiguration includes feature flags: {any(key.startswith('.appconfig.featureflag/') for key in config_with_flags.keys())}"
)
