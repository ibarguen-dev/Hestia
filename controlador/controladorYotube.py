from os import chdir
from pytube import YouTube
from Modelo.modeloYoutube import modeloYoutube
from view.vistaAlerta import vistaAlerta
class controladorYoutube():

    def __init__(self):

        self.__youtube = None
        self.__modeloYoutube = modeloYoutube()
        self.__alertas = vistaAlerta()

    #metodo para la desdcar de videos y audios de youtube
    def Descargar(self,link,boton,ubicacion):
        try:


            respuesta = self.__modeloYoutube.validarUrl(link)
            if respuesta:

                self.__youtube = YouTube(link)

                if(boton == "Alta"):

                    chdir(ubicacion + "/Imagenes y Videos/Videos")

                    self.__youtube.streams.get_highest_resolution().download()

                    self.__alertas.informacion("Descarga completa")

                elif( boton == "Baja"):

                    chdir(ubicacion + "/Imagenes y Videos/Videos")

                    self.__youtube.streams.get_lowest_resolution().download()

                    self.__alertas.informacion("Descarga completa")

                else:

                    chdir(ubicacion + "/Audios")

                    titulo = self.__youtube.title

                    audio_stream = self.__youtube.streams.filter(only_audio=True).first()

                    audio_stream.download(filename=titulo + ".mp3")

                    self.__alertas.informacion("Descarga completa")

        except Exception as e:

            self.__alertas.error("Hubo un error al mento de hacer las descarga" + e)

        finally:

            pass
