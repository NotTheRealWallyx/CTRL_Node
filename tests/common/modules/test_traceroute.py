import unittest
from unittest.mock import MagicMock, patch

from ctrl_node.common.modules.traceroute import Traceroute


class TestTraceroute(unittest.TestCase):
    @patch("subprocess.run")
    @patch("questionary.text")
    def test_traceroute_system(self, mock_questionary_text, mock_subprocess_run):

        mock_subprocess_run.return_value = MagicMock(stdout="Traceroute output")
        mock_questionary_text.return_value.ask.return_value = None

        traceroute_instance = Traceroute(host="example.com")
        traceroute_instance.traceroute_system()

        mock_subprocess_run.assert_called_once_with(
            ["traceroute", "example.com"], capture_output=True, text=True
        )

        self.assertEqual(mock_subprocess_run.return_value.stdout, "Traceroute output")
