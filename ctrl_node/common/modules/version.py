"""Class that manages dns lookup"""

import socket


from ctrl_node.common.utils import get_version


class Version:
    def __init__(self):
        """
        Initializes the class for the version.
        """
        application_version = get_version("ctrl-node")
        print(f"You are running version {application_version} ")
