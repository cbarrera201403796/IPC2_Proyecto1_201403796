from ..models.Cell import Cell
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
        return_value = None
        while not found and iterator < len(self.__cell_req_list):
            current_value = self.__cell_req_list[iterator]
            if current_value.col == col and current_value.row == row:
                return_value = current_value
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
            if self.search_value(col=column_counter, row=row_counter):
                current.status = Cell.STATUS_INFECTED
            else:
                current.status = Cell.STATUS_NON_INFECTED

            if going_forward and column_counter < self.__max_cols_size:
                current.right = Cell()
                current.right.left = current
                if row_counter != 1:
                    current.right.up = current.up.right
                    current.up.right.down = current.right
                # print("Pos Col: ", column_counter)
                # print("Pos Row: ", row_counter)
                column_counter += 1
                current = current.right
                cells_created += 1

            elif going_forward and column_counter == self.__max_cols_size:
                current.down = Cell()
                current.down.up = current
                # print("Pos Col: ", column_counter)
                # print("Pos Row: ", row_counter)
                row_counter += 1
                current = current.down
                cells_created += 1
                going_forward = False
            elif going_forward is False and column_counter > 1:
                current.left = Cell()
                current.left.up = current.up.left
                current.up.left.down = current.left
                current.left.right = current
                # print("Pos Col: ", column_counter)
                # print("Pos Row: ", row_counter)
                column_counter -= 1
                current = current.left
                cells_created += 1
            elif not going_forward and column_counter == 1:
                current.down = Cell()
                current.down.up = current
                # print("Pos Col: ", column_counter)
                # print("Pos Row: ", row_counter)
                if not row_counter == self.__max_rows_size:
                    row_counter += 1
                current = current.down
                cells_created += 1
                going_forward = True
            all_work_done = cells_created == self.__max_rows_size * self.__max_cols_size

            if all_work_done:
                current.row = row_counter
                current.col = column_counter
                if self.search_value(col=column_counter, row=row_counter):
                    current.status = Cell.STATUS_INFECTED
                else:
                    current.status = Cell.STATUS_NON_INFECTED

    def get_node_name(self, node):
        if node:
            return str(node.col) + str(node.row)
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
            print("Counter_", counter)
            if current:
                self.__f.node(name=self.get_node_name(current),
                              label=(str(current.col)+","+str(current.row)),
                              color="red" if current.status == 1 else "black",
                              fillcolor="red" if current.status == 1 else "white",
                              shape="box",
                              pos=str(current.col)+","+str(-1*current.row)+"!")

            if going_right and current.right:
                current = current.right
                counter += 1
            elif going_right and not current.right:
                current = current.down
                counter += 1
                going_right = False
            elif going_right is False and current.left:
                current = current.left
                counter += 1
            elif going_right is False and not current.left:
                if not current.down:
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
            print("Counter_", counter)
            if current:
                if current.left:
                    self.__f.edge(self.get_node_name(current), self.get_node_name(current.left))
                if current.right:
                    self.__f.edge(self.get_node_name(current), self.get_node_name(current.right))
                if current.up:
                    self.__f.edge(self.get_node_name(current), self.get_node_name(current.up))
                if current.down:
                    self.__f.edge(self.get_node_name(current), self.get_node_name(current.down))

            if going_right and current.right:
                current = current.right
                counter += 1
            elif going_right and not current.right:
                current = current.down
                counter += 1
                going_right = False
            elif going_right is False and current.left:
                current = current.left
                counter += 1
            elif going_right is False and not current.left:
                if not current.down:
                    ended = True
                else:
                    current = current.down
                    counter += 1
                    going_right = True

        self.__f.view()

