import unittest
from unittest.mock import MagicMock, patch

from ctrl_node.common.modules.whois import Whois


class TestWhois(unittest.TestCase):

    @patch("questionary.text")
    def test_display_domain_info(self, mock_questionary_text):
        mock_questionary_text.return_value.ask.return_value = None
        whois_instance = Whois()
        self.assertIsNone(whois_instance.display_domain_info())
