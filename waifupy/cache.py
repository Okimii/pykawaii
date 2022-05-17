from __future__ import annotations

from typing import Any, Callable

from .errors import CacheDisabled

__all__ = ["Cache"]


class Cache:
    def __init__(self, cachable: bool) -> None:
        self.cachable = cachable
        self.cache: list[str] = []

    def __setattr__(self, name: str, value: Any) -> None:
        setattr(self, name, value)

    def __getattribute__(self, name: str) -> Any:
        getattr(self, name)

    def cachable(self, callable: Callable[..., Any]) -> Any | None:
        def cachechecker():
            if self.cache:
                return callable()
            raise CacheDisabled()

    @cachable
    def getobj(self, index: int) -> str:
        return self.cache[index]

    @cachable
    def setobj(self, value: str) -> None:
        self.cache.append(value)
