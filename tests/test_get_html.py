import unittest
from unittest.mock import patch, Mock

from watchdog.item.helpers import get_item_page_html


class TestRequestHelpers(unittest.TestCase):
    @patch("requests.get")
    def test_get_item_page_html_valid(self, mock_get: Mock):
        mock_response: Mock = Mock()
        mock_response.status_code = 200
        mock_response.text = "<html>Test Response</html>"

        mock_get.return_value = mock_response

        func_result: str | None = get_item_page_html("https://www.test.com")

        self.assertEqual(func_result, "<html>Test Response</html>")


if __name__ == "__main__":
    _ = unittest.main()
