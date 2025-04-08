"""Class that manages dns lookup"""

from dns.resolver import NoAnswer, query

from ctrl_node.common.utils import askforhost, clean_console
from ctrl_node.variables.globals import TERMINAL_PROMPT
from ctrl_node.variables.logos import DNS_LOGO


class DnsScan:
    def __init__(self):
        """
        Clears the console and shows the menu to ask the user
        to select an option.
        """
        clean_console()
        print(
            DNS_LOGO
            + """
         1 - Scan host
         0 - Main meu
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
        back_menu = False
        wrong_option = False
        if option == "1":
            self.host_to_scan = askforhost()
            self.dns_scan()
        elif option == "0":
            back_menu = True
        else:
            wrong_option = True

        if wrong_option:
            self.try_again()
        elif back_menu:
            pass
        else:
            self.completed()

    def completed(self):
        """Shows the complete message and calls back the class"""
        input("\nCompleted, click return to go back.")
        self.__init__()

    def try_again(self):
        """Shows the error message and calls back the class"""
        input("That option does not exit, click return to go back.")
        self.__init__()

    def dns_scan(self):
        """Makes a DNS scan of the given host"""

        print("-" * 60)
        print("DNS results for the domain: ", self.host_to_scan)
        print("-" * 60)

        mx_results = query(self.host_to_scan, "MX")
        print("")
        print("MX Results: ")
        for mx_result in mx_results:
            print(
                "     Host: ",
                mx_result.exchange,
                " has preference ",
                mx_result.preference,
            )

        # Show different records
        self.create_query_and_show_results("NS")
        self.create_query_and_show_results("A")
        self.create_query_and_show_results("AAAA")
        self.create_query_and_show_results("SOA")
        self.create_query_and_show_results("TXT")

    def create_query_and_show_results(self, record: str):
        """
        Creates the query for the given DNS record, and shows
        and shows the information.

        Arguments:
            record {str}: Record to create the query
        """
        try:
            results = query(self.host_to_scan, record)
            print(f"\n{record} Results: ")
            for result in results:
                print("     ", result)
        except NoAnswer:
            print("     None")
