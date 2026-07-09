import socket
import unittest
from unittest.mock import MagicMock, patch

from ctrl_node.common.modules.latency import LatencyCheck


class TestLatencyCheck(unittest.TestCase):
    @patch("ctrl_node.common.modules.latency.askforhost", return_value="example.com")
    def test_initialization(self, mock_askforhost):
        instance = LatencyCheck()
        self.assertEqual(instance.host, "example.com")
        self.assertEqual(instance.port, 443)
        self.assertTrue(instance.use_tls)
        self.assertEqual(instance.path, "/")
        mock_askforhost.assert_called_once()

    @patch("ctrl_node.common.modules.latency.ssl.create_default_context")
    @patch("ctrl_node.common.modules.latency.socket.create_connection")
    @patch("ctrl_node.common.modules.latency.socket.getaddrinfo")
    def test_measure_latency_success(
        self, mock_getaddrinfo, mock_create_connection, mock_context_factory
    ):
        mock_getaddrinfo.return_value = [
            (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("93.184.216.34", 443))
        ]
        mock_create_connection.return_value = MagicMock()

        mock_ssock = MagicMock()
        mock_ssock.recv.side_effect = [b"HTTP/1.1 200 OK", b""]
        mock_context_factory.return_value.wrap_socket.return_value = mock_ssock

        instance = LatencyCheck(host="example.com")
        instance.measure_latency()

        self.assertIn("DNS lookup", instance.timings)
        self.assertIn("TCP connect", instance.timings)
        self.assertIn("TLS handshake", instance.timings)
        self.assertIn("Time to first byte", instance.timings)
        self.assertIn("Content download", instance.timings)
        mock_ssock.sendall.assert_called_once()
        mock_ssock.close.assert_called_once()

    @patch(
        "ctrl_node.common.modules.latency.socket.getaddrinfo",
        side_effect=socket.gaierror("Name resolution failed"),
    )
    @patch("builtins.print")
    def test_measure_latency_dns_error(self, mock_print, mock_getaddrinfo):
        instance = LatencyCheck(host="example.com")
        instance.measure_latency()

        self.assertEqual(instance.timings, {})
        mock_print.assert_called_once_with(
            "Could not measure latency for example.com:443 - Name resolution failed"
        )

    @patch("ctrl_node.common.modules.latency.questionary.text")
    @patch("builtins.print")
    def test_display_results_with_data(self, mock_print, mock_questionary_text):
        mock_questionary_text.return_value.ask.return_value = None
        instance = LatencyCheck(host="example.com")
        instance.timings = {"DNS lookup": 0.01, "TCP connect": 0.02}

        instance.display_results()

        mock_print.assert_any_call("Latency results for example.com")
        mock_questionary_text.assert_called_once_with(
            "Press Enter to return to the menu..."
        )

    @patch("ctrl_node.common.modules.latency.questionary.text")
    @patch("builtins.print")
    def test_display_results_without_data(self, mock_print, mock_questionary_text):
        mock_questionary_text.return_value.ask.return_value = None
        instance = LatencyCheck(host="example.com")

        instance.display_results()

        mock_print.assert_any_call("No latency data available.")


if __name__ == "__main__":
    unittest.main()
