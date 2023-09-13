"""

foxford 
A modern, asynchronous wrapper for the Foxford's web API.

Copyright 2023-present frostx
License: MIT, see LICENSE

"""

# Find the original here: https://github.com/Rapptz/discord.py/blob/master/discord/__init__.py
# also copied from ro.py lmaooo

__title__ = "foxford"
__author__ = "frostx"
__license__ = "MIT"
__copyright__ = "Copyright 2023-present frostx"
__version__ = "1.1"

import logging
from typing import NamedTuple

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .client import Client
from .utilities.exceptions import *

class VersionInfo(NamedTuple):
    """
    Represents the package's version info.
    """
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(
    major=2,
    minor=0,
    micro=0,
    releaselevel="release",
    serial=0
)

logging.getLogger(__name__).addHandler(logging.NullHandler())