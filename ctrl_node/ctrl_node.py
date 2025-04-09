"""Main file for the application"""

import sys

from ctrl_node.common.utils import clean_console, version
from ctrl_node.common.modules.dns import DnsScan
from ctrl_node.common.modules.host_to_ip import HostToIp
from ctrl_node.common.modules.ports import ScanPorts
from ctrl_node.variables.globals import TERMINAL_PROMPT
from ctrl_node.variables.logos import SERVER_TOOLS_LOGO
from ctrl_node.common.utils import display_scan_ports_header, display_host_to_ip_header


class CTRL_Node:
    """Main class for the application"""

    def __init__(self):
        """
        Clears the console and shows the menu to ask the user
        to select an option.
        """
        clean_console()
        print(
            SERVER_TOOLS_LOGO
            + """
         1 - Scan ports
         2 - DNS look up
         3 - Host to IP
         4 - Show application version
         0 - Exit
        """
        )

        user_option = input(TERMINAL_PROMPT)
        self.execute_menu(user_option)

    def execute_menu(self, option: int):
        """
        Executes the menu of the class.

        Arguments:
            option {int}: User selected option
        """
        wrong_option = False
        if option == "1":
            run_port_scan()
        elif option == "2":
            DnsScan()
        elif option == "3":
            run_host_to_ip()
        elif option == "4":
            run_version()
        elif option == "0":
            sys.exit()
        else:
            wrong_option = True

        if wrong_option:
            self.try_again()
        else:
            self.completed()

    def completed(self):
        """Shows the complete message and calls back the class"""
        input("Completed, press enter to go back.")
        self.__init__()

    def try_again(self):
        """Shows the error message and calls back the class"""
        input("That option does not exit, press enter to go back.")
        self.__init__()


def run_port_scan():
    """Run the port scan"""
    clean_console()
    display_scan_ports_header()
    scan = ScanPorts()
    scan.scan_all_ports()


def run_host_to_ip():
    """Run the port scan"""
    clean_console()
    display_host_to_ip_header()
    hostToIp = HostToIp()
    hostToIp.get_ip_from_hostname()


def run_version():
    """Run the port scan"""
    clean_console()
    version()


def main():
    CTRL_Node()
