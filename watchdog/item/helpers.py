from typing import Any
import requests
from requests import Response
from bs4 import BeautifulSoup, ResultSet


def get_item_page_html(url: str) -> str | None:
    response: Response = requests.get(url)
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        response.raise_for_status()


def get_item_price(soup_html: BeautifulSoup) -> str: 
    PRICE_TAG_TYPE: str = "span"
    price_classes: list[str] = ["a-price-symbol", "a-price-whole", "a-price-fraction"]
    price: str = ""

    for index, class_name in enumerate(price_classes):
        tag: ResultSet[Any] = soup_html.find_all(PRICE_TAG_TYPE, class_=class_name)[0]
        price += tag.text

    return price
