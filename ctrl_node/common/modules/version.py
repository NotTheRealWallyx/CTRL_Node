import questionary

from importlib.metadata import version as get_version


class Version:
    def __init__(self):
        """
        Initializes the class for the version.
        """
        application_version = get_version("ctrl-node")
        print(f"You are running version {application_version}")
        questionary.text("Press Enter to return to the menu...").ask()
