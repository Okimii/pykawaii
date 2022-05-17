![image](https://user-images.githubusercontent.com/92546867/168911637-b661ab7d-767d-4e14-8dec-d59c99c8b5ac.png)


Waifpy
=======
[![pypi!](https://img.shields.io/badge/Waifpy-Pypi-yellow](https://pypi.org/project/waifpy/)[![documentation!](https://img.shields.io/badge/Waifpy-Docs-blue)](https://waifpy.readthedocs.io/en/latest/)

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
python3 -m pip install -U waifpy

# Windows
py -3 -m pip install -U waifpy
```

Quick Example
-------------

### Basic Client Example

``` py
import waifpy

waifu = waifpy.Client()

async main() -> None:
    sfw_waifu_payload = await waifu.sfw.waifu()
    nsfw_waifu_payload = await waifu.nsfw.waifu()
    print(sfw_waifu_payload)
    print(nsfw_waifu_payload)

if __name__ == "__main__":
    asyncio.run(main())
```
