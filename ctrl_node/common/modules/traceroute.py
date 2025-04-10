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
        Performs a traceroute for the given host.
        """
        process = subprocess.Popen(
            ["traceroute", self.host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        for line in process.stdout:
            print(line, end="")

        process.wait()

        questionary.text("Press Enter to return to the menu...").ask()
