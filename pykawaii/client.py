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

from .http import HTTPClient
from .cache import Cache
from .models import NotSafeForWork
from .models import SafeForWork

__all__ = ["Client"]


class Client(HTTPClient):
    def __init__(self) -> None:
        self.cache = Cache
        super().__init__(self.cache)

    @property
    def nsfw(self) -> NotSafeForWork:

        """
        nsfw attribute to return an instance of the NotSafeForWork class.
        
        Returns
        -------
        :class:`NotSafeForWork`
        """

        return NotSafeForWork(self)

    @property
    def sfw(self) -> SafeForWork:

        """
        sfw attribute to return an instance of the SafeForWork class.
        
        Returns
        -------
        :class:`SafeForWork`
        """

        return SafeForWork(self)
