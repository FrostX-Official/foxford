<p align="center" width="100%">
    <a href="https://github.com/frostx-official/foxford">
        <img src="https://raw.githubusercontent.com/frostx-official/foxford/main/resources/logo.png" alt="foxford wrapper logo" height="128em" />
    </a>
    <br>
    <b>Foxford Wrapper</b>
    <br>
</p>

<p align="center">
  <img src="https://img.shields.io/pypi/dm/foxford?logo=pypi&logoColor=white&cacheSeconds=0">
  <img src="https://img.shields.io/github/issues/frostx-official/foxford/bug">
  <img src="https://img.shields.io/pypi/v/foxford?color=green&label=PyPI">
  <img src="https://img.shields.io/github/stars/frostx-official/foxford">
  <img src="https://img.shields.io/github/languages/code-size/frostx-official/foxford?label=repo%20size">
  <img src="https://readthedocs.org/projects/foxford/badge/?version=latest">
</p>

## Example / Boilerplate

```python
from foxford import Client
import asyncio

ffclient = Client("token")

async def main():
    user = await ffclient.get_user()
    print(user.id)

ffclient.loop.run_until_complete(main())
```

## No documentation yet. :(

# Disclaimer
this "framework" uses most of the ro.py's code,<br>
thanks to them for writing it.<br>
i dunno how to properly write frameworks,<br>
so looking at their code and copying lol (sorry pls)
<br><br>
so, here the original roblox api wrapper: https://github.com/ro-py/ro.py<br>
also heavily inspired by vkbottle.

to install/upgrade the latest unstable version of foxford wrapper, install [git-scm](https://git-scm.com/downloads) and run the following:
```
pip install git+https://github.com/frostx-official/foxford.git --upgrade
```
