from tkinter import filedialog

from api.structures.Matrix import Matrix
from api.workers.FileParser import FileParser
from api.structures.doublelinkedlist.DoubleLinkedList import DoubleLinkedList

fileparser = FileParser(filedialog.askopenfilename(filetypes=[("XML Files", ".xml")]))
patient_list = fileparser.parse_file()


for i in range(patient_list.size()):
    patient = patient_list.get(i)
    matrix_list = DoubleLinkedList()
    next_period_data = None
    for p in range(patient.periods):
        mtxTmp = None
        if next_period_data:
            mtxTmp = Matrix(next_period_data, patient.matrix_size, patient.matrix_size)
        else:
            mtxTmp = Matrix(patient.cell_req_list, patient.matrix_size, patient.matrix_size)

        mtxTmp.generate_matrix()
        mtxTmp.iterate_matrix_and_get_graph("Paciente " + patient.name + " Periodo " + str(p+1), patient.name)
        matrix_list.add(mtxTmp)
        next_period_data = mtxTmp.get_next_data()




