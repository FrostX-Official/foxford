from browser_cookie3 import Opera
from foxford import get_cookie
from foxford import Client
import asyncio

client = Client(get_cookie(Opera))

async def main():
    print(await client.get_user())

asyncio.run(main())