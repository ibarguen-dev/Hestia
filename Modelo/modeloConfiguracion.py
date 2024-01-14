import re


class modeloConfiguracion():

    """
    Clase que realiza validaciones relacionadas con la configuración del programa.
    """

    def __init__(self):
        """
        Constructor de la clase.
        """
        self.__rgex = re

    def validaciones(self, ruta):

        """
        Realiza validaciones en una ruta dada.

        Args:
            ruta (str): La ruta a ser validada.

        Returns:
            bool: True si la ruta es válida, False si no lo es.
        """

        try:
            patron = r'^[cC-zZ]:/(?:[^/:]+/)*[^/:]+$'
            return bool(self.__rgex.match(patron, ruta))
        except Exception as e:
            print(e)
        finally:
            pass
