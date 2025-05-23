# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from typing import (
    Any, Callable, cast, Dict,
    List, Optional, Tuple, Union
)

from azure.core.exceptions import HttpResponseError
from azure.core.async_paging import AsyncPageIterator

from .._deserialize import (
    get_deleted_path_properties_from_generated_code,
    process_storage_error,
    return_headers_and_deserialized_path_list
)
from .._generated.models import (
    BlobItemInternal,
    BlobPrefix as GenBlobPrefix,
    Path
)
from .._models import DeletedPathProperties, PathProperties
from .._shared.models import DictMixin
from .._shared.response_handlers import return_context_and_deserialized


class DirectoryPrefix(DictMixin):
    """Directory prefix."""

    name: str
    """Name of the directory."""
    results_per_page: int
    """The maximum number of results retrieved per API call."""
    file_system: str
    """The file system that the deleted paths are listed from."""
    delimiter: str
    """A delimiting character used for hierarchy listing."""
    location_mode: str
    """The location mode being used to list results. The available
        options include "primary" and "secondary"."""

    def __init__(self, **kwargs: Any) -> None:
        self.name = kwargs.get('prefix')  # type: ignore [assignment]
        self.results_per_page = kwargs.get('results_per_page')  # type: ignore [assignment]
        self.file_system = kwargs.get('container')  # type: ignore [assignment]
        self.delimiter = kwargs.get('delimiter')  # type: ignore [assignment]
        self.location_mode = kwargs.get('location_mode')  # type: ignore [assignment]


class DeletedPathPropertiesPaged(AsyncPageIterator):
    """An Iterable of deleted path properties."""

    service_endpoint: Optional[str]
    """The service URL."""
    prefix: Optional[str]
    """A path name prefix being used to filter the list."""
    marker: Optional[str]
    """The continuation token of the current page of results."""
    results_per_page: Optional[int]
    """The maximum number of results retrieved per API call."""
    continuation_token: Optional[str]
    """The continuation token to retrieve the next page of results."""
    container: Optional[str]
    """The container that the paths are listed from."""
    delimiter: Optional[str]
    """A delimiting character used for hierarchy listing."""
    current_page: Optional[List[DeletedPathProperties]]
    """The current page of listed results."""
    location_mode: Optional[str]
    """The location mode being used to list results. The available
        options include "primary" and "secondary"."""

    def __init__(
        self, command: Callable,
        container: Optional[str] = None,
        prefix: Optional[str] = None,
        results_per_page: Optional[int] = None,
        continuation_token: Optional[str] = None,
        delimiter: Optional[str] = None,
        location_mode: Optional[str] = None
    ) -> None:
        super(DeletedPathPropertiesPaged, self).__init__(
            get_next=self._get_next_cb,
            extract_data=self._extract_data_cb,
            continuation_token=continuation_token or ""
        )
        self._command = command
        self.service_endpoint = None
        self.prefix = prefix
        self.marker = None
        self.results_per_page = results_per_page
        self.container = container
        self.delimiter = delimiter
        self.current_page = None
        self.location_mode = location_mode

    async def _get_next_cb(self, continuation_token):
        try:
            return await self._command(
                prefix=self.prefix,
                marker=continuation_token or None,
                max_results=self.results_per_page,
                cls=return_context_and_deserialized,
                use_location=self.location_mode
            )
        except HttpResponseError as error:
            process_storage_error(error)

    async def _extract_data_cb(self, get_next_return):
        self.location_mode, self._response = cast(Tuple[Optional[str], Any], get_next_return)
        self.service_endpoint = self._response.service_endpoint
        self.prefix = self._response.prefix
        self.marker = self._response.marker
        self.results_per_page = self._response.max_results
        self.container = self._response.container_name
        self.current_page = self._response.segment.blob_prefixes  + self._response.segment.blob_items
        self.current_page = [self._build_item(item) for item in self.current_page]
        self.delimiter = self._response.delimiter

        return self._response.next_marker or None, self.current_page

    def _build_item(self, item):
        if isinstance(item, BlobItemInternal):
            file_props = get_deleted_path_properties_from_generated_code(item)
            file_props.file_system = self.container
            return file_props
        if isinstance(item, GenBlobPrefix):
            return DirectoryPrefix(
                container=self.container,
                prefix=item.name,
                results_per_page=self.results_per_page,
                location_mode=self.location_mode
            )
        return item


class PathPropertiesPaged(AsyncPageIterator):
    """An Iterable of Path properties."""

    recursive: bool
    """Set True for recursive, False for iterative."""
    results_per_page: Optional[int]
    """The maximum number of results retrieved per API call."""
    path: Optional[str]
    """Filters the results to return only paths under the specified path."""
    upn: Optional[str]
    """If True, the user identity values will be returned as User Principal names.
        If False, the user identity values will be returned as Azure Active Directory Object IDs."""
    current_page: Optional[List[PathProperties]]
    """The current page of listed results."""
    path_list: Optional[List[Path]]
    """The path list to build the items for the current page."""

    def __init__(
        self, command: Callable,
        recursive: bool,
        path: Optional[str] = None,
        max_results: Optional[int] = None,
        continuation_token: Optional[str] = None,
        upn: Optional[str] = None
    ) -> None:
        super(PathPropertiesPaged, self).__init__(
            get_next=self._get_next_cb,
            extract_data=self._extract_data_cb,
            continuation_token=continuation_token or ""
        )
        self._command = command
        self.recursive = recursive
        self.results_per_page = max_results
        self.path = path
        self.upn = upn
        self.current_page = None
        self.path_list = None

    async def _get_next_cb(self, continuation_token):
        try:
            return await self._command(
                self.recursive,
                continuation=continuation_token or None,
                path=self.path,
                max_results=self.results_per_page,
                upn=self.upn,
                cls=return_headers_and_deserialized_path_list
            )
        except HttpResponseError as error:
            process_storage_error(error)

    async def _extract_data_cb(self, get_next_return):
        self.path_list, self._response = cast(Tuple[List[Path], Dict[str, Any]], get_next_return)
        self.current_page = [self._build_item(item) for item in self.path_list]

        return self._response['continuation'] or None, self.current_page

    @staticmethod
    def _build_item(item: Union[Path, PathProperties]) -> PathProperties:
        if isinstance(item, PathProperties):
            return item
        if isinstance(item, Path):
            path = PathProperties._from_generated(item)  # pylint: disable=protected-access
            return path
        return item
