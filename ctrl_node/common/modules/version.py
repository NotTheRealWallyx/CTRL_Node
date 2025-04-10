from importlib.metadata import version as get_version

import questionary


class Version:
    def __init__(self):
        """
        Initializes the Version class and retrieves the application version.
        """
        self.application_version = get_version("ctrl-node")

    def display_version(self):
        """
        Displays the version of the application.
        """
        print(f"You are running version {self.application_version}")
        questionary.text("Press Enter to return to the menu...").ask()
