import subprocess

def clean_console():
    comand = ["clear"]
    subprocess.call(comand, shell=False)