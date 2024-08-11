class Item:
    def __init__(self, url: str):
        self.__url = url
        self.__name = ""

    @property
    def url(self):
        return self.__url


    @url.setter
    def url(self, url: str):
        self.__url = url


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name: str):
        self.__name = name
