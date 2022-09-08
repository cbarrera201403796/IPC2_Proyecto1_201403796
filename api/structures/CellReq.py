
class CellReq:
    def __init__(self, row=None, col=None):
        self.__row = row
        self.__col = col

    @property
    def row(self):
        return self.__row

    @row.setter
    def row(self, value):
        self.__row = value

    @row.deleter
    def row(self):
        self.__row = None

    @property
    def col(self):
        return self.__col

    @col.setter
    def col(self, value):
        self.__col = value

    @col.deleter
    def col(self):
        self.__col = None
