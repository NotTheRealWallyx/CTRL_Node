import unittest
from unittest.mock import patch, MagicMock
from ctrl_node.common.utils import (
    display_scan_ports_header,
    display_host_to_ip_header,
    askforhost,
    clean_console,
    execute_clear_command,
)
from ctrl_node.variables.logos import SCAN_PORTS_LOGO, HOST_TO_IP_LOGO


class TestUtils(unittest.TestCase):
    @patch("builtins.print")
    def test_display_scan_ports_header(self, mock_print):
        display_scan_ports_header()
        mock_print.assert_called_with(SCAN_PORTS_LOGO)

    @patch("builtins.print")
    def test_display_host_to_ip_header(self, mock_print):
        display_host_to_ip_header()
        mock_print.assert_called_with(HOST_TO_IP_LOGO)

    @patch("ctrl_node.common.utils.execute_clear_command")
    def test_clean_console(self, mock_execute_clear_command):
        clean_console()
        mock_execute_clear_command.assert_called_once()

    @patch("questionary.text")
    def test_askforhost(self, mock_questionary_text):
        mock_questionary_text.return_value.ask.return_value = "localhost"
        result = askforhost()
        self.assertEqual(result, "localhost")
        mock_questionary_text.return_value.ask.assert_called_once()


if __name__ == "__main__":
    unittest.main()
