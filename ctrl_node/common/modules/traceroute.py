import shutil
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
        traceroute_path = shutil.which("traceroute")
        if not traceroute_path:
            raise FileNotFoundError(
                "The 'traceroute' command is not found in the system PATH."
            )

        process = subprocess.Popen(
            [traceroute_path, self.host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        for line in process.stdout:
            print(line, end="")

        process.wait()
        if process.returncode != 0:
            error_message = process.stderr.read()
            print(f"Error: Traceroute command failed with exit code {process.returncode}.")
            print(f"Details: {error_message}")
            return

        questionary.text("Press Enter to return to the menu...").ask()
