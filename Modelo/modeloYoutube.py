from pytubefix import YouTube
from view.vistaAlerta import vistaAlerta
class modeloYoutube():
    """
    Clase que realiza validaciones relacionadas con enlaces de YouTube.
    """

    def __init__(self):
        """
        Constructor de la clase.
        """

        self.__alertas = vistaAlerta


    def validarUrl(self,url):

        """
        Valida si un enlace de YouTube es válido y corresponde a un video existente.

        Args:
            url (str): El enlace de YouTube a validar.

        Returns:
            bool: True si el enlace es válido y corresponde a un video existente, False en caso contrario.
        """

        try:
            if (url != "" and url.startswith("https://www.youtube.com/watch?v=")):
                video = YouTube(url)
                if video.title:
                    
                    return True

                else:

                    self.__alertas.error("El link ingresado no es valido o el video ya no existe")

                    return False
            else:

                self.__alertas.error("El link ingresado no es valido")

                return False

        except Exception as e:
            print(e)
            self.__alertas.error(e)

            return  False