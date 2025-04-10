import questionary
from dns.resolver import NoAnswer, query

from ctrl_node.common.utils import askforhost


class DnsScan:
    def __init__(self):
        """
        Initializes the DnsScan class and sets up the host variable.
        """
        self.host = None

    def scan_host(self):
        """
        Prompts the user for a host and performs a DNS scan.
        """
        self.host = askforhost()
        if self.host:
            self.dns_scan()
        else:
            print("No host provided. Returning to the menu.")

    def dns_scan(self):
        """Performs a DNS scan for the given host."""
        print("-" * 60)
        print("DNS results for the domain: ", self.host)
        print("-" * 60)

        try:
            mx_results = query(self.host, "MX")
            print("")
            print("MX Results: ")
            for mx_result in mx_results:
                print(
                    "     Host: ",
                    mx_result.exchange,
                    " has preference ",
                    mx_result.preference,
                )
        except NoAnswer:
            print("No MX records found.")

        # Show different records
        self.create_query_and_show_results("NS")
        self.create_query_and_show_results("A")
        self.create_query_and_show_results("AAAA")
        self.create_query_and_show_results("SOA")
        self.create_query_and_show_results("TXT")

        questionary.text("Press Enter to return to the menu...").ask()

    def create_query_and_show_results(self, record: str):
        """
        Queries and displays DNS records for the given type.

        Arguments:
            record {str}: The DNS record type to query.
        """
        try:
            results = query(self.host, record)
            print(f"\n{record} Results: ")
            for result in results:
                print("     ", result)
        except NoAnswer:
            print(f"No {record} records found.")
