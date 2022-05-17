"""
MIT License

Copyright (c) 2022 Okimii

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from ..client import Client

__all__ = ("SafeForWork",)


class SafeForWork:

    """
    Represents the SafeForWork category.
    
    Parameters
    ----------
    client: :class:`Client` the class to use as the main HTTP client.
    """

    TYPE = "sfw"
    URL = "URL"

    def __init__(self, client: Client, /) -> None:
        self.http = client()

    async def waifu(self) -> str:

        """
        Safe for work image url of a waifu.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "waifu"))[self.URL]

    async def neko(self) -> str:

        """
        Safe for work image url of a neko.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "neko"))[self.URL]

    async def shinobu(self) -> str:
        
        """
        Safe for work image url of a shinobu.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "shinobu"))[self.URL]

    async def bully(self) -> str:
        
        """
        Safe for work image url of a bully.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "bully"))[self.URL]

    async def cuddle(self) -> str:
        
        """
        Safe for work image url of a cuddle.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "cuddle"))[self.URL]

    async def megumin(self) -> str:
        
        """
        Safe for work image url of a megumin.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "megumin"))[self.URL]

    async def cry(self) -> str:
        
        """
        Safe for work image url of a cry.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "cry"))[self.URL]

    async def hug(self) -> str:
        
        """
        Safe for work image url of a hug.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "hug"))[self.URL]

    async def awoo(self) -> str:
        
        """
        Safe for work image url of a awoo.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "awoo"))[self.URL]

    async def kiss(self) -> str:
        
        """
        Safe for work image url of a kiss.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "kiss"))[self.URL]

    async def lick(self) -> str:
        
        """
        Safe for work image url of a lick.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "lick"))[self.URL]

    async def pat(self) -> str:
        
        """
        Safe for work image url of a pat.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "pat"))[self.URL]

    async def wave(self) -> str:
        
        """
        Safe for work image url of a wave.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "wave"))[self.URL]

    async def smug(self) -> str:
        
        """
        Safe for work image url of a smug.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "smug"))[self.URL]

    async def bonk(self) -> str:
        
        """
        Safe for work image url of a bonk.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "bonk"))[self.URL]

    async def yeet(self) -> str:
        
        """
        Safe for work image url of a yeet.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "yeet"))[self.URL]

    async def blush(self) -> str:
        
        """
        Safe for work image url of a blush.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "blush"))[self.URL]

    async def smile(self) -> str:
        
        """
        Safe for work image url of a smile.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "smile"))[self.URL]

    async def highfive(self) -> str:
        
        """
        Safe for work image url of a highfive.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "highfive"))[self.URL]

    async def handhold(self) -> str:
        
        """
        Safe for work image url of a handhold.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "handhold"))[self.URL]

    async def nom(self) -> str:
        
        """
        Safe for work image url of a nom.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "nom"))[self.URL]

    async def bite(self) -> str:
        
        """
        Safe for work image url of a bite.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "bite"))[self.URL]

    async def glomp(self) -> str:
        
        """
        Safe for work image url of a glomp.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "glomp"))[self.URL]

    async def slap(self) -> str:
        
        """
        Safe for work image url of a slap.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "slap"))[self.URL]

    async def kill(self) -> str:
        
        """
        Safe for work image url of a kill.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "kill"))[self.URL]

    async def wink(self) -> str:
        
        """
        Safe for work image url of a wink.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "wink"))[self.URL]

    async def kick(self) -> str:
        
        """
        Safe for work image url of a kick.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "kick"))[self.URL]

    async def poke(self) -> str:
        
        """
        Safe for work image url of a poke.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "poke"))[self.URL]

    async def happy(self) -> str:
        
        """
        Safe for work image url of a happy.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "happy"))[self.URL]

    async def dance(self) -> str:
        
        """
        Safe for work image url of a dance.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "dance"))[self.URL]

    async def cringe(self) -> str:
        
        """
        Safe for work image url of a cringe.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "cringe"))[self.URL]


Sfw = SafeForWork
