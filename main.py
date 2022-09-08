from tkinter import filedialog

from api.models.Cell import Cell
from api.structures.CellReq import CellReq
from api.structures.Matrix import Matrix
from api.structures.doublelinkedlist.DoubleLinkedList import DoubleLinkedList
from api.workers.FileParser import FileParser

filepath = filedialog.askopenfilename(filetypes=[("XML Files", ".xml")])


# celList = []
celList = DoubleLinkedList()

celList.add(CellReq(row=1, col=1))
celList.add(CellReq(row=1, col=2))
celList.add(CellReq(row=2, col=1))
celList.add(CellReq(row=2, col=2))
celList.add(CellReq(row=1, col=9))
celList.add(CellReq(row=1, col=10))
celList.add(CellReq(row=2, col=9))
celList.add(CellReq(row=2, col=10))
celList.add(CellReq(row=5, col=2))
celList.add(CellReq(row=5, col=3))
celList.add(CellReq(row=6, col=2))
celList.add(CellReq(row=6, col=3))

celList.add(CellReq(row=5, col=8))
celList.add(CellReq(row=5, col=9))
celList.add(CellReq(row=6, col=8))
celList.add(CellReq(row=6, col=9))

celList.add(CellReq(row=9, col=1))
celList.add(CellReq(row=9, col=2))
celList.add(CellReq(row=10, col=1))
celList.add(CellReq(row=10, col=2))
celList.add(CellReq(row=9, col=9))
celList.add(CellReq(row=9, col=10))
celList.add(CellReq(row=10, col=9))
celList.add(CellReq(row=10, col=10))

matrix = Matrix(cell_req_list=celList, max_rows_size=10, max_cols_size=10)
matrix.generate_matrix()
matrix.iterate_matrix_and_get_graph("prueba1")

matrix2 = Matrix(cell_req_list=matrix.get_next_data(), max_rows_size=10, max_cols_size=10)
matrix2.generate_matrix()
matrix2.iterate_matrix_and_get_graph("prueba2")

