import unittest
from unittest.mock import patch

from ctrl_node.common.modules.module_utils import rate_ttfb, show_port_open_or_close


class TestUtils(unittest.TestCase):

    @patch("builtins.print")
    def test_show_port_open_or_close_open(self, mock_print):
        show_port_open_or_close(0, 80)
        mock_print.assert_called_once_with("Port 80: \t Open")

    @patch("builtins.print")
    def test_show_port_open_or_close_closed(self, mock_print):
        show_port_open_or_close(1, 80)
        mock_print.assert_called_once_with("Port 80: \t Close")

    def test_rate_ttfb_good(self):
        self.assertEqual(rate_ttfb(0.8), "Good")

    def test_rate_ttfb_needs_improvement(self):
        self.assertEqual(rate_ttfb(1.8), "Needs Improvement")

    def test_rate_ttfb_poor(self):
        self.assertEqual(rate_ttfb(1.9), "Poor")


if __name__ == "__main__":
    unittest.main()
