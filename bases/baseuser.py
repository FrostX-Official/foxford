from .baseitem import BaseItem

class BaseUser(BaseItem):
    """
    Represents a Foxford user ID.

    Attributes:
        id: The user ID.
    """

    def __init__(self, user_id: int):
        """
        Arguments:
            user_id: The user ID.
        """

        self.id: int = user_id