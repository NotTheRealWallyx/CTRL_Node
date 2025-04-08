"""Class that manages dns lookup"""

import socket

from ctrl_node.common.utils import clean_console
from ctrl_node.variables.globals import TERMINAL_PROMPT
from ctrl_node.variables.logos import HOST_TO_IP_LOGO


class HostToIp:
    def __init__(self):
        """
        Clears the console and shows the menu to ask the user
        to select an option.
        """
        clean_console()
        print(
            HOST_TO_IP_LOGO
            + """
         Insert the host name
        """
        )

        hostname = input(TERMINAL_PROMPT)
        self.get_ip_from_hostname(hostname)

    def get_ip_from_hostname(self, hostname):
        print(f"The IP for {hostname} is {socket.gethostbyname(hostname)}")
        self.complete()

    def complete(self):
        """Shows the complete message and calls back the class"""
        input("\nCompleted, click return to go back.")
