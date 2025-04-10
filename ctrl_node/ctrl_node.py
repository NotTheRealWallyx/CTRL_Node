import sys
import questionary

from ctrl_node.common.utils import clean_console
from ctrl_node.common.modules.dns import DnsScan
from ctrl_node.common.modules.host_to_ip import HostToIp
from ctrl_node.common.modules.ports import ScanPorts
from ctrl_node.common.modules.version import Version
from ctrl_node.variables.logos import MAIN_LOGO


class CTRL_Node:
    """Main class for the application"""

    def __init__(self):
        """
        Clears the console and shows the menu to ask the user
        to select an option.
        """
        while True:
            clean_console()
            print(MAIN_LOGO)
            self.show_menu()

    def show_menu(self):
        """
        Displays the menu and handles user selection.
        """
        choice = questionary.select(
            "What would you like to do?",
            choices=[
                "1 - Scan ports",
                "2 - DNS look up",
                "3 - Host to IP",
                "4 - Show application version",
                "0 - Exit",
            ],
        ).ask()

        self.execute_menu(choice)

    def execute_menu(self, option: str):
        """
        Executes the menu of the class.

        Arguments:
            option {str}: User selected option
        """
        if option.startswith("1"):
            scan = ScanPorts()
            scan.scan_all_ports()
        elif option.startswith("2"):
            dns_scan = DnsScan()
            dns_scan.scan_host()
        elif option.startswith("3"):
            host_to_ip = HostToIp()
            host_to_ip.get_ip_from_hostname()
        elif option.startswith("4"):
            Version()
        elif option.startswith("0"):
            sys.exit()


def main():
    CTRL_Node()
