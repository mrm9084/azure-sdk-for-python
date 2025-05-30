# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from __future__ import annotations
from enum import Enum
from typing import Dict, Mapping, Optional, Union, Sequence, TypedDict

from ...utils import CaseInsensitiveEnumMeta


AttributeValue = Union[
    str,
    bool,
    int,
    float,
    Sequence[str],
    Sequence[bool],
    Sequence[int],
    Sequence[float],
]
Attributes = Mapping[str, AttributeValue]


class SpanKind(Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the role or kind of a span within a distributed trace.

    This helps to categorize spans based on their relationship to other spans and the type
    of operation they represent.
    """

    UNSPECIFIED = 1
    """Unspecified span kind."""

    SERVER = 2
    """Indicates that the span describes an operation that handles a remote request."""

    CLIENT = 3
    """Indicates that the span describes a request to some remote service."""

    PRODUCER = 4
    """Indicates that the span describes the initiation or scheduling of a local or remote operation."""

    CONSUMER = 5
    """Indicates that the span represents the processing of an operation initiated by a producer."""

    INTERNAL = 6
    """Indicates that the span is used internally in the application."""


class Link:
    """Represents a reference from one span to another span.

    :param headers: A dictionary of the request header as key value pairs.
    :type headers: dict
    :param attributes: Any additional attributes that should be added to link
    :type attributes: dict
    """

    def __init__(self, headers: Dict[str, str], attributes: Optional[Attributes] = None) -> None:
        self.headers = headers
        self.attributes = attributes


class TracingOptions(TypedDict, total=False):
    """Options to configure tracing behavior for operations."""

    enabled: bool
    """Whether tracing is enabled for the operation. By default, if the global setting is enabled, tracing is
    enabled for all operations. This option can be used to override the global setting for a specific operation."""
    attributes: Attributes
    """Attributes to include in the spans emitted for the operation."""
