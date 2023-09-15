from browser_cookie3 import Opera
from foxford import get_cookie
from foxford import Client

ffclient = Client(get_cookie(Opera))

async def main():
    objectives = await ffclient.custom_request("GET", "https://foxford.ru/api/user/objectives")
    for objective in objectives:
        print(f"Objective №{objectives.index(objective)+1}") # +1 cuz python lmao
        print("=================================")
        print(objective["title"])
        print(objective["subtitle"])
        print("=================================")

ffclient.loop.run_until_complete(main())