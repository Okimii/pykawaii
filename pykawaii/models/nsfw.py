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

__all__ = ("NotSafeForWork",)


class NotSafeForWork:

    """
    Represents the NotSafeForWork category.
    
    Parameters
    ----------
    client: :class:`Client` the class to use as the main HTTP client.
    """

    TYPE = "nsfw"
    URL = "url"

    def __init__(self, client: Client, /) -> None:
        self.http = client()

    async def waifu(self) -> str:

        """
        Not safe for work image url of a waifu.
        
        Returns
        -------
        :class:`str`
        """

        return (await self._http._request(self.TYPE, "waifu"))[self._URL]

    async def neko(self) -> str:

        """
        Not safe for work image url of a neko.
        
        Returns
        -------
        :class:`str`
        """

        return (await self._http._request(self.TYPE, "neko"))[self._URL]

    async def trap(self) -> str:

        """
        Not safe for work image url of a trap.
        
        Returns
        -------
        :class:`str`
        """

        return (await self._http._request(self.TYPE, "trap"))[self._URL]

    async def blowjob(self) -> str:

        """
        Not safe for work image url of a blowjob.
        
        Returns
        -------
        :class:`str`
        """

        return (await self._http._request(self.TYPE, "blowjob"))[self._URL]


Nsfw = NotSafeForWork
