from bs4 import BeautifulSoup

from watchdog.item.helpers import get_item_price, get_item_page_html


class Item:
    def __init__(self, url: str):
        self.__url: str = url
        self.__name: str = ""
        self.__price: str = self.set_price()  
        self.__soup: BeautifulSoup = self.make_soup()

    @property
    def url(self) -> str:
        return self.__url


    @property
    def soup(self) -> BeautifulSoup:
        return self.__soup


    @url.setter
    def url(self, url: str) -> None:
        self.__url = url


    @property
    def name(self) -> str:
        return self.__name

    # TODO: put method to set name here 


    @property
    def price(self) -> str:
        return self.__price


    def set_price(self):
        return get_item_price(self.__soup)
    

    def make_soup(self) -> BeautifulSoup:
        html: str | None = get_item_page_html(self.url)
        soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
        return soup

