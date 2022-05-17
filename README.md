![image](https://user-images.githubusercontent.com/92546867/168890028-97e623d5-04eb-41b0-98ec-6bd4dd922391.png)

Waifupy
=======

Python api wrapper for the waifu.pics api made by: [okimii#0434](https://discord.com/users/637458038915203127)

Key Features
------------

- Object Oriented wrapper
- Type-safety measures.

Installing
----------

**Python 3.7 or higher is required.**

To install the library, you can just run thefollowing command:

``` sh
# Linux/macOS
python3 -m pip install -U waifupy

# Windows
py -3 -m pip install -U waifupy
```

Quick Example
-------------

### Basic Client Example

``` py
import waifupy
from waifupy import HTTPClient

cachable = True # Set to True if you want your client to cache payloads. If you dont want your client to cache paylods you can set the kwarg to False or do not call it.
http = HttpClient

waifu = waifupy.Client(cacheable=cacheable, http=http)

async main() -> None:
    sfw_waifu_payload = await waifu.sfw.waifu()
    nsfw_waifu_payload = await waifu.nsfw.waifu()
    print(sfw_waifu_payload)
    print(nsfw_waifu_payload)

if __name__ == "__main__":
    asyncio.run(main())
```
