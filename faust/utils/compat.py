"""Compatibility utilities."""
from types import TracebackType
from typing import Any, AnyStr, Type

__all__ = ['DummyContext', 'OrderedDict', 'want_bytes', 'want_str']

#: Dictionaries are ordered by default in Python 3.6
OrderedDict = dict


class DummyContext:
    """Context for with-statement doing nothing."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        ...

    async def __aenter__(self) -> 'DummyContext':
        return self

    async def __aexit__(self,
                        exc_type: Type[Exception],
                        exc_val: Exception,
                        exc_tb: TracebackType) -> None:
        ...

    def __enter__(self) -> 'DummyContext':
        return self

    def __exit__(self,
                 exc_type: Type[Exception],
                 exc_val: Exception,
                 exc_tb: TracebackType) -> Any:
        ...


def want_bytes(s: AnyStr) -> bytes:
    """Convert string to bytes."""
    if isinstance(s, str):
        return s.encode()
    return s


def want_str(s: AnyStr) -> str:
    """Convert bytes to string."""
    if isinstance(s, bytes):
        return s.decode()
    return s
