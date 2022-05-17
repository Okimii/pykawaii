from ..http import HTTPClient

__all__ = ("SafeForWork",)


class SafeForWork:

    TYPE = "sfw"
    URL = "URL"

    def __init__(self, httpclient: HTTPClient, /) -> None:
        self.http = httpclient()

    async def waifu(self) -> str:
        return (await self.http.request(self.TYPE, "waifu"))[self.URL]

    async def neko(self) -> str:
        return (await self.http.request(self.TYPE, "neko"))[self.URL]

    async def shinobu(self) -> str:
        return (await self.http.request(self.TYPE, "shinobu"))[self.URL]

    async def bully(self) -> str:
        return (await self.http.request(self.TYPE, "bully"))[self.URL]

    async def cuddle(self) -> str:
        return (await self.http.request(self.TYPE, "cuddle"))[self.URL]

    async def megumin(self) -> str:
        return (await self.http.request(self.TYPE, "megumin"))[self.URL]

    async def cry(self) -> str:
        return (await self.http.request(self.TYPE, "cry"))[self.URL]

    async def hug(self) -> str:
        return (await self.http.request(self.TYPE, "hug"))[self.URL]

    async def awoo(self) -> str:
        return (await self.http.request(self.TYPE, "awoo"))[self.URL]

    async def kiss(self) -> str:
        return (await self.http.request(self.TYPE, "kiss"))[self.URL]

    async def lick(self) -> str:
        return (await self.http.request(self.TYPE, "lick"))[self.URL]

    async def pat(self) -> str:
        return (await self.http.request(self.TYPE, "pat"))[self.URL]

    async def wave(self) -> str:
        return (await self.http.request(self.TYPE, "wave"))[self.URL]

    async def smug(self) -> str:
        return (await self.http.request(self.TYPE, "smug"))[self.URL]

    async def bonk(self) -> str:
        return (await self.http.request(self.TYPE, "bonk"))[self.URL]

    async def yeet(self) -> str:
        return (await self.http.request(self.TYPE, "yeet"))[self.URL]

    async def blush(self) -> str:
        return (await self.http.request(self.TYPE, "blush"))[self.URL]

    async def smile(self) -> str:
        return (await self.http.request(self.TYPE, "smile"))[self.URL]

    async def highfive(self) -> str:
        return (await self.http.request(self.TYPE, "highfive"))[self.URL]

    async def handhold(self) -> str:
        return (await self.http.request(self.TYPE, "handhold"))[self.URL]

    async def nom(self) -> str:
        return (await self.http.request(self.TYPE, "nom"))[self.URL]

    async def bite(self) -> str:
        return (await self.http.request(self.TYPE, "bite"))[self.URL]

    async def glomp(self) -> str:
        return (await self.http.request(self.TYPE, "glomp"))[self.URL]

    async def slap(self) -> str:
        return (await self.http.request(self.TYPE, "slap"))[self.URL]

    async def kill(self) -> str:
        return (await self.http.request(self.TYPE, "kill"))[self.URL]

    async def wink(self) -> str:
        return (await self.http.request(self.TYPE, "wink"))[self.URL]

    async def kick(self) -> str:
        return (await self.http.request(self.TYPE, "kick"))[self.URL]

    async def poke(self) -> str:
        return (await self.http.request(self.TYPE, "poke"))[self.URL]

    async def happy(self) -> str:
        return (await self.http.request(self.TYPE, "happy"))[self.URL]

    async def dance(self) -> str:
        return (await self.http.request(self.TYPE, "dance"))[self.URL]

    async def cringe(self) -> str:
        return (await self.http.request(self.TYPE, "cringe"))[self.URL]


Sfw = SafeForWork
