"""Class that manages dns lookup"""

import socket

from ctrl_node.common.utils import clean_console
from ctrl_node.variables.globals import TERMINAL_PROMPT
from ctrl_node.variables.logos import HOST_TO_IP_LOGO


class HostToIp:
    def __init__(self, host=None):
        """
        Initializes the class with the host to retrieve the IP.
        """
        clean_console()
        print(HOST_TO_IP_LOGO)

        self.host = host or askforhost()

    def get_ip_from_hostname(self):
        print(f"The IP for {self.host} is {socket.gethostbyname(self.host)}")
        self.complete()

    def complete(self):
        """Shows the complete message and calls back the class"""
        input("\nCompleted, press enter to go back.")
