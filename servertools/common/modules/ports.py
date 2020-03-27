""" Functions that have to do with port scanning """
import socket
import sys
from datetime import datetime

from servertools.common.misc_functions import askforhost, clean_console
from servertools.variables.globals import COMMON_PORTS, TERMINAL_PROMPT
from servertools.variables.logos import SCAN_PORTS_LOGO


class ScanPorts:
    def __init__(self: ScanPorts):
        """
            Clears the console and shows the menu to ask the user
            to select an option.
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

    def execute_menu(self: ScanPorts, option: int):
        """
            Executes the menu of the class.

            Arguments:
                option {int}: User selected option
        """
        back_menu = False
        wrong_option = False
        if option == "1":
            self.scan_ports(False)
        elif option == "2":
            self.scan_ports()
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

    def completed(self: ScanPorts):
        """ Shows the complete message and calls back the class """
        input("\nCompleted, click return to go back.")
        self.__init__()

    def try_again(self: ScanPorts):
        """ Shows the error message and calls back the class """
        input("That option does not exit, click return to go back.")
        self.__init__()

    def scan_ports(self: ScanPorts, common: bool = True):
        """
            Calls for the scan ports function, it will call for only
            the common ones or first 1024 ports depending on the parameter.
            
            Arguments:
                common {bool}: Scan common ports only, True by default
        """
        remote_server = askforhost()
        remote_server_address = socket.gethostbyname(remote_server)

        print("-" * 60)
        print(f"Scanning remote host {remote_server_address}")
        print("Please wait, this may take a while")
        print("You can cancel anytime pressing Ctrl+C")
        print("-" * 60)

        start_time = datetime.now()

        try:
            if common:
                self.common_port_scan(remote_server_address)
            else:
                self.scan_all_ports(remote_server_address)

        except KeyboardInterrupt:
            print("You pressed Ctrl+C")
            sys.exit()

        except socket.gaierror:
            print("Hostname could not be resolved. Exiting")
            sys.exit()

        except socket.error:
            print("Couldn't connect to server")
            sys.exit()

        end_time = datetime.now()

        total = end_time - start_time

        print("Scanning Completed in: ", total)

    def scan_all_ports(self: ScanPorts, host):
        """
            This will scan only the first 1024, from 1 to 1024 and will print just the
            open ones. Using the socket module.

            Arguments:
                host {str}: The IP of the server to check with socket
        """
        for port in range(1, 1025):
            self.check_port_and_call_for_result(host, port, True)

    def common_port_scan(self: ScanPorts, host):
        """
            Scans the common ports of one host, using the socket module.

            Arguments:
                host {str}: The IP of the server to check with socket
        """

        for port in COMMON_PORTS:
            self.check_port_and_call_for_result(host, port)

    def check_port_and_call_for_result(self, host, port, silence = False):
        """
            Checks the given port and calls for the print result function.
            
            Arguments:
                host {str}: Host to scan
                port {int}: The scanned port
                silence {bool}: The flag to make close ports not to show

        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.settimeout(None)
        self.show_port_open_or_close(result, port, silence)
        sys.stdout.flush()
        sock.close()

    def show_port_open_or_close(self: ScanPorts, result: int, port: int, silence: bool = False):
        """
            Depending on the response parsed to the function prints if the
            port is open or closed, the closed ones can be silenced with the
            True flag.

            Arguments:
                result {int}: The result of the socket function
                port {int}: The scanned port
                silence {bool}: The flag to make close ports not to show
        """
        if result == 0:
            print(f"Port {port}: 	 Open")
        else:
            if not silence:
                print(f"Port {port}: 	 Close")

