class Item:
    def __init__(self, url: str):
        self.__url = url

    @property
    def url(self):
        return self.__url


    @url.setter
    def url(self, url: str):
        self.__url = url
