from bs4 import BeautifulSoup

from watchdog.item.helpers import get_item_price, get_item_page_html, get_item_name


class Item:
    def __init__(self, url: str):
        self.__url: str = url
        self.__name: str = self.set_name()
        self.__price: str = self.set_price()  
        self.__soup: BeautifulSoup = self.make_soup()

    @property
    def url(self) -> str:
        return self.__url


    @property
    def soup(self) -> BeautifulSoup:
        return self.__soup


    @property
    def name(self) -> str:
        return self.__name


    def set_name(self) -> str:
        return get_item_name(self.__soup)


    @property
    def price(self) -> str:
        return self.__price


    def set_price(self) -> str:
        return get_item_price(self.__soup)
    

    def make_soup(self) -> BeautifulSoup:
        html: str | None = get_item_page_html(self.url)
        soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
        return soup
