import socket
import ssl
from datetime import datetime

import questionary

from ctrl_node.common.utils import askforhost


class SslCheck:
    """
    Class that checks the SSL/TLS certificate of a remote server.
    """

    def __init__(self, host=None, port=443):
        """
        Initializes the class with the host and port to check.

        Arguments:
            host {str}: Optional host to check. If not provided, it will default to None.
            port {int}: Port to connect to. Defaults to 443.
        """
        self.host = host or askforhost()
        self.port = port
        self.certificate = None

    def fetch_certificate(self):
        """
        Connects to the host and fetches its SSL/TLS certificate.
        """
        try:
            context = ssl.create_default_context()
            with socket.create_connection((self.host, self.port), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=self.host) as ssock:
                    self.certificate = ssock.getpeercert()
        except (socket.error, ssl.SSLError) as error:
            print(f"Could not fetch certificate for {self.host}:{self.port} - {error}")

    def display_certificate_info(self):
        """
        Displays the fetched certificate information, including subject,
        issuer, and expiry date.
        """
        if not self.certificate:
            print("No certificate info available.")
        else:
            subject = dict(x[0] for x in self.certificate.get("subject", []))
            issuer = dict(x[0] for x in self.certificate.get("issuer", []))
            not_after = self.certificate.get("notAfter")

            print(f"Subject: {subject.get('commonName', 'Unknown')}")
            print(f"Issuer: {issuer.get('commonName', 'Unknown')}")
            print(f"Valid until: {not_after}")

            if not_after:
                expiry = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
                days_left = (expiry - datetime.utcnow()).days
                print(f"Days until expiry: {days_left}")

        questionary.text("Press Enter to return to the menu...").ask()
