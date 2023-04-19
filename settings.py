from db import Database

from download import Download

from os import getlogin, system, chdir, listdir,remove,rmdir

from time import sleep

from validations import validation

from pdf2docx import parse

from docx2pdf  import convert

from PIL import Image

from patoolib import extract_archive

from pytube import YouTube

from autolib import automa

from windolib import Windows

from moviepy.editor import *

from pathlib import Path

from pathlib import Path
from shutil import move

class setting():

    descargas = Download()

    database = Database()

    validations = validation()

    def __init__(self):
        self.database
        self.user()
        

    def user(self):
        
        print("Cargando...")
        response = self.database.ReadUser()

        if(response == None):
        
            while True:
                
                response =  self.database.InsertUser(getlogin())
        
                if(response == True):

                    self.ruta()

                    break 

        elif(response[0] != getlogin()):

            print("Se a detectado que HESTIA se abrió en otro computador ")

            sleep(12)

            print("Se comenzará una nueva configuración para este pc ")

            sleep(12)

            response = self.database.DelateSettings()

            if response == True:

                response =  self.database.InsertUser(getlogin())

                if(response == True):

                    self.ruta()

                else:

                    print(response)

                    sleep(10) 
            else:
                print(response)

                sleep(10) 

        system("cls")          

            

    
    def ruta(self):
        respuesta = input("Quieres que HESTIA pase tus archivos a otros discos. Ingrese 1 para sí, o enter para no: ")

        if respuesta == "1":

            ruta = input("Ingrese la letra del disco a utilizar: ").upper()

            response = self.validations.disk(ruta)

            if response.endswith(":/"):

                response = self.database.InsertAddres(response)

                if(response == True):

                    print("Ruta guardad...")
                    
                    sleep(10) 

                else:

                    print(response)

            else: print("Response")           
        else:

            response = self.database.InsertAddres("C:/")

            if response == True:

                print("La ruta guardada por defecto...")

                sleep(10)

                onedriver = self.validations.oneDrive()

                if onedriver:
    
                    data = self.database.InsertCloud("1")
                
                else:

                    data = self.database.InsertCloud("0")

                if data == Exception :

                    input(data)
                system("cls")

class converts():

    validations = validation()

    def __init__(self):
        pass
    

    def files(self,options):
        
        while True:

            try:
                inp = input("Arraste aqui el archivo que desea  convertir: ")

                repuesta = self.validations.filesvalidations(inp)

                if repuesta != False:

                    output =""

                    for ruta in repuesta:

                        output = output + ruta

                    if options == "1":

                        output = output + ".docx"

                        parse(inp,output, start=0, end=0)

                    elif options == "2":
                    
                        output = output + ".pdf"

                        convert(inp)

                    print("el archivo ya se a convertido")

                    break
                
                else:
                
                    print("el archivo ingresado no es pdf") 

                system("cls")
            
            except Exception as e:

                input(e) 

    def imagenes(self,options):

        while True:    
            try:
                imagen = input("Arraste aqui la imagen que desea convertir: ")

                resultados = self.validations.images(imagen)

                if resultados != False:

                    file = "" 

                    for resultado in resultados:

                        file = file + resultado

                    if options == "1":

                        file = ".png"

                    elif options == "2":

                        file = ".jpg"

                    im = Image.open(imagen)

                    im.save(file)

                    im.close()

                    print("La imagen se a convertido")

                    sleep(5)

                    break

                else:

                    print("El archivo ingresado no se puede convertir, porfavor intente de nuevo")

            except Exception as e:

                print(e)

    def mp3File(self):

            try:
                file = input("Arraste aqui el archivo que desea convertir: ")

                response = self.validations.audiovalidations(file)

                if(response != False and response != "Espacios"):

                    convert = response.split(".mp4")[0]

                    video = VideoFileClip(response)

                    sonido = video.audio

                    mp3 = convert +".mp3"

                    sonido.write_audiofile(mp3) 

                    sonido.close()

                    video.close()

                elif(response == "Espacios"):

                    print("El archivo ingreasado contiene esapcios porfavor cambie el nombre intentolo de nuevo")

                else:
                
                    input("a")

            except Exception as e:

                print(e)


    def mp3MultiFile():
            
        while True:

            try:
                files = input("Arrate aqui la carpeta: ")

                chdir(files) 

                for file in listdir():

                    if file.endswith(".mp4"):

                        video = VideoFileClip(file)

                        sonido = video.audio
                        
                        extension  = file.split('.mp4')[0]
                        
                        mp3 = extension +".mp3"
                        
                        sonido.write_audiofile(mp3) 

                        sonido.close()
                        
                        video.close()
                    
                        move(mp3,"C:/Users/" + getlogin() + "/Downloads/")

                        break

            except Exception as e:

                print(e)
        
class compressor():

    def __init__(self):
        pass

    def Descompresor(self):

        while True:


            try:

                file = input("Arraste aqui el archivo a descomprimir: ")

                extract_archive(file)

                print("La extrasion a finalizado correctamente")

                break

            except Exception as e:

                print(e)

                sleep(5)

                
class youlib():

    audioConvert = converts()

    def __init__(self):
        pass

    def videoOrAudio(self,option):

        while True:
            url = input("Ingrese la el link o la direccion url: ")
            try:

                if(url.startswith("https://www.youtube.com/watch?v=")):

                    chdir("C:/Users/" + getlogin() + "/Downloads/")

                    yt = YouTube(url)
                    
                    if option == "1":

                        videos = yt.streams.get_highest_resolution()

                        videos.download("C:/Users/" + getlogin() + "/Downloads/")

                    elif option == "2":

                        videos = yt.streams.get_lowest_resolution()

                        videos.download("C:/Users/" + getlogin() + "/Downloads/")

                    if option == "3":

                        videos = yt.streams.get_lowest_resolution()

                        Path("Audio").mkdir(exist_ok=True)

                        

                        videos.download("C:/Users/" + getlogin() + "/Downloads/Audio/")
                        
                        chdir("C:/Users/" + getlogin() + "/Downloads/Audio/")
                        
                        for file in listdir():

                            self.audioConvert.mp3.audioHestia(file)

                            audio = file.split("mp4")[0]

                            move(audio+".mp3","C:/Users/" + getlogin() + "/Downloads/")

                            remove("C:/Users/" + getlogin() + "/Downloads/Audio")

                    print("La descarga del video es correcta..")

                    sleep(5)

                    system("cls")

                    break

                    
                else:

                    print("La direccion ingresada no es correcta")

            except Exception as error:

                print(f"Error al descargar un video {error}")

class automatization():

    data = Database()
    autolib = automa()
    validations = validation()
    def __init__(self):
        self.data
        self.auto()
        self.autolib

    
    def auto(self):

        router = ""

        disk = self.data.ReadAdress()[0]

        documents = ""

        onedrive = ""
        
        if(disk.endswith("C:/")):

            onedrive = self.data.ReadCloud()

            if onedrive[0] == "1":

                documents = self.validations.documentsOneDriver()

                router = disk + "Users/"+getlogin()+"/OneDriver/"+documents+"/"

            else: 

                documents = self.validations.documentsNormal()

                router = disk + "Users/"+getlogin()+"/"+documents+"/"
            
        else:

            router = disk
        

        self.autolib.documnts(router)


        system("cls")


hola = converts()

hola.mp3File()