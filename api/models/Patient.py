from ..structures.doublelinkedlist.DoubleLinkedList import DoubleLinkedList
class Patient:
    def __init__(self,
                 name=None,
                 age=None,
                 periods=None,
                 result=None,
                 matrix_size=None,
                 cell_req_list=None,
                 generated_periods: DoubleLinkedList=None):
        self.__name = name
        self.__age = age
        self.__periods = periods
        self.__result = result
        self.__matrix_size = matrix_size
        self.__cell_req_list = cell_req_list
        self.__generated_periods: DoubleLinkedList = generated_periods

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        self.__name = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @age.deleter
    def age(self):
        self.__age = None

    @property
    def periods(self):
        return self.__periods

    @periods.setter
    def periods(self, value):
        self.__periods = value

    @periods.deleter
    def periods(self):
        self.__periods = None

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value

    @result.deleter
    def result(self):
        self.__result = None

    @property
    def matrix_size(self):
        return self.__matrix_size

    @matrix_size.setter
    def matrix_size(self, value):
        self.__matrix_size = value

    @matrix_size.deleter
    def matrix_size(self):
        self.__matrix_size = None

    @property
    def cell_req_list(self):
        return self.__cell_req_list

    @cell_req_list.setter
    def cell_req_list(self, value):
        self.__cell_req_list = value

    @cell_req_list.deleter
    def cell_req_list(self):
        self.__cell_req_list = None

    @property
    def generated_periods(self):
        return self.__generated_periods

    @generated_periods.setter
    def generated_periods(self, value):
        self.__generated_periods = value
