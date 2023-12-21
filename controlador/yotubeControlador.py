from os import chdir,remove,getlogin,system
from pytube import YouTube


class youtubeController():

    def __init__(self):

        self.__youtube = None

    def Descargar(self,link,boton):
        try:
            chdir("C:/Users/" + getlogin() + "/Downloads/Imagenes y Videos/Videos")
            self.__youtube = YouTube(link)

            if(boton == "Alta"):
                self.__youtube.streams.get_highest_resolution().download()
                return [0,"Descarga completa"]
            elif( boton == "Baja"):
                self.__youtube.streams.get_lowest_resolution().download()
                return [0,"Descarga completa"]
            else:
                titulo = self.__youtube.title

                audio_stream = self.__youtube.streams.filter(only_audio=True).first()

                audio_stream.download(filename=titulo + ".mp3")

                return [1,"Descarga completa"]

        except Exception:

            return("Hubo un error al mento de hacer las descarga" + Exception)


