from .baseitem import BaseItem

class BaseLevel(BaseItem):
    """
    Represents a Foxford level.

    Attributes:
        id: The user ID.
    """

    def __init__(self, level: int):
        """
        Arguments:
            level: The user ID.
        """

        self.id: int = level