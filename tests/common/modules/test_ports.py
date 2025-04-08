import unittest
from unittest.mock import patch
from ctrl_node.common.modules.ports import ScanPorts
from ctrl_node.variables.globals import COMMON_PORTS

class TestScanPorts(unittest.TestCase):
    @patch("ctrl_node.common.modules.ports.show_port_open_or_close")
    def test_scan_common_ports(self, mock_show_port):
        scanner = ScanPorts(host="localhost")
        scanner.common_port_scan()

        # Assert that the function was called for each common port
        self.assertEqual(mock_show_port.call_count, len(COMMON_PORTS))

    @patch("ctrl_node.common.modules.ports.show_port_open_or_close")
    def test_scan_all_ports(self, mock_show_port):
        scanner = ScanPorts(host="localhost")
        scanner.scan_all_ports()

        # Assert that the function was called for ports 1 to 1024
        self.assertEqual(mock_show_port.call_count, 1024)

if __name__ == "__main__":
    unittest.main()