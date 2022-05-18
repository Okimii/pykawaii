![image](https://user-images.githubusercontent.com/92546867/168926452-28c8d415-0f2f-438a-bdb6-38e182db5b52.png)

Pykawaii
=======
[![pypi!](https://img.shields.io/badge/Pypi-v3.4.0-yellow)](https://pypi.org/project/pykawaii/) [![documentation!](https://img.shields.io/badge/pykawaii-Docs-blue)](https://waifpy.readthedocs.io/en/latest/)

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
python3 -m pip install -U pykawaii

# Windows
py -3 -m pip install -U pykawaii
```

Quick Example
-------------

### Basic Client Example

``` py
import pykawaii
import asyncio

waifu = pykawaii.Client()

async def main() -> None:
    sfw_waifu_payload = await waifu.sfw.waifu()
    nsfw_waifu_payload = await waifu.nsfw.waifu()
    print(sfw_waifu_payload)
    print(nsfw_waifu_payload)

if __name__ == "__main__":
    asyncio.run(main())
```
