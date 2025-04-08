from ctrl_node.common.utils import askforhost


def get_host():
    """Asks the user for a host to scan"""
    return askforhost()


def show_port_open_or_close(result: int, port: int, silence: bool = False):
    """
    Depending on the response parsed to the function prints if the
    port is open or closed, the closed ones can be silenced with the
    True flag.

    Arguments:
        result {int}: The result of the socket function
        port {int}: The scanned port
        silence {bool}: The flag to make close ports not to show
    """
    if result == 0:
        print(f"Port {port}: 	 Open")
    else:
        if not silence:
            print(f"Port {port}: 	 Close")
