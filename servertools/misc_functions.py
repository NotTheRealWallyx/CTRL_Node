""" File common used functions """
from subprocess import run


def clean_console():
    """ Clean the console in a secure way """
    run(["/usr/bin/clear"], shell=False, check=True)
