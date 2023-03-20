from pytube import YouTube
import os

def videoAltaResolucion():

    url = input("Ingrese la el link o la direccion url: ")

    while True:

        try:

            if(url.startswith("https://www.youtube.com/watch?v=")):
                
                yt = YouTube(url)

                videos = yt.streams.get_highest_resolution()

                if not os.path.exists("C:/Users/" + os.getlogin() + "/Documentos"):   
                    videos.download("C:/Users/" + os.getlogin() + "/Documents/Imagenes y Videos/Videos/")
                    break
                else:
                    videos.download("C:/Users/" + os.getlogin() + "/Documentos/Imagenes y Videos/Videos/")
                    break
                
            else:

                print("La direccion ingresada no es correcta")


        except Exception as error:

            print(f"Error al descargar un video {error}")

def videoBajaResolucion():

    url = input("Ingrese la el link o la direccion url: ")

    while True:

        try:

            if(url.startswith("https://www.youtube.com/watch?v=")):
                
                yt = YouTube(url)

                videos = yt.streams.get_lowest_resolution()

                if not os.path.exists("C:/Users/" + os.getlogin() + "/Documentos"):   
                    videos.download("C:/Users/" + os.getlogin() + "/Documents/Imagenes y Videos/Videos/")
                    break
                else:
                    videos.download("C:/Users/" + os.getlogin() + "/Documentos/Imagenes y Videos/Videos/")
                    break
                
            else:

                print("La direccion ingresada no es correcta")


        except Exception as error:

            print(f"Error al descargar un video {error}")
