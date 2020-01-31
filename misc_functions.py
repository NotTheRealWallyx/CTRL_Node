import subprocess


def clean_console():
    comand = ["clear"]
    subprocess.run(comand, shell=False)
    #subprocess.call(comand, shell=False)
