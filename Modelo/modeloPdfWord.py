
class modeloPdfWord():

    """
    Clase que realiza operaciones relacionadas con la obtención de nombres base de archivos PDF y Word.
    """

    def __init__(self):
        """
        Constructor de la clase.
        """

        pass

    def word(self,archivo):

        """
        Obtiene el nombre base de un archivo Word a partir del nombre de archivo dado.

        Args:
            archivo (str): El nombre del archivo Word.

        Returns:
            str: El nombre base del archivo Word.
        """

        nombre = archivo.split(".docx")[0]

        return nombre


    def pdf(selfs,archivo):

        """
        Obtiene el nombre base de un archivo PDF a partir del nombre de archivo dado.

        Args:
            archivo (str): El nombre del archivo PDF.

        Returns:
            str: El nombre base del archivo PDF.
        """

        nombre = archivo.split(".pdf")[0]

        return nombre
