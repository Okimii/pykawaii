from aiohttp import ClientSession


class HTTPClient:

    _base = "https://api.waifu.pics/"

    async def _request(self, type: str, category: str, /) -> dict[str, str]:
        async with ClientSession() as session:
            async with session.get(f"{self._base}{type}/{category}") as response:
                return await response.json()
