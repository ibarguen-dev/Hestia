from os import chdir,remove,getlogin
from pytube import YouTube
from moviepy.editor import *
class ViewYoutube():

    def __init__(self):
        pass

    def videos(self):

        

        print('''
                ********************************************** MENU DE OPCIONES ************************************
                * 1. Video en alta Resolucion                                                                      *
                * 2. Video en baja Resolucion                                                                      *
                * 3. Audio                                                                                         *
                * 4. Salir                                                                                         *
                ****************************************************************************************************
        ''')

        opncion = input("Ingrese una opcion: ")

        while True:
            chdir("C:/Users/" + getlogin() + "/Downloads/Imagenes y Videos/Videos") 
            url = input("Ingrese la direccion url: ")

            match opncion:

                case "1":
                    if(url != ""):



                        video = YouTube(url)

                        video.streams.get_highest_resolution().download()

                        break

                    else:

                        print(" Error no ingreso niguna URL")

                        url = input("Ingrese la direccion url: ")
                
                case "2":
                    while True:
                        if(url != ""):


                            video = YouTube(url)

                            video.streams.get_lowest_resolution().download()

                            break

                        else:

                            print(" Error no ingreso niguna URL")

                            url = input("Ingrese la direccion url: ")
                
                case "3":
                    while True:
                        if(url != ""):


                            nombre = input("Ingrese el nombre del audio: ")

                            while True:
                                
                                if nombre != "":

                                    video = YouTube(url)

                                    audio = video.streams.filter(only_audio=True).first()

                                    audio.download(filename=nombre)

                                    clip = AudioFileClip(nombre+".mp4")

                                    clip.write_audiofile(nombre+".mp3")

                                    remove(nombre+".mp4")

                                    break
                                else:
                                    print("Error no ingreso el nombre del audio")

                                    nombre = input("Ingrese eñ nombre del archivo: ")

                            break
                        else:
                            print(" Error no ingreso niguna URL")

                            url = input("Ingrese la direccion url: ")
                
                case "4":
                    break

                case _:

                    print(" La opcion ingrsada no existe")
