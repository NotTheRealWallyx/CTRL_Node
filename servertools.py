#!/usr/bin/env python
import socket
import subprocess
import sys
import getopt
from datetime import datetime
import dns
import dns.resolver


def askforhost():
    # Clear the screen
    subprocess.call('clear', shell=True)

    # Ask for input
    remoteServer = raw_input("Enter a remote host to scan: ")

    return remoteServer


def scanallports():
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


def commonportsscan():
    ports = [20, 21, 22, 23, 25, 53, 80, 110,
             143, 161, 162, 443, 636, 989, 990, 3306]

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


def dnsscan():
    remoteServer = askforhost()

    print("-" * 60)
    print("DNS results for the domain: ", remoteServer)
    print("-" * 60)

    res = dns.resolver.query(remoteServer, 'MX')
    print("")
    print("MX Results: ")
    for rdata in res:
        print("     Host: ", rdata.exchange,
              " has preference ", rdata.preference)

    resns = dns.resolver.query(remoteServer, 'NS')
    print("")
    print("NS Results: ")
    for rdata in resns:
        print '     ', rdata

    resa = dns.resolver.query(remoteServer, 'A')
    print("")
    print("A Results: ")
    for rdata in resa:
        print '     ', rdata

    print("")
    print("AAA Results: ")
    try:
        resaaaa = dns.resolver.query(remoteServer, 'AAAA')
        for rdata in resaaaa:
            print("     ", rdata)
    except:
        print("     None")

    ressoa = dns.resolver.query(remoteServer, 'SOA')
    print("")
    print("SOA Results: ")
    for rdata in ressoa:
        print('     ', rdata)

    print("")
    print("TXT Results: ")
    try:
        resaaaa = dns.resolver.query(remoteServer, 'TXT')
        for rdata in restxt:
            print("     ", rdata)
    except:
        print("     None")


def helpCommands():
    print("Server Tools: ")
    print(" ")
    print("Options: ")
    print("  -h  --help       Show this screen.")
    print("  -v  --version    Show version.")
    print("  -a  --all        Scan all ports (Takes a while).")
    print("  -c  --common     Only scans the most commond ports.")
    print("  -d  --dns        DNS scan of the domain.")


def version():
    print("You are running version 0.1 ")


def main(argv):
    helpCommandsShow = False
    try:
        opts, args = getopt.getopt(argv, "hi:vi:ai:ci:di:", [
                                   "version", "help", "all", "common", "dns"])
    except getopt.GetoptError:
        helpCommandsShow = True
        sys.exit(2)

    if not opts:
        helpCommandsShow = True

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            helpCommands()
            sys.exit()
        elif opt in ("-v", "--version"):
            version()
        elif opt in ("-a", "--all"):
            scanallports()
        elif opt in ("-c", "--common"):
            commonportsscan()
        elif opt in ("-d", "--dns"):
            dnsscan()
        else:
            helpCommandsShow = True

    if (helpCommandsShow == True):
        helpCommands()


if __name__ == "__main__":
    main(sys.argv[1:])
