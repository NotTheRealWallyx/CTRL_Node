import unittest
from unittest.mock import patch
from ctrl_node.common.modules.module_utils import show_port_open_or_close


class TestUtils(unittest.TestCase):

    @patch("builtins.print")
    def test_show_port_open_or_close_open(self, mock_print):
        show_port_open_or_close(0, 80)
        mock_print.assert_called_once_with("Port 80: \t Open")

    @patch("builtins.print")
    def test_show_port_open_or_close_closed(self, mock_print):
        show_port_open_or_close(1, 80)
        mock_print.assert_called_once_with("Port 80: \t Close")


if __name__ == "__main__":
    unittest.main()
