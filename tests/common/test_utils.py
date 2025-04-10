import unittest
from unittest.mock import patch
from ctrl_node.common.utils import (
    askforhost,
    clean_console,
)


class TestUtils(unittest.TestCase):

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
