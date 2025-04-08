import unittest
from unittest.mock import patch, MagicMock
from ctrl_node.common.utils import display_scan_ports_header, askforhost, version, clean_console, execute_clear_command
from ctrl_node.variables.logos import SCAN_PORTS_LOGO

class TestUtils(unittest.TestCase):
    @patch("builtins.print")
    def test_display_scan_ports_header(self, mock_print):
        display_scan_ports_header()
        mock_print.assert_called_with(SCAN_PORTS_LOGO)

    @patch("ctrl_node.common.utils.execute_clear_command")
    def test_clean_console(self, mock_execute_clear_command):
        clean_console()
        mock_execute_clear_command.assert_called_once()

    @patch("builtins.input", return_value="localhost")
    def test_askforhost(self, mock_input):
        result = askforhost()
        self.assertEqual(result, "localhost")
        mock_input.assert_called_once_with("Enter a remote host to scan: ")

    @patch("ctrl_node.common.utils.get_version", return_value="1.0.0")
    @patch("builtins.print")
    def test_version(self, mock_print, mock_get_version):
        version()
        mock_get_version.assert_called_once_with("ctrl-node")
        mock_print.assert_called_with("You are running version 1.0.0 ")

if __name__ == "__main__":
    unittest.main()