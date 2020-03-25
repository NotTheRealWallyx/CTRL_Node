import getopt
import socket
import sys
from datetime import datetime

import pkg_resources
from dns.resolver import NoAnswer, query

from servertools.misc_functions import clean_console


def askforhost():
    # Clear the screen
    clean_console()

    # Ask for input
    remoteServer = input("Enter a remote host to scan: ")

    return remoteServer


def scan_all_ports():
    remoteServer = askforhost()
    remoteServerIP = socket.gethostbyname(remoteServer)

    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-" * 60)

    # Check what time the scan started
    t1 = datetime.now()

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)

    # We also put in some error handling for catching errors

    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((remoteServerIP, port))
            sock.settimeout(None)
            if result == 0:
                print("Port {}: 	 Open".format(port))
                sys.stdout.flush()
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    print("Scanning Completed in: ", total)


def common_port_scan():
    ports = [20, 21, 22, 23, 25, 53, 80, 110, 143, 161, 162, 443, 636, 989, 990, 3306]

    remoteServer = askforhost()
    remoteServerIP = socket.gethostbyname(remoteServer)

    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-" * 60)

    # Check what time the scan started
    t1 = datetime.now()

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)

    # We also put in some error handling for catching errors

    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((remoteServerIP, port))
            sock.settimeout(None)
            if result == 0:
                print("Port {}: 	 Open".format(port))
            else:
                print("Port {}: 	 Close".format(port))

            sys.stdout.flush()
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    print("Scanning Completed in: ", total)


def dns_scan(remoteServer=""):
    print(remoteServer)
    if remoteServer is "":
        remoteServer = askforhost()

    print("-" * 60)
    print("DNS results for the domain: ", remoteServer)
    print("-" * 60)

    mx_results = query(remoteServer, "MX")
    print("")
    print("MX Results: ")
    for mx_result in mx_results:
        print("     Host: ", mx_result.exchange, " has preference ", mx_result.preference)

    ns_results = query(remoteServer, "NS")
    print("")
    print("NS Results: ")
    for ns_result in ns_results:
        print("     ", ns_result)

    a_results = query(remoteServer, "A")
    print("")
    print("A Results: ")
    for a_result in a_results:
        print("     ", a_result)

    print("")
    print("AAA Results: ")
    try:
        aaa_results = query(remoteServer, "AAAA")
        for aaa_result in aaa_results:
            print("	 ", aaa_result)
    except NoAnswer:
        print("	 None")

    soa_results = query(remoteServer, "SOA")
    print("")
    print("SOA Results: ")
    for soa_result in soa_results:
        print("     ", soa_result)

    print("")
    print("TXT Results: ")
    try:
        txt_results = query(remoteServer, "TXT")
        for txt_result in txt_results:
            print("	 ", txt_result)
    except NoAnswer:
        print("	 None")


def help_commands():
    print("Server Tools: ")
    print(" ")
    print("Options: ")
    print("  -h  --help       Show this screen.")
    print("  -v  --version    Show version.")
    print("  -a  --all        Scan all ports (Takes a while).")
    print("  -c  --common     Only scans the most common ports.")
    print("  -d  --dns        DNS scan of the domain.")


def version():
    version = pkg_resources.require("servertools")[0].version
    print(f"You are running version {version} ")


def main(argv):
    helpCommandsShow = False
    try:
        opts, args = getopt.getopt(
            argv, "hi:vi:ai:ci:di:", ["version", "help", "all", "common", "dns"]
        )
    except getopt.GetoptError:
        helpCommandsShow = True
        sys.exit(2)

    if not opts:
        helpCommandsShow = True

    for opt, args in opts:
        if opt in ("-h", "--help"):
            help_commands()
            sys.exit()
        elif opt in ("-v", "--version"):
            version()
        elif opt in ("-a", "--all"):
            scan_all_ports()
        elif opt in ("-c", "--common"):
            common_port_scan()
        elif opt in ("-d", "--dns"):
            dns_scan(args)
        else:
            helpCommandsShow = True

    if helpCommandsShow is True:
        help_commands()


if __name__ == "__main__":
    main(sys.argv[1:])
