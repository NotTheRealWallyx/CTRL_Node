import questionary
import whois


class Whois:
    def __init__(self):
        """
        Initializes the class for the Whois.
        """

        domain_info = whois.whois("example.com")
        print(domain_info)

        questionary.text("Press Enter to return to the menu...").ask()
