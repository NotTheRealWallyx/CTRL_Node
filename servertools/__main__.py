""" main file for the application """
import sys

import pkg_resources

from servertools.common.misc_functions import clean_console
from servertools.variables.globals import TERMINAL_PROMPT
from servertools.variables.logos import SERVER_TOOLS_LOGO
from servertools.common.modules.ports import scan_ports
from servertools.common.modules.dns import dns_scan

class server_tools:
    """ Main class for the application """
    def __init__(self):
        clean_console()
        print(SERVER_TOOLS_LOGO + """
         1 - Scan ports
         2 - DNS look up
         3 - Show application version
         0 - Exit
        """)
        user_option = input(TERMINAL_PROMPT)
        self.execute_menu(user_option)

    def execute_menu(self, option):
        wrong_option = False
        if option == "1":
            scan_ports()
        elif option == "2":
            dns_scan()
        elif option == "3":
            self.version()
        elif option == "0":
            sys.exit()
        else:
            wrong_option = True
            
        if wrong_option:
            self.try_again()
        else:
            self.completed()

    def version(self):
        """ Shows the version of the application on the terminal """
        application_version = pkg_resources.require("servertools")[0].version
        print(f"You are running version {application_version} ")

    def completed(self):
        input("Completed, click return to go back.")
        self.__init__()

    def try_again(self):
        input("That option does not exit, click return to go back.")
        self.__init__()

if __name__ == "__main__":
    server_tools()
