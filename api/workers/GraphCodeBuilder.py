class GraphCodeBuilder:
    def __init__(self, patients_list=None):
        self.__patients_list = None
        self.__source_code_generated = None

    @property
    def patient_list(self):
        return self.__patients_list

    @patient_list.setter
    def patient_list(self, value):
        self.__patients_list = value

    @patient_list.deleter
    def patient_list(self):
        self.__patients_list = None

    def generate_code(self):
        return None


