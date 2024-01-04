from os import chdir
from pytube import YouTube
from Modelo.modeloYoutube import modeloYoutube
from view.vistaAlerta import vistaAlerta
class controladorYoutube():

    def __init__(self):

        self.__youtube = None
        self.__modeloYoutube = modeloYoutube()
        self.__aletas = vistaAlerta()

    def Descargar(self,link,boton,ubicacion):
        try:

            chdir(ubicacion + "/Imagenes y Videos/Videos")
            respuesta = self.__modeloYoutube.validarUrl(link)
            if respuesta:

                self.__youtube = YouTube(link)

                if(boton == "Alta"):

                    self.__youtube.streams.get_highest_resolution().download()

                    self.__aletas.informacion("Descarga completa")

                elif( boton == "Baja"):

                    self.__youtube.streams.get_lowest_resolution().download()

                    self.__aletas.informacion("Descarga completa")

                else:

                    titulo = self.__youtube.title

                    audio_stream = self.__youtube.streams.filter(only_audio=True).first()

                    audio_stream.download(filename=titulo + ".mp3")

                    self.__aletas.informacion("Descarga completa")

        except Exception:

            self.__aletas.error("Hubo un error al mento de hacer las descarga" + Exception)

        finally:

            pass
