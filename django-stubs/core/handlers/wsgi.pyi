from io import BytesIO
from typing import Any, Callable, Dict, Optional, Union

from django.contrib.auth.models import AbstractUser
from django.contrib.sessions.backends.base import SessionBase
from django.core.handlers import base
from django.http import HttpRequest
from django.http.request import QueryDict
from django.http.response import HttpResponse
from django.utils.datastructures import MultiValueDict


_Stream = Union[BytesIO, str]


class LimitedStream:
    stream: _Stream = ...
    remaining: int = ...
    buffer: bytes = ...
    buf_size: int = ...

    def __init__(
            self,
            stream: _Stream,
            limit: int,
            buf_size: int = ...,
    ) -> None: ...

    def read(self, size: Optional[int] = ...) -> bytes: ...

    def readline(self, size: Optional[int] = ...) -> bytes: ...


class WSGIRequest(HttpRequest):
    content_params: Dict[str, str]
    content_type: str
    environ: Dict[str, Any] = ...
    path_info: str = ...
    path: str = ...
    user: AbstractUser
    session: SessionBase

    META: Dict[str, Any] = ...
    method: str = ...
    encoding: Any = ...
    resolver_match: None = ...

    def __init__(self, environ: Dict[str, Any]) -> None: ...

    def GET(self) -> QueryDict: ...

    def COOKIES(self) -> Dict[str, str]: ...

    @property
    def FILES(self) -> MultiValueDict: ...

    POST: Any = ...


class WSGIHandler(base.BaseHandler):
    request_class: Any = ...

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __call__(
            self,
            environ: Dict[str, Any],
            start_response: Callable,
    ) -> HttpResponse: ...


def get_path_info(environ: Dict[str, Any]) -> str: ...


def get_script_name(environ: Dict[str, Any]) -> str: ...


def get_bytes_from_wsgi(
        environ: Dict[str, Any], key: str, default: str
) -> bytes: ...


def get_str_from_wsgi(
        environ: Dict[str, Any], key: str, default: str
) -> str: ...
