from browser_cookie3 import Opera
from foxford import get_cookie
from foxford import Client

ffclient = Client(get_cookie(Opera))

async def main():
    user = await ffclient.get_user()
    print(user.full_name)

ffclient.loop.run_until_complete(main())