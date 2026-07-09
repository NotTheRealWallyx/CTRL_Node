import socket
import ssl
import time

import questionary

from ctrl_node.common.utils import askforhost


class LatencyCheck:
    """
    Class that measures the latency of connecting to a website, broken
    down by phase: DNS lookup, TCP connect, TLS handshake, time to first
    byte, and content download.
    """

    def __init__(self, host=None, port=443, use_tls=True, path="/"):
        """
        Initializes the class with the host to measure.

        Arguments:
            host {str}: Optional host to check. If not provided, it will default to None.
            port {int}: Port to connect to. Defaults to 443.
            use_tls {bool}: Whether to connect over TLS. Defaults to True.
            path {str}: Path to request. Defaults to "/".
        """
        self.host = host or askforhost()
        self.port = port
        self.use_tls = use_tls
        self.path = path
        self.timings = {}

    def measure_latency(self):
        """
        Connects to the host and records the time taken by each phase of
        the request: DNS lookup, TCP connect, TLS handshake, time to
        first byte, and content download.
        """
        self.timings = {}
        try:
            address_info = self.time_phase(
                "DNS lookup", lambda: socket.getaddrinfo(self.host, self.port)
            )
            ip_address = address_info[0][4][0]

            sock = self.time_phase(
                "TCP connect",
                lambda: socket.create_connection((ip_address, self.port), timeout=10),
            )

            if self.use_tls:
                context = ssl.create_default_context()
                sock = self.time_phase(
                    "TLS handshake",
                    lambda: context.wrap_socket(sock, server_hostname=self.host),
                )

            self.request_content(sock)
            sock.close()
        except (socket.error, ssl.SSLError, socket.timeout) as error:
            print(f"Could not measure latency for {self.host}:{self.port} - {error}")

    def time_phase(self, name: str, action):
        """
        Runs the given action and stores how long it took under the
        given phase name.

        Arguments:
            name {str}: Name of the phase being timed.
            action {Callable}: Zero-argument callable to run and time.

        Returns:
            The return value of the action.
        """
        start = time.perf_counter()
        result = action()
        self.timings[name] = time.perf_counter() - start
        return result

    def request_content(self, sock):
        """
        Sends an HTTP GET request over the given socket and measures the
        time to first byte and the time to download the rest of the
        content.

        Arguments:
            sock {socket.socket}: Connected (and possibly TLS-wrapped) socket.
        """
        request = (
            f"GET {self.path} HTTP/1.1\r\n"
            f"Host: {self.host}\r\n"
            "Connection: close\r\n"
            "\r\n"
        ).encode()

        start = time.perf_counter()
        sock.sendall(request)
        sock.recv(4096)
        self.timings["Time to first byte"] = time.perf_counter() - start

        download_start = time.perf_counter()
        while sock.recv(4096):
            pass
        self.timings["Content download"] = time.perf_counter() - download_start

    def display_results(self):
        """
        Displays the measured timings for each phase along with the
        total time taken.
        """
        if not self.timings:
            print("No latency data available.")
        else:
            print("-" * 60)
            print(f"Latency results for {self.host}")
            print("-" * 60)
            for phase, duration in self.timings.items():
                print(f"{phase}: \t {duration * 1000:.2f} ms")
            print(f"Total: \t {sum(self.timings.values()) * 1000:.2f} ms")

        questionary.text("Press Enter to return to the menu...").ask()
