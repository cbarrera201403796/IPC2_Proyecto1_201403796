
class Cell:
    STATUS_INFECTED = 1
    STATUS_NON_INFECTED = 0

    def __init__(self, upper_cell=None, down_cell=None, left_cell=None, right_cell=None, status=None, row=None, col=None):
        self.__up = upper_cell
        self.__down = down_cell
        self.__left = left_cell
        self.__right = right_cell
        self.__status = status
        self.__row = row
        self.__col = col

    # defines getters and setters
    @property
    def up(self):
        return self.__up

    @up.setter
    def up(self, value):
        self.__up = value

    @up.deleter
    def up(self):
        self.__up = None

    @property
    def down(self):
        return self.__down

    @down.setter
    def down(self, value):
        self.__down = value

    @down.deleter
    def down(self):
        self.__down = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @left.deleter
    def left(self):
        self.__left = None

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value

    @right.deleter
    def right(self):
        self.__right = None

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @status.deleter
    def status(self):
        self.__status = None

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

