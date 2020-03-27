""" main file for the application """
import sys

from servertools.common.misc_functions import clean_console, version
from servertools.common.modules.dns import DnsScan
from servertools.common.modules.ports import ScanPorts
from servertools.variables.globals import TERMINAL_PROMPT
from servertools.variables.logos import SERVER_TOOLS_LOGO


class ServerTools:
    """ Main class for the application """

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
         3 - Show application version
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
            ScanPorts()
        elif option == "2":
            DnsScan()
        elif option == "3":
            version()
        elif option == "0":
            sys.exit()
        else:
            wrong_option = True

        if wrong_option:
            self.try_again()
        else:
            self.completed()

    def completed(self):
        """ Shows the complete message and calls back the class """
        input("Completed, click return to go back.")
        self.__init__()

    def try_again(self):
        """ Shows the error message and calls back the class """
        input("That option does not exit, click return to go back.")
        self.__init__()


if __name__ == "__main__":
    ServerTools()
