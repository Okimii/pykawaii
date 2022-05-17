from ..http import HTTPClient

__all__ = ("NotSafeForWork",)


class NotSafeForWork:

    TYPE = "nsfw"
    URL = "url"

    def __init__(self, httpclient: HTTPClient, /) -> None:
        self.http = httpclient()

    async def waifu(self) -> str:
        return (await self._http._request(self.TYPE, "waifu"))[self._URL]

    async def neko(self) -> str:
        return (await self._http._request(self.TYPE, "neko"))[self._URL]

    async def trap(self) -> str:
        return (await self._http._request(self.TYPE, "trap"))[self._URL]

    async def blowjob(self) -> str:
        return (await self._http._request(self.TYPE, "blowjob"))[self._URL]


Nsfw = NotSafeForWork
