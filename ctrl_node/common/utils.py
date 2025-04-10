from subprocess import run
import questionary


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
    remote_server = questionary.text("Enter host name:").ask()
    return remote_server
