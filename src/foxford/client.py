"""

Contains the Client, which is the core object at the center of all foxford applications.

"""

from typing import Union, List

from .partials.partialuser import PartialUser
from .bases.baseuser import BaseUser
from .partials.partiallevel import PartialLevel
from .bases.baselevel import BaseLevel
from .users import User
from .level import Level
from .utilities.exceptions import BadRequest, NotFound, UserNotFound
from .utilities.requests import Requests

import asyncio

class Client:
    """
    Represents a Foxford client.

    Attributes:
        requests: The requests object, which is used to send requests to Foxford endpoints.
    """

    def __init__(self, cookie: str = None):
        """
        It is recommended to get cookies with EditThisCookie plugin thru export button

        Arguments:
            cookie: A Foxford cookie to login with. (_fox_session cookie)
        """
        self._requests: Requests = Requests()
        self.requests: Requests = self._requests

        self.loop = asyncio.get_event_loop()

        if cookie:
            self.set_cookie(cookie)
        else:
            raise Exception("No cookie provided")

    def __repr__(self):
        return f"<{self.__class__.__name__}>"

    # Authentication
    def set_cookie(self, cookie: str) -> None:
        """
        Authenticates the client with the passed Foxford cookie.
        This method does not send any requests and will not throw if the cookie is invalid.
        It is recommended to get cookies with EditThisCookie plugin thru export button

        Arguments:
            cookie: A Foxford cookie to login with.

        """
        self._requests.session.cookies["_fox_session"] = cookie

    # Users
    async def get_user(
            self, expand: bool = True
    ) -> Union[User, PartialUser]:
        """
        Grabs the authenticated user.

        Arguments:
            expand: Whether to return a User rather than a PartialUser

        Returns:
            The authenticated user.
        """
        authenticated_user_response = await self._requests.get(url="https://foxford.ru/api/user/me")
        authenticated_user_data = authenticated_user_response.json()

        if expand:
            return User(data=authenticated_user_data)
        else:
            return PartialUser(data=authenticated_user_data)
        
    async def get_level(
            self, expand: bool = True
            ) -> Union[Level, PartialLevel]:
        """
        Grabs the authenticated user's level.

        Arguments:
            expand: Whether to return a Level rather than a PartialLevel

        Returns:
            The authenticated user's level.
        """
        level_response = await self._requests.get(url="https://foxford.ru/api/user/level")
        level_data = level_response.json()

        if expand:
            return Level(data=level_data)
        else:
            return PartialLevel(data=level_data)

    async def get_ulms_token(self):
        """
        Get ulms token for your usages

        Returns:
            ulms_token: json with ["access_token"] and ["token_type"]
        """
        token_response = await self._requests.post(url="https://foxford.ru/api/user/ulms_token")
        token_data = token_response.json()

        return token_data
    
    async def custom_request(self, method, url, *args):
        """
        Send method request to url with *args

        Example:
            await custom_request("GET", "https://foxford.ru/api/current_reminders")

        Arguments:
            method: one of the methods: GET, POST, PUT, DELETE
            url: url to send request to
        """
        response = await self._requests.request(method=method, url=url, *args)
        data = response.json()

        return data