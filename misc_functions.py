from subprocess import run


def clean_console():
    run(["/usr/bin/clear"], shell=False)
