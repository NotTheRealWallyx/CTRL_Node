""" File common used functions """
from subprocess import run
from importlib.metadata import version as get_version


def clean_console():
    """ Clean the console in a secure way """
    run(["/usr/bin/clear"], shell=False, check=True)


def askforhost() -> str:
    """
    Asks for the host name

    Returns:
        str: input entered by user
    """
    clean_console()

    # Ask for input
    remote_server = input("Enter a remote host to scan: ")

    return remote_server


def version():
    """ Shows the version of the application on the terminal """
    application_version = get_version("ctrl-node")
    print(f"You are running version {application_version} ")


def show_port_open_or_close(self, result: int, port: int, silence: bool = False):
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
