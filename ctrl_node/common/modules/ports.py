"""Functions that have to do with port scanning"""

import socket

from ctrl_node.common.utils import (
    askforhost,
)
from ctrl_node.variables.globals import COMMON_PORTS
from ctrl_node.common.modules.module_utils import show_port_open_or_close


class ScanPorts:
    """Class to scan ports of a remote server"""

    def __init__(self, host=None):
        """
        Initializes the class with the host to scan.

        Arguments:
            host {str}: Optional host to scan. If not provided, it will default to None.
        """
        self.host = host or askforhost()
        self.remote_server_ip = socket.gethostbyname(self.host)

    def scan_all_ports(self):
        """Scans all ports of the remote server"""
        print(f"Scanning all ports on {self.host} ({self.remote_server_ip})")
        for port in range(1, 1025):
            self.check_port(port)

    def common_port_scan(self):
        """Scans common ports of the remote server"""
        print(f"Scanning common ports on {self.host} ({self.remote_server_ip})")
        for port in COMMON_PORTS:
            self.check_port(port)

    def check_port(self, port):
        """
        Checks if a port is open or closed.

        Arguments:
            port {int}: Port to check
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((self.remote_server_ip, port))
            show_port_open_or_close(result, port)
