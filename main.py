from api.models.Cell import Cell
from api.structures.CellReq import CellReq
from api.structures.Matrix import Matrix
from api.workers.FileParser import FileParser


celList = []
celList.append(CellReq(row=1, col=1))
celList.append(CellReq(row=4, col=4))
celList.append(CellReq(row=5, col=5))


matrix = Matrix(cell_req_list=celList, max_rows_size=20, max_cols_size=20)
matrix.generate_matrix()
matrix.iterate_matrix_and_get_graph("prueba")
