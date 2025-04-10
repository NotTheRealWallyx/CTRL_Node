import unittest
from unittest.mock import patch
from ctrl_node.common.modules.host_to_ip import HostToIp


class TestHostToIp(unittest.TestCase):
    @patch("ctrl_node.common.modules.host_to_ip.askforhost", return_value="example.com")
    def test_initialization(self, mock_askforhost):
        instance = HostToIp()
        self.assertEqual(instance.host, "example.com")
        mock_askforhost.assert_called_once()

    @patch(
        "ctrl_node.common.modules.host_to_ip.socket.gethostbyname",
        return_value="93.184.216.34",
    )
    @patch("builtins.print")
    def test_get_ip_from_hostname(self, mock_print, mock_gethostbyname):
        instance = HostToIp(host="example.com")
        with patch.object(instance, "complete", return_value=None):
            instance.get_ip_from_hostname()
            mock_gethostbyname.assert_called_once_with("example.com")
            mock_print.assert_any_call("The IP for example.com is 93.184.216.34")


if __name__ == "__main__":
    unittest.main()
