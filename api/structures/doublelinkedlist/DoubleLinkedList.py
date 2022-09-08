from ..doublelinkedlist.Node import Node


class DoubleLinkedList:
    def __init__(self):
        self.__root: Node = None
        self.__last: Node = None
        self.__counter = -1

    def add(self, data):
        self.__counter += 1
        new_node = Node(data=data)
        new_node.index = self.__counter
        if self.__root is None:
            self.__root = new_node
            self.__last = new_node
        else:
            self.__last.next = new_node
            new_node.previous = self.__last
            self.__last = new_node

    def size(self):
        return self.__counter + 1

    def get(self, index):
        current = self.__root
        while current.next and current.index is not index:
            current = current.next
        return current.data

    def iterate(self):
        current = self.__root
        while current:
            print('Index', current.index)
            current = current.next

