from ..models.Cell import Cell
from ..structures.CellReq import CellReq
from ..structures.doublelinkedlist.DoubleLinkedList import DoubleLinkedList
import graphviz


class Matrix:

    def __init__(self, cell_req_list=None, max_rows_size=None, max_cols_size=None):
        self.__cell_req_list = cell_req_list
        self.__max_rows_size = max_rows_size
        self.__max_cols_size = max_cols_size
        self.__root = None
        self.__f = None

    def search_value(self, col, row):
        found = False
        iterator = 0
        return_value = False
        while not found and iterator < self.__cell_req_list.size():
            current_value = self.__cell_req_list.get(iterator)
            if current_value.col == col and current_value.row == row:
                return_value = True
                found = True
            iterator += 1

        return return_value

    def generate_matrix(self):
        column_counter = 1
        row_counter = 1
        self.__root = Cell()
        current = self.__root
        all_work_done = False
        going_forward = True
        cells_created = 1
        print("Enter Generate Matrix")

        while not all_work_done:
            current.row = row_counter
            current.col = column_counter
            print(str(column_counter) + ",", str(row_counter))
            if self.search_value(col=current.col, row=current.row):
                current.status = Cell.STATUS_INFECTED
            else:
                current.status = Cell.STATUS_NON_INFECTED
            print('Status: ', current.status)
            if going_forward and column_counter < self.__max_cols_size:
                current.right = Cell()
                current.right.left = current
                if row_counter != 1:
                    current.right.up = current.up.right
                    current.up.right.down = current.right
                column_counter += 1
                current = current.right
            elif going_forward and column_counter == self.__max_cols_size:
                current.down = Cell()
                current.down.up = current
                if row_counter == self.__max_rows_size:
                    all_work_done = True
                    current.col = column_counter
                    if self.search_value(col=column_counter, row=row_counter):
                        current.status = Cell.STATUS_INFECTED
                    else:
                        current.status = Cell.STATUS_NON_INFECTED
                else:
                    row_counter += 1
                    current = current.down
                    going_forward = False
            elif going_forward is False and column_counter > 1:
                current.left = Cell()
                current.left.up = current.up.left
                current.up.left.down = current.left
                current.left.right = current
                column_counter -= 1
                current = current.left
            elif not going_forward and column_counter == 1:
                current.down = Cell()
                current.down.up = current
                if row_counter == self.__max_rows_size:
                    all_work_done = True
                    current.col = column_counter
                    if self.search_value(col=column_counter, row=row_counter):
                        current.status = Cell.STATUS_INFECTED
                    else:
                        current.status = Cell.STATUS_NON_INFECTED
                else:
                    row_counter += 1
                    current = current.down
                    going_forward = True

    def get_node_name(self, node):
        if node:
            return "a" + str(node.col) + "b" + str(node.row)
        else:
            return ''

    def iterate_matrix_and_get_graph(self, file_name):
        self.__f = graphviz.Digraph(filename=file_name + ".gv", engine='neato', graph_attr={'splines': 'true'},
                                    node_attr={'shape': 'point'})

        ended = False
        current = self.__root
        going_right = True
        counter = 1
        while not ended:
            # print("Counter_", counter)
            color = "white"
            if current.status == 1:
                color = "red"
            self.__f.node(name=self.get_node_name(current),
                          label=(str(current.row) + "," + str(current.col)),
                          color="white" if current.status == 1 else "black",
                          fillcolor=color,
                          style="filled",
                          shape="box",
                          fontcolor="white" if current.status == 1 else "black",
                          pos=str(current.col) + "," + str(-1 * current.row) + "!")

            if going_right and current.right:
                current = current.right
                counter += 1
            elif going_right and not current.right:
                if current.row == self.__max_rows_size:
                    ended = True
                else:
                    current = current.down
                    counter += 1
                    going_right = False
            elif going_right is False and current.left:
                current = current.left
                counter += 1
            elif going_right is False and not current.left:
                if current.row == self.__max_rows_size:
                    ended = True
                else:
                    current = current.down
                    counter += 1
                    going_right = True
        self.relation_graph()

    def relation_graph(self):
        ended = False
        current = self.__root
        going_right = True
        counter = 1
        while not ended:
            if current.left and current.left.status is not None:
                self.__f.edge(self.get_node_name(current), self.get_node_name(current.left))
            if current.right and current.right.status is not None:
                self.__f.edge(self.get_node_name(current), self.get_node_name(current.right))
            if current.up and current.up.status is not None:
                self.__f.edge(self.get_node_name(current), self.get_node_name(current.up))
            if current.down and current.down.status is not None:
                self.__f.edge(self.get_node_name(current), self.get_node_name(current.down))

            if going_right and current.right:
                current = current.right
                counter += 1
            elif going_right and not current.right:
                if current.row == self.__max_rows_size:
                    ended = True
                else:
                    current = current.down
                    counter += 1
                    going_right = False
            elif going_right is False and current.left:
                current = current.left
                counter += 1
            elif going_right is False and not current.left:
                if current.row == self.__max_rows_size:
                    ended = True
                else:
                    current = current.down
                    counter += 1
                    going_right = True
        self.__f.attr(label='Matriz')
        self.__f.attr(fontsize='20')
        self.__f.view()


    def get_total_infected_cells(self, node: Cell):
        count = 0
        if node.right and node.down and node.left is None and node.up is None:
            if node.right.status == 1:
                count += 1
            if node.right.down.status == 1:
                count += 1
            if node.down.status == 1:
                count += 1
        elif node.right and node.down and node.left and node.up is None:
            if node.right.status == 1:
                count += 1
            if node.right.down.status == 1:
                count += 1
            if node.left.status == 1:
                count += 1
            if node.left.down.status == 1:
                count += 1
            if node.down.status == 1:
                count += 1
        elif node.right is None and node.down and node.left and node.up is None:
            if node.left.status == 1:
                count += 1
            if node.left.down.status == 1:
                count += 1
            if node.down.status == 1:
                count += 1
        elif node.right and node.down and node.left and node.up:
            if node.left.status == 1:
                count += 1
            if node.right.status == 1:
                count += 1
            if node.down.status == 1:
                count += 1
            if node.down.left.status == 1:
                count += 1
            if node.down.right.status == 1:
                count += 1
            if node.up.status == 1:
                count += 1
            if node.up.left.status == 1:
                count += 1
            if node.up.right.status == 1:
                count += 1
        elif node.right is None and node.down and node.left and node.up:
            if node.left.status == 1:
                count += 1
            if node.down.status and node.down.status == 1:
                count += 1
            if node.down.status and node.down.left.status == 1:
                count += 1
            if node.up.status == 1:
                count += 1
            if node.up.left.status == 1:
                count += 1
        elif node.right and node.down and node.left is None and node.up:
            if node.right.status == 1:
                count += 1
            if node.down.status == 1:
                count += 1
            if node.down.status and node.down.right.status == 1:
                count += 1
            if node.up.status == 1:
                count += 1
            if node.up.right.status == 1:
                count += 1
        elif node.right is None and node.down is None and node.left and node.up:
            if node.left.status == 1:
                count += 1
            if node.up.status == 1:
                count += 1
            if node.up.left.status == 1:
                count += 1
        elif node.right and node.down is None and node.left and node.up:
            if node.left.status == 1:
                count += 1
            if node.right.status == 1:
                count += 1
            if node.up.status == 1:
                count += 1
            if node.up.left.status == 1:
                count += 1
            if node.up.right.status == 1:
                count += 1
        elif node.right is None and node.down is None and node.left and node.up:
            if node.left.status == 1:
                count += 1
            if node.up.status == 1:
                count += 1
            if node.up.left.status == 1:
                count += 1
        return count

    def get_next_data(self):
        ended = False
        current = self.__root
        going_right = True
        counter = 1
        cell_req_list = DoubleLinkedList()
        while not ended:
            infected = self.get_total_infected_cells(current)
            cell = CellReq(col=current.col, row=current.row)
            if current.status == 1 and (infected == 2 or infected == 3):
                cell_req_list.add(cell)
            elif current.status == 0 and infected == 3:
                cell_req_list.add(cell)

            if going_right and current.right:
                current = current.right
                counter += 1
            elif going_right and not current.right:
                if current.row == self.__max_rows_size:
                    ended = True
                else:
                    current = current.down
                    counter += 1
                    going_right = False
            elif going_right is False and current.left:
                current = current.left
                counter += 1
            elif going_right is False and not current.left:
                if current.row == self.__max_rows_size:
                    ended = True
                else:
                    current = current.down
                    counter += 1
                    going_right = True
        return cell_req_list
