import subprocess

def clean_console():
    comand = ["clear"]
    subprocess.check_output(comand)
    subprocess.call(comand, shell=False)