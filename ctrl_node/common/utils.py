from ctrl_node.variables.logos import SCAN_PORTS_LOGO
from subprocess import run
from importlib.metadata import version as get_version


def display_scan_ports_header():
    """Displays the SCAN_PORTS_LOGO header"""
    print(SCAN_PORTS_LOGO)


def display_host_to_ip_header():
    """Displays the HOST_TO_IP_LOGO header"""
    print(HOST_TO_IP_LOGO)


def clean_console():
    """Clean the console in a secure way"""
    execute_clear_command()


def execute_clear_command():
    """Executes the clear command"""
    run(["/usr/bin/clear"], shell=False, check=True)


def askforhost() -> str:
    """
    Asks for the host name

    Returns:
        str: input entered by user
    """

    # Ask for input
    remote_server = input("Enter host name: ")

    return remote_server


def version():
    """Shows the version of the application on the terminal"""
    application_version = get_version("ctrl-node")
    print(f"You are running version {application_version} ")
