import unittest
from unittest.mock import patch, MagicMock
import socket
from ctrl_node.common.modules.ports import ScanPorts

class TestScanPorts(unittest.TestCase):
    @patch("ctrl_node.common.modules.ports.askforhost", return_value="localhost")
    @patch("socket.gethostbyname", return_value="127.0.0.1")
    @patch("ctrl_node.common.modules.ports.show_port_open_or_close")
    def test_scan_common_ports(self, mock_show_port, mock_gethostbyname, mock_askforhost):
        scanner = ScanPorts()
        scanner.common_port_scan("127.0.0.1")

        # Assert that the function was called for each common port
        self.assertEqual(mock_show_port.call_count, len(scanner.COMMON_PORTS))

    @patch("ctrl_node.common.modules.ports.askforhost", return_value="localhost")
    @patch("socket.gethostbyname", return_value="127.0.0.1")
    @patch("ctrl_node.common.modules.ports.show_port_open_or_close")
    def test_scan_all_ports(self, mock_show_port, mock_gethostbyname, mock_askforhost):
        scanner = ScanPorts()
        scanner.scan_all_ports("127.0.0.1")

        # Assert that the function was called for ports 1 to 1024
        self.assertEqual(mock_show_port.call_count, 1024)

if __name__ == "__main__":
    unittest.main()