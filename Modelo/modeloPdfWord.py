
class modeloPdfWord():


    def __init__(self):
        pass

    def word(self,archivo):

        nombre = archivo.split(".docx")[0]

        return nombre


    def pdf(selfs,archivo):

        nombre = archivo.split(".pdf")[0]

        return nombre
