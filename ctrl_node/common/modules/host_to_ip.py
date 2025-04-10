"""Class that manages dns lookup"""

import socket

import questionary

from ctrl_node.common.utils import askforhost


class HostToIp:
    def __init__(self, host=None):
        """
        Initializes the class with the host to retrieve the IP.
        """
        self.host = host or askforhost()

    def get_ip_from_hostname(self):
        print(f"The IP for {self.host} is {socket.gethostbyname(self.host)}")
        questionary.text("Press Enter to return to the menu...").ask()
