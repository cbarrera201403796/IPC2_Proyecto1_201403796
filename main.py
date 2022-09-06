from api.models.Cell import Cell
from api.structures.CellReq import CellReq
from api.structures.Matrix import Matrix
from api.workers.FileParser import FileParser


# celList = []
# celList.append(CellReq(row=1, col=1))
# celList.append(CellReq(row=4, col=4))
# celList.append(CellReq(row=5, col=5))


# matrix = Matrix(cell_req_list=celList, max_rows_size=600, max_cols_size=600)
# matrix.generate_matrix()
# matrix.iterate_matrix()

fileParser = FileParser('/Users/admin/PycharmProjects/IPC2P1/api/workers/entry.xml')
patients = fileParser.parse_file()

for patient in patients:
    print('_____________________')
    print('Name: ', patient.name)
    print('Age: ', patient.age)
    print('Matrix Size: ', patient.matrix_size)
    print('Periods: ', patient.periods)
    print('Cells:')
    for cell in patient.cell_req_list:
        print('Col: ', cell.col)
        print('Row: ', cell.row)
    print('_____________________')
