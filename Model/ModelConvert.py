
class ModelConvert():

    """
    Clase que realiza operaciones relacionadas con la obtención de nombres base de archivos PDF y Word.
    """

    def __init__(self):
        """
        Constructor de la clase.
        """

        pass

    def verify_file_word(self,file):

        """
        Obtiene el nombre base de un archivo Word a partir del nombre de archivo dado.

        Args:
            archivo (str): El nombre del archivo Word.

        Returns:
            str: El nombre base del archivo Word.
        """

        name = file.split(".docx")[0]

        return name


    def verify_file_pdf(self,file):

        """
        Obtiene el nombre base de un archivo PDF a partir del nombre de archivo dado.

        Args:
            archivo (str): El nombre del archivo PDF.

        Returns:
            str: El nombre base del archivo PDF.
        """

        name = file.split(".pdf")[0]

        return name
