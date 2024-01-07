from os import chdir,remove,getlogin,system
from pytube import YouTube
class ViewYoutube():

    def __init__(self):
        pass

    def videos(self):

    


        while True:

            print('''
                ********************************************** MENU DE OPCIONES ************************************
                * 1. Video en alta resolución                                                                      *
                * 2. Video en baja resolución                                                                      *
                * 3. Audio                                                                                         *
                * 4. Salir                                                                                         *
                ****************************************************************************************************
            
            ''')

            opncion = input("Ingrese una opción: ")

            chdir("C:/Users/" + getlogin() + "/Downloads/Imagenes y Videos/Videos")

            

            match opncion:

                case "1":
                    while True:
                        
                        url = input("Ingrese la dirección url: ")
                    
                        if(url != "" and url.startswith("https://www.youtube.com/watch?v=")):

                            video = YouTube(url)

                            video.streams.get_highest_resolution().download()
                            system("cls")
                            print(''' 
                                ******************************** Informacion ***************************
                                * Descarga completa                                                    *
                                ************************************************************************
                            ''')
                            r = input("Si deseas no seguir descargando mas videos de alta ingrese [y]")
                            
                            if(r == "y" or r == "Y"):
                            
                                break

                        else:

                            print(" La dirección URL ingresada invalida")

                
                case "2":

                    while True:

                        url = input("Ingrese la dirección url:")

                        if(url != ""and url.startswith("https://www.youtube.com/watch?v=")):

                            video = YouTube(url)

                            video.streams.get_lowest_resolution().download()
                            system("cls")

                            print(''' 
                                ******************************** Informacion ***************************
                                * Descarga complecta                                                   *
                                ************************************************************************
                            ''')

                            r = input(" Si deseas no seguir descargando mas  videos de baja ingrese [y]")
                            
                            if(r == "y" or r == "Y"):
                            
                                break

                        else:

                            print(" La dirección URL ingresada invalida ")

                            
                
                case "3":
                    while True:

                        print(''' 
                            ******************************** Informacion ***************************
                            *Los audios descargados estaran descargados en la carpeta Videos       *
                            ************************************************************************
                        ''')
                        url = input("Ingrese la dirección url: ")

                        if(url != "" and url.startswith("https://www.youtube.com/watch?v=")):

                            while True:
                                nombre = input("Ingrese el nombre del audio: ")

                                if nombre != "":

                                    video = YouTube(url)
                                    
                                    audio_stream = video.streams.filter(only_audio=True).first()

                                    audio_stream.download(filename= nombre+".mp3")
                                    
                                    system("cls")

                                    break
                                else:

                                    print("No ingreso el nombre del audio")

                            r = input("Si deseas no seguir descargando mas audios ingrese [y]")

                            print(''' 
                                ******************************** Informacion ***************************
                                * Descarga complecta                                                   *
                                ************************************************************************
                            ''')

                            if(r == "y" or r == "Y"):
                                
                                break

                        else:
                            print(" La dirección URL ingresada invalida ")
                case "4":
                    
                    break

                case _:

                    print(" La opción ingresada no existe")
