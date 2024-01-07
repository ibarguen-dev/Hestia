from pytube import  YouTube
from view.vistaAlerta import vistaAlerta
class modeloYoutube():

    def __init__(self):

        self.__alertas = vistaAlerta


    def validarUrl(self,url):
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

            self.__alertas.error(e)

            return  False