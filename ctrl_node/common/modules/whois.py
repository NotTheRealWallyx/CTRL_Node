import questionary
import whois

from ctrl_node.common.utils import askforhost


class Whois:

    def __init__(self, host=None):
        """
        Initializes the Whois class.
        """
        self.domain_info = None
        self.host = host or askforhost()

    def fetch_domain_info(self):
        """
        Fetches the Whois information for the given domain.

        Args:
            domain {str}: The domain name to query.
        """
        self.domain_info = whois.whois(self.host)

    def display_domain_info(self):
        """
        Displays the fetched Whois information.
        """
        if self.domain_info:
            print(self.domain_info)
        else:
            print("No domain info available.")

        questionary.text("Press Enter to return to the menu...").ask()
