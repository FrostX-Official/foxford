"""

This module contains classes intended to parse and deal with data from Foxford client information endpoints.

"""

from .bases.baselevel import BaseLevel

class Level(BaseLevel):
    """
    Represents a single conversation.

    Attributes:
        gained_xp: The gained xp of user
        level: The level of user
        available_xp: The available xp of user
        progress: The level progress of user
    """

    def __init__(self, data: dict):
        """
        Arguments:
            data: The data from the request.
        """
        super().__init__(level=data["level"])

        self._data: dict = data

        self.level: int = data["level"]
        self.gained_xp: int = data["gained_xp"]
        self.available_xp: int = data["available_xp"]
        self.progress: int = data["progress"]

    def __repr__(self):
        return f"<{self.__class__.__name__} level={self.level!r}>"