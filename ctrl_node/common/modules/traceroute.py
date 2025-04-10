import subprocess

import questionary

from ctrl_node.common.utils import askforhost


class Traceroute:

    def __init__(self, host=None):
        """
        Initializes the Traceroute class.
        """
        self.domain_info = None
        self.host = host or askforhost()

    def traceroute_system(self):
        """
        Performs a traceroute to the given host using the system's traceroute command.
        """

        result = subprocess.run(
            ["traceroute", self.host], capture_output=True, text=True
        )

        print(result.stdout)

        questionary.text("Press Enter to return to the menu...").ask()
