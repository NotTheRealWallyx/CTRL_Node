""" File common used functions """
from subprocess import run
import pkg_resources

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
    application_version = pkg_resources.require("servertools")[0].version
    print(f"You are running version {application_version} ")