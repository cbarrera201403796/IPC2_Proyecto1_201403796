from api.models.Cell import Cell
from api.structures.CellReq import CellReq
from api.structures.Matrix import Matrix
from api.workers.FileParser import FileParser


celList = []
celList.append(CellReq(row=1, col=1))
celList.append(CellReq(row=1, col=2))
celList.append(CellReq(row=2, col=1))
celList.append(CellReq(row=2, col=2))
celList.append(CellReq(row=1, col=9))
celList.append(CellReq(row=1, col=10))
celList.append(CellReq(row=2, col=9))
celList.append(CellReq(row=2, col=10))
celList.append(CellReq(row=5, col=2))
celList.append(CellReq(row=5, col=3))
celList.append(CellReq(row=6, col=2))
celList.append(CellReq(row=6, col=3))

celList.append(CellReq(row=5, col=8))
celList.append(CellReq(row=5, col=9))
celList.append(CellReq(row=6, col=8))
celList.append(CellReq(row=6, col=9))

celList.append(CellReq(row=9, col=1))
celList.append(CellReq(row=9, col=2))
celList.append(CellReq(row=10, col=1))
celList.append(CellReq(row=10, col=2))
celList.append(CellReq(row=9, col=9))
celList.append(CellReq(row=9, col=10))
celList.append(CellReq(row=10, col=9))
celList.append(CellReq(row=10, col=10))

matrix = Matrix(cell_req_list=celList, max_rows_size=10, max_cols_size=10)
matrix.generate_matrix()
matrix.iterate_matrix_and_get_graph("prueba1")

matrix2 = Matrix(cell_req_list=matrix.get_next_data(), max_rows_size=10, max_cols_size=10)
matrix2.generate_matrix()
matrix2.iterate_matrix_and_get_graph("prueba2")

