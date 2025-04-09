"""Class that manages dns lookup"""

import socket

from ctrl_node.common.utils import askforhost
from ctrl_node.variables.globals import TERMINAL_PROMPT
from ctrl_node.variables.logos import HOST_TO_IP_LOGO


class Version:
    def __init__(self):
        """
        Initializes the class for the version.
        """
        application_version = get_version("ctrl-node")
        print(f"You are running version {application_version} ")
