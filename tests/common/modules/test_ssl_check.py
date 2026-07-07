import unittest
from unittest.mock import MagicMock, patch

from ctrl_node.common.modules.ssl_check import SslCheck


class TestSslCheck(unittest.TestCase):
    @patch("ctrl_node.common.modules.ssl_check.askforhost", return_value="example.com")
    def test_initialization(self, mock_askforhost):
        instance = SslCheck()
        self.assertEqual(instance.host, "example.com")
        self.assertEqual(instance.port, 443)
        mock_askforhost.assert_called_once()

    @patch("ctrl_node.common.modules.ssl_check.socket.create_connection")
    @patch("ctrl_node.common.modules.ssl_check.ssl.create_default_context")
    def test_fetch_certificate_success(
        self, mock_context_factory, mock_create_connection
    ):
        mock_ssock = MagicMock()
        mock_ssock.getpeercert.return_value = {
            "subject": [[("commonName", "example.com")]]
        }
        mock_context_factory.return_value.wrap_socket.return_value.__enter__.return_value = (
            mock_ssock
        )
        mock_create_connection.return_value.__enter__.return_value = MagicMock()

        instance = SslCheck(host="example.com")
        instance.fetch_certificate()

        self.assertEqual(
            instance.certificate, {"subject": [[("commonName", "example.com")]]}
        )

    @patch(
        "ctrl_node.common.modules.ssl_check.socket.create_connection",
        side_effect=OSError("Connection refused"),
    )
    @patch("builtins.print")
    def test_fetch_certificate_connection_error(
        self, mock_print, mock_create_connection
    ):
        instance = SslCheck(host="example.com")
        instance.fetch_certificate()

        self.assertIsNone(instance.certificate)
        mock_print.assert_called_once_with(
            "Could not fetch certificate for example.com:443 - Connection refused"
        )

    @patch("ctrl_node.common.modules.ssl_check.questionary.text")
    @patch("builtins.print")
    def test_display_certificate_info_with_data(
        self, mock_print, mock_questionary_text
    ):
        mock_questionary_text.return_value.ask.return_value = None
        instance = SslCheck(host="example.com")
        instance.certificate = {
            "subject": [[("commonName", "example.com")]],
            "issuer": [[("commonName", "Example CA")]],
            "notAfter": "Jan  1 00:00:00 2030 GMT",
        }

        instance.display_certificate_info()

        mock_print.assert_any_call("Subject: example.com")
        mock_print.assert_any_call("Issuer: Example CA")
        mock_questionary_text.assert_called_once_with(
            "Press Enter to return to the menu..."
        )

    @patch("ctrl_node.common.modules.ssl_check.questionary.text")
    @patch("builtins.print")
    def test_display_certificate_info_without_data(
        self, mock_print, mock_questionary_text
    ):
        mock_questionary_text.return_value.ask.return_value = None
        instance = SslCheck(host="example.com")

        instance.display_certificate_info()

        mock_print.assert_any_call("No certificate info available.")


if __name__ == "__main__":
    unittest.main()
