import unittest
from unittest.mock import MagicMock, patch

from ctrl_node.ctrl_node import CTRL_Node


class TestCTRLNode(unittest.TestCase):
    @patch("ctrl_node.ctrl_node.questionary.select")
    @patch("ctrl_node.ctrl_node.ScanPorts")
    def test_menu_execution(self, mock_scan_ports, mock_questionary_select):
        mock_questionary_select.return_value.ask.return_value = "1 - Scan ports"

        mock_scan_instance = MagicMock()
        mock_scan_ports.return_value = mock_scan_instance

        ctrl_node = CTRL_Node(loop=False)
        with patch("ctrl_node.ctrl_node.clean_console"), patch(
            "ctrl_node.ctrl_node.MAIN_LOGO", new=""
        ):
            ctrl_node.show_menu()

        mock_scan_ports.assert_called_once()
        mock_scan_instance.scan_all_ports.assert_called_once()

    @patch("ctrl_node.ctrl_node.questionary.select")
    def test_menu_exit(self, mock_questionary_select):
        mock_questionary_select.return_value.ask.return_value = "0 - Exit"

        with patch("sys.exit") as mock_exit, patch(
            "ctrl_node.ctrl_node.clean_console"
        ), patch("ctrl_node.ctrl_node.MAIN_LOGO", new=""):
            ctrl_node = CTRL_Node(loop=False)
            ctrl_node.show_menu()

        mock_exit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
