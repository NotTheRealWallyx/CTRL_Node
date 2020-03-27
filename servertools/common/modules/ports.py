""" Functions that have to do with port scanning """
import socket
import sys
from datetime import datetime

from servertools.common.misc_functions import askforhost, clean_console
from servertools.variables.globals import TERMINAL_PROMPT
from servertools.variables.logos import SCAN_PORTS_LOGO


class ScanPorts:
    def __init__(self):
        """
        Clears the console and shows the menu to ask the user
        to select an option
        """
        clean_console()
        print(
            SCAN_PORTS_LOGO
            + """
         1 - All ports
         2 - Common ports
         0 - Main meu
        """
        )

        user_option = input(TERMINAL_PROMPT)
        self.execute_menu(user_option)

    def execute_menu(self, option: int):
        """
        Executes the menu of the class

        Arguments:
            option {int}: User selected option
        """
        back_menu = False
        wrong_option = False
        if option == "1":
            self.scan_all_ports()
        elif option == "2":
            self.common_port_scan()
        elif option == "0":
            back_menu = True
        else:
            wrong_option = True

        if wrong_option:
            self.try_again()
        elif back_menu:
            pass
        else:
            self.completed()

    def completed(self):
        """ Shows the complete message and calls back the class """
        input("\nCompleted, click return to go back.")
        self.__init__()

    def try_again(self):
        """ Shows the error message and calls back the class """
        input("That option does not exit, click return to go back.")
        self.__init__()

    def scan_all_ports(self):
        """ Scans all known ports of one host """
        remote_server = askforhost()
        remote_server_address = socket.gethostbyname(remote_server)

        # Print a nice banner with information on which host we are about to scan
        print("-" * 60)
        print("Please wait, scanning remote host", remote_server_address)
        print("-" * 60)

        # Check what time the scan started
        start_time = datetime.now()

        # Using the range function to specify ports (here it will scans all ports between 1 and 1024)
        # We also put in some error handling for catching errors
        try:
            for port in range(1, 1025):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((remote_server_address, port))
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
        end_time = datetime.now()

        # Calculates the difference of time, to see how long it took to run the script
        total = end_time - start_time

        # Printing the information to screen
        print("Scanning Completed in: ", total)

    def common_port_scan(self):
        """ Scans the common ports of one host """
        ports = [
            20,
            21,
            22,
            23,
            25,
            53,
            80,
            110,
            143,
            161,
            162,
            443,
            636,
            989,
            990,
            3306,
        ]

        remote_server = askforhost()
        remote_server_address = socket.gethostbyname(remote_server)

        # Print a nice banner with information on which host we are about to scan
        print("-" * 60)
        print("Please wait, scanning remote host", remote_server_address)
        print("-" * 60)

        # Check what time the scan started
        start_time = datetime.now()

        # Using the range function to specify ports (here it will scans all ports between 1 and 1024)
        # We also put in some error handling for catching errors

        try:
            for port in ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((remote_server_address, port))
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
        end_time = datetime.now()

        # Calculates the difference of time, to see how long it took to run the script
        total = end_time - start_time

        # Printing the information to screen
        print("Scanning Completed in: ", total)
