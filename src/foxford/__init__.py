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
from typing import NamedTuple, Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .client import Client
from .utilities.exceptions import *

from browser_cookie3 import ChromiumBased, FirefoxBased, Safari
from requests.utils import dict_from_cookiejar
from browser_cookie3 import Opera

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

def get_cookie(browser: Union[FirefoxBased, ChromiumBased, Safari]) -> None:
        """
        Get "cookie" from "browser" thru browser_cookie3 library.

        Arguments:
            browser: Browser to get cookies from (where you logged in with foxford session)

        Returns:
            cookie: The _fox_session cookie you need
                    in set_cookie method or Client class init
        """
        try:
            return dict_from_cookiejar(browser().load())["_fox_session"]
        except:
            raise KeyError("No _fox_session cookie found in cookie jar")