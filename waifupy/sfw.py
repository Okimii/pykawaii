from http import HTTPClient

__all__ = ("SafeForWork",)

class SafeForWork:

    _http = HTTPClient()
    _type = "sfw"
    _url = "url"

    async def waifu(self) -> str:
        return (await self._http._request(self._type, "waifu"))[self._url]

    async def neko(self) -> str:
        return (await self._http._request(self._type, "neko"))[self._url]

    async def shinobu(self) -> str:
        return (await self._http._request(self._type, "shinobu"))[self._url]

    async def bully(self) -> str:
        return (await self._http._request(self._type, "bully"))[self._url]

    async def cuddle(self) -> str:
        return (await self._http._request(self._type, "cuddle"))[self._url]

    async def megumin(self) -> str:
        return (await self._http._request(self._type, "megumin"))[self._url]

    async def cry(self) -> str:
        return (await self._http._request(self._type, "cry"))[self._url]

    async def hug(self) -> str:
        return (await self._http._request(self._type, "hug"))[self._url]

    async def awoo(self) -> str:
        return (await self._http._request(self._type, "awoo"))[self._url]

    async def kiss(self) -> str:
        return (await self._http._request(self._type, "kiss"))[self._url]

    async def lick(self) -> str:
        return (await self._http._request(self._type, "lick"))[self._url]

    async def pat(self) -> str:
        return (await self._http._request(self._type, "pat"))[self._url]

    async def wave(self) -> str:
        return (await self._http._request(self._type, "wave"))[self._url]

    async def smug(self) -> str:
        return (await self._http._request(self._type, "smug"))[self._url]

    async def bonk(self) -> str:
        return (await self._http._request(self._type, "bonk"))[self._url]

    async def yeet(self) -> str:
        return (await self._http._request(self._type, "yeet"))[self._url]

    async def blush(self) -> str:
        return (await self._http._request(self._type, "blush"))[self._url]

    async def smile(self) -> str:
        return (await self._http._request(self._type, "smile"))[self._url]

    async def highfive(self) -> str:
        return (await self._http._request(self._type, "highfive"))[self._url]

    async def handhold(self) -> str:
        return (await self._http._request(self._type, "handhold"))[self._url]

    async def nom(self) -> str:
        return (await self._http._request(self._type, "nom"))[self._url]

    async def bite(self) -> str:
        return (await self._http._request(self._type, "bite"))[self._url]

    async def glomp(self) -> str:
        return (await self._http._request(self._type, "glomp"))[self._url]

    async def slap(self) -> str:
        return (await self._http._request(self._type, "slap"))[self._url]

    async def kill(self) -> str:
        return (await self._http._request(self._type, "kill"))[self._url]

    async def wink(self) -> str:
        return (await self._http._request(self._type, "wink"))[self._url]

    async def kick(self) -> str:
        return (await self._http._request(self._type, "kick"))[self._url]

    async def poke(self) -> str:
        return (await self._http._request(self._type, "poke"))[self._url]

    async def happy(self) -> str:
        return (await self._http._request(self._type, "happy"))[self._url]

    async def dance(self) -> str:
        return (await self._http._request(self._type, "dance"))[self._url]

    async def cringe(self) -> str:
        return (await self._http._request(self._type, "cringe"))[self._url]


Sfw = SafeForWork()
