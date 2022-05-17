import aiohttp

__all__ = ["HTTPClient"]


class HTTPClient:

    BASE = "https://api.waifu.pics/"

    async def request(self, type: str, category: str, /) -> dict[str, str]:
        async with aiohttp.request("GET", f"{self.BASE}{type}{category}") as payload:
            return await payload.json()
