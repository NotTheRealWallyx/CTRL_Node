import subprocess
import unittest
from unittest.mock import MagicMock, patch

from ctrl_node.common.modules.traceroute import Traceroute


class TestTraceroute(unittest.TestCase):
    @patch("subprocess.Popen")
    @patch("questionary.text")
    def test_traceroute_system(self, mock_questionary_text, mock_popen):
        # Mock the Popen object and its behavior
        mock_process = MagicMock()
        mock_process.stdout = ["line 1\n", "line 2\n", "line 3\n"]
        mock_process.wait.return_value = None
        mock_popen.return_value = mock_process

        # Mock questionary.text(...).ask() to prevent user input
        mock_questionary_text.return_value.ask.return_value = None

        # Create an instance of Traceroute with a predefined host
        traceroute_instance = Traceroute(host="example.com")
        traceroute_instance.traceroute_system()

        # Validate that Popen was called with the correct arguments
        mock_popen.assert_called_once_with(
            ["traceroute", "example.com"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # Validate that the output lines were printed
        expected_output = "line 1\nline 2\nline 3\n"
        printed_output = "".join(mock_process.stdout)
        self.assertEqual(printed_output, expected_output)
