import subprocess


def clean_console():
    # comand = ["clear"]
    subprocess.run(["clear"], shell=False)
    #subprocess.call(comand, shell=False)
