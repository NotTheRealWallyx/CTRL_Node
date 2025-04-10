"""Variables that contain the logo ASCII art"""

import pyfiglet


def get_logo(text):
    return pyfiglet.figlet_format(text)


MAIN_LOGO = get_logo("CTRL_Node")
