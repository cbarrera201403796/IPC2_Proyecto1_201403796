import graphviz


class GraphicGenerator:
    def __init__(self, source_file=None, patient_name=None):
        self.__source_file = source_file
        self.__patient_name = patient_name

    @property
    def source_file(self):
        return self.__source_file

    @source_file.setter
    def source_file(self, value):
        self.__source_file = value

    @source_file.deleter
    def source_file(self):
        self.__source_file = None

    @property
    def patient_name(self):
        return self.patient_name

    @patient_name.setter
    def patient_name(self, value):
        self.__patient_name = value

    @patient_name.deleter
    def patient_name(self):
        self.__patient_name = None

    def generate_document(self):
        dot = graphviz.Digraph(comment=self.__patient_name)
        dot.render(self.__source_file, view=True).replace('\\', '/')




