from http import HTTPClient


class NotSafeForWork:

    _http = HTTPClient()
    _type = "nsfw"
    _url = "url"

    async def waifu(self) -> str:
        return (await self._http._request(self._type, "waifu"))[self._url]

    async def neko(self) -> str:
        return (await self._http._request(self._type, "neko"))[self._url]

    async def trap(self) -> str:
        return (await self._http._request(self._type, "trap"))[self._url]

    async def blowjob(self) -> str:
        return (await self._http._request(self._type, "blowjob"))[self._url]


Nsfw = NotSafeForWork()
