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


class Client:
    """
    Represents a Foxford client.

    Attributes:
        requests: The requests object, which is used to send requests to Foxford endpoints.
    """

    def __init__(self, cookie: str = None, base_url: str = "foxford.ru"):
        """
        Arguments:
            cookie: A Foxford cookie to login with.
            base_url: The base URL to use when sending requests.
        """
        self._requests: Requests = Requests()
        self.requests: Requests = self._requests

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

        Arguments:
            cookie: A Foxford cookie to login with.

        """
        self._requests.session.cookies = cookie

    # Users
    async def get_authenticated_user(
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
        
    async def get_authenticated_user_level(
            self, expand: bool = True
            ) -> Union[Level, PartialLevel]:
        """
        Grabs the authenticated user's level.

        Arguments:
            expand: Whether to return a Level rather than a PartialLevel

        Returns:
            The authenticated user's level.
        """
        authenticated_user_response = await self._requests.get(url="https://foxford.ru/api/user/level")
        authenticated_user_data = authenticated_user_response.json()

        if expand:
            return Level(data=authenticated_user_data)
        else:
            return PartialLevel(data=authenticated_user_data)