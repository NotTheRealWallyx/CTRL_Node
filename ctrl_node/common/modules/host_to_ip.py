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
        """
        Retrieves the IP address from the hostname.
        """
        print(f"The IP for {self.host} is {socket.gethostbyname(self.host)}")
        questionary.text("Press Enter to return to the menu...").ask()

    def validate_hostname(self):
        """
        Validates the hostname by attempting to resolve it.

        Returns:
            bool: True if the hostname is valid, False otherwise.
        """
        try:
            socket.gethostbyname(self.host)
            return True
        except socket.error:
            return False
