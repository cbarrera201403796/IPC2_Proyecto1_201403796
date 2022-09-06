from xml.dom import minidom
from ..structures.CellReq import CellReq
from ..models.Patient import Patient


class FileParser:
    def __init__(self, file_path=None):
        self.__file_path = file_path

    def parse_file(self):
        document = minidom.parse(self.__file_path)
        patients = document.getElementsByTagName('paciente')
        mapped_patients = []
        for patient in patients:
            personal_data = patient.getElementsByTagName('datospersonales')[0]
            name = personal_data.getElementsByTagName('nombre')[0].firstChild.nodeValue
            age = personal_data.getElementsByTagName('edad')[0].firstChild.nodeValue

            periods = patient.getElementsByTagName('periodos')[0].firstChild.nodeValue
            m = patient.getElementsByTagName('m')[0].firstChild.nodeValue
            row = patient.getElementsByTagName('rejilla')[0]
            cells = row.getElementsByTagName('celda')
            cells_req_list = []
            for cell in cells:
                new_cell = CellReq()
                new_cell.row = cell.getAttribute('f')
                new_cell.col = cell.getAttribute('c')
                cells_req_list.append(new_cell)
            tmp_patient = Patient(
                name=name,
                age=age,
                periods=periods,
                matrix_size=m,
                cell_req_list=cells_req_list
            )
            mapped_patients.append(tmp_patient)
        return mapped_patients


