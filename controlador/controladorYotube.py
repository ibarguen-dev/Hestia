from os import chdir
from pytube import YouTube
from Modelo.modeloYoutube import modeloYoutube
from view.vistaAlerta import vistaAlerta
class controladorYoutube():

    """
    Clase que gestiona la descarga de videos y audios de YouTube.
    """

    def __init__(self):

        """
         Constructor de la clase. Inicializa instancias de otras clases y variables.
        """
        self.__youtube = None
        self.__modeloYoutube = modeloYoutube()
        self.__alertas = vistaAlerta()


    def Descargar(self,link,boton,ubicacion):

        """
         Método para descargar videos o audios de YouTube.

         Args:
             link (str): El enlace del video de YouTube.
             boton (str): El botón seleccionado para la calidad de descarga (Alta, Baja o None).
             ubicacion (str): La ubicación en la que se guardarán los archivos descargados.

         Returns:
             None
         """

        try:
            respuesta = self.__modeloYoutube.validarUrl(link)
            if respuesta:
                self.__youtube = YouTube(link)

                if boton == "Alta":
                    chdir(ubicacion + "/Imagenes y Videos/Videos")
                    self.__youtube.streams.get_highest_resolution().download()
                    self.__alertas.informacion("Descarga completa")

                elif boton == "Baja":
                    chdir(ubicacion + "/Imagenes y Videos/Videos")
                    self.__youtube.streams.get_lowest_resolution().download()
                    self.__alertas.informacion("Descarga completa")


                elif boton == "Audio":
                    chdir(ubicacion + "/Audios")
                    titulo = self.__youtube.title
                    audio_stream = self.__youtube.streams.filter(only_audio=True).first()
                    audio_stream.download(filename=titulo + ".mp3")
                    self.__alertas.informacion("Descarga completa")

        except Exception as e:
            self.__alertas.error("Hubo un error al mento de hacer las descarga" + e)

        finally:

            pass
