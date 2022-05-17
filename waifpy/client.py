from .http import HTTPClient
from .cache import Cache
from .models import NotSafeForWork
from .models import SafeForWork

__all__ = ["Client"]


class Client(Cache):
    def __init__(self, *, cachable: bool = False, http: HTTPClient) -> None:
        super().__init__(cachable)
        self.http = http

    @property
    def nsfw(self) -> NotSafeForWork:
        return NotSafeForWork(self.http)

    @property
    def sfw(self) -> SafeForWork:
        return SafeForWork(self.http)
