"""Variables that contain the logo ASCII art"""

import pyfiglet


def get_logo(text):
    return pyfiglet.figlet_format(text)


SERVER_TOOLS_LOGO = get_logo("CTRL_Node")
SCAN_PORTS_LOGO = get_logo("Scan Ports")
DNS_LOGO = get_logo("DNS")
HOST_TO_IP_LOGO = get_logo("Host to IP")
