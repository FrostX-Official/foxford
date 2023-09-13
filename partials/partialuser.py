"""

This file contains partial objects related to Foxford users.

"""

from ..bases.baseuser import BaseUser

class PartialUser(BaseUser):
    """
    Represents partial user information.

    Attributes:
        id: The user's ID.
        full_name: The user's full name.
    """

    def __init__(self, data: dict):
        """
        Arguments:
            data: The data from the endpoint.
        """

        self.id: int = data.get("id")

        super().__init__(user_id=self.id)

        self.full_name: str = data.get("full_name")

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id} full_name={self.full_name!r}>"