"""

This file contains partial objects related to Foxford level.

"""

from ..bases.baselevel import BaseLevel

class PartialLevel(BaseLevel):
    """
    Represents partial level information.

    Attributes:
        level: The user's level
    """

    def __init__(self, data: dict):
        """
        Arguments:
            data: The data from the endpoint.
        """

        self.level: str = data.get("level")

        super().__init__(level=self.level)

    def __repr__(self):
        return f"<{self.__class__.__name__} level={self.level!r}>"