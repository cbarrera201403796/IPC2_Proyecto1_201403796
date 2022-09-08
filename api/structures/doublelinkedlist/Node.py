class Node:
    def __init__(self, data=None):
        self.__index = None
        self.__next = None
        self.__previous = None
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @data.deleter
    def data(self):
        self.__data = None

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, value):
        self.__index = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, value):
        self.__previous = value

