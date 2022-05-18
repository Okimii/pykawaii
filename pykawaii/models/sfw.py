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

__all__ = ("SafeForWork",)


class SafeForWork:

    """
    Represents the SafeForWork category.
    
    Parameters
    ----------
    client: :class:`Client` the class to use as the main HTTP client.
    """

    TYPE = "sfw"
    
    def __init__(self, client: "Client", /) -> None:
        self.http = client

    async def waifu(self) -> str:

        """
        Safe for work image url of a waifu.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "waifu"))

    async def neko(self) -> str:

        """
        Safe for work image url of a neko.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "neko"))

    async def shinobu(self) -> str:
        
        """
        Safe for work image url of a shinobu.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "shinobu"))

    async def bully(self) -> str:
        
        """
        Safe for work image url of a bully.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "bully"))

    async def cuddle(self) -> str:
        
        """
        Safe for work image url of a cuddle.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "cuddle"))
    async def megumin(self) -> str:
        
        """
        Safe for work image url of a megumin.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "megumin"))

    async def cry(self) -> str:
        
        """
        Safe for work image url of a cry.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "cry"))

    async def hug(self) -> str:
        
        """
        Safe for work image url of a hug.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "hug"))

    async def awoo(self) -> str:
        
        """
        Safe for work image url of a awoo.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "awoo"))

    async def kiss(self) -> str:
        
        """
        Safe for work image url of a kiss.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "kiss"))

    async def lick(self) -> str:
        
        """
        Safe for work image url of a lick.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "lick"))

    async def pat(self) -> str:
        
        """
        Safe for work image url of a pat.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "pat"))

    async def wave(self) -> str:
        
        """
        Safe for work image url of a wave.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "wave"))

    async def smug(self) -> str:
        
        """
        Safe for work image url of a smug.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "smug"))

    async def bonk(self) -> str:
        
        """
        Safe for work image url of a bonk.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "bonk"))

    async def yeet(self) -> str:
        
        """
        Safe for work image url of a yeet.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "yeet"))

    async def blush(self) -> str:
        
        """
        Safe for work image url of a blush.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "blush"))

    async def smile(self) -> str:
        
        """
        Safe for work image url of a smile.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "smile"))

    async def highfive(self) -> str:
        
        """
        Safe for work image url of a highfive.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "highfive"))

    async def handhold(self) -> str:
        
        """
        Safe for work image url of a handhold.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "handhold"))

    async def nom(self) -> str:
        
        """
        Safe for work image url of a nom.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "nom"))

    async def bite(self) -> str:
        
        """
        Safe for work image url of a bite.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "bite"))

    async def glomp(self) -> str:
        
        """
        Safe for work image url of a glomp.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "glomp"))

    async def slap(self) -> str:
        
        """
        Safe for work image url of a slap.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "slap"))

    async def kill(self) -> str:
        
        """
        Safe for work image url of a kill.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "kill"))

    async def wink(self) -> str:
        
        """
        Safe for work image url of a wink.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "wink"))

    async def kick(self) -> str:
        
        """
        Safe for work image url of a kick.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "kick"))

    async def poke(self) -> str:
        
        """
        Safe for work image url of a poke.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "poke"))

    async def happy(self) -> str:
        
        """
        Safe for work image url of a happy.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "happy"))

    async def dance(self) -> str:
        
        """
        Safe for work image url of a dance.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "dance"))

    async def cringe(self) -> str:
        
        """
        Safe for work image url of a cringe.
        
        Returns
        -------
        :class:`str`
        """

        return (await self.http.request(self.TYPE, "cringe"))

