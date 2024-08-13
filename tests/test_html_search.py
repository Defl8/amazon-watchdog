import unittest
from bs4 import BeautifulSoup
from watchdog.item.helpers import get_item_price, get_item_name


class TestHtmlSearching(unittest.TestCase):
    def test_get_price_valid(self):
        html_doc: str = """
            <span class="a-price-symbol">$</span>
            <span class="a-price-whole">159<span class="a-price-decimal">.</span></span>
            <span class="a-price-fraction">99</span>
            """
        expected_result: str = "$159.99"

        soup: BeautifulSoup = BeautifulSoup(html_doc, 'html.parser')
        func_result: str = get_item_price(soup)
        print("Testing if get_item_price is working...")
        print(f"Expected result is {expected_result}")
        print(f"Function result is {func_result}")

        self.assertEqual(func_result, expected_result)


    def test_get_name_valid(self):
        html_doc: str = """
            <span id="productTitle">Test Name</span>
            """
        expected_result: str = "Test Name"
        soup: BeautifulSoup = BeautifulSoup(html_doc, 'html.parser')
        func_result: str = get_item_name(soup)
        print("Testing if get_item_price is working...")
        print(f"Expected result is {expected_result}")
        print(f"Function result is {func_result}")

        self.assertEqual(func_result, expected_result)


if __name__ == "__main__":
    _ = unittest.main()
