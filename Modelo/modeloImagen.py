

class modeloImagen():


    """
    Clase que realiza operaciones relacionadas con la verificación de nombres de archivos de imagen.
    """

    def __init__(self):
        """
        Constructor de la clase.
        """
        pass

    def verificar(self,ruta):
        """
        Verifica y extrae el nombre base de un archivo de imagen a partir de la ruta.

        Args:
            ruta (str): La ruta del archivo de imagen.

        Returns:
            str: El nombre base del archivo de imagen.
        """

        nombre = None

        try:

            if ruta.endswith(".png"):
                nombre = ruta.split(".png")[0]
            elif ruta.endswith(".jpeg"):
                nombre = ruta.split(".jpeg")[0]
            elif ruta.endswith(".jpg"):
                nombre = ruta.split(".jpg")[0]
            elif ruta.endswith(".svg"):
                nombre = ruta.split(".svg")[0]

            return nombre
        except Exception as e:

            print(e)
        finally:
            del nombre