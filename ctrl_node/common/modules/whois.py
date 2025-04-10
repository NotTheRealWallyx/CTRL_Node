import questionary
import whois


class Whois:
    def __init__(self):
        """
        Initializes the Whois class.
        """
        self.domain_info = None

    def fetch_domain_info(self, domain):
        """
        Fetches the Whois information for the given domain.

        Args:
            domain {str}: The domain name to query.
        """
        self.domain_info = whois.whois(domain)

    def display_domain_info(self):
        """
        Displays the fetched Whois information.
        """
        if self.domain_info:
            print(self.domain_info)
        else:
            print("No domain info available.")

        questionary.text("Press Enter to return to the menu...").ask()
