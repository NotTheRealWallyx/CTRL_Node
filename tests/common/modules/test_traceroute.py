import io
import subprocess
import unittest
from unittest.mock import MagicMock, patch

from ctrl_node.common.modules.traceroute import Traceroute


class TestTraceroute(unittest.TestCase):
    @patch("shutil.which")
    @patch("subprocess.Popen")
    @patch("questionary.text")
    def test_traceroute_system(self, mock_questionary_text, mock_popen, mock_which):
        mock_which.return_value = "/usr/sbin/traceroute"

        mock_process = MagicMock()
        mock_process.stdout = io.StringIO("line 1\nline 2\nline 3\n")
        mock_process.wait.return_value = None
        mock_popen.return_value = mock_process

        mock_questionary_text.return_value.ask.return_value = None

        traceroute_instance = Traceroute(host="example.com")
        traceroute_instance.traceroute_system()

        mock_popen.assert_called_once_with(
            ["/usr/sbin/traceroute", "example.com"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        expected_output = "line 1\nline 2\nline 3\n"
        printed_output = mock_process.stdout.getvalue()
        self.assertEqual(printed_output, expected_output)

    @patch("shutil.which")
    @patch("questionary.text")
    def test_traceroute_system_command_not_found(
        self, mock_questionary_text, mock_which
    ):
        mock_which.return_value = None

        mock_questionary_text.return_value.ask.return_value = None

        traceroute_instance = Traceroute(host="example.com")

        with self.assertRaises(FileNotFoundError):
            traceroute_instance.traceroute_system()
