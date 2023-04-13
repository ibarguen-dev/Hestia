from db import Database

from download import Download

from os import getlogin, system, chdir, listdir,remove,rmdir

from time import sleep

from validations import validation

from pdf2docx import parse

from PIL import Image

from patoolib import extract_archive, create_archive

from pytube import YouTube

from autolib import automa

from windolib import Windows

from moviepy.editor import *

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

class convert():

    def __init__(self):
        pass
    
    def Pdf(self):

        pdf = input("Arraste aqui el pdf para convertir: ")

        if(pdf.endswith(".pdf")):

            rutas = pdf.split(".pdf")

            word =""

            for ruta in rutas:

                word = word + ruta

            word = word + ".docx"

            parse(pdf,word, start=0, end=0)

            print("el archivo ya se a convertido")

        else:
       
            print("el archivo ingresado no es pdf") 
        
        system("cls")
    
    def Word(self):

        word = input("Arraste aqui el word para convertir: ")

        if word.endswith(".docx") or word.endswith(".doc") or word.endswith(".docm") or word.endswith(".dot") or word.endswith(".dotx") or word.endswith(".dotm"):

            rutas = ""

            if word.endswith(".doc"):

                rutas = word.split(".doc")

            elif word.endswith(".doc"):

                rutas = word.split(".doc")

            elif word.endswith(".docm"):

                rutas = word.split(".docm")

            elif word.endswith(".dot"):

                rutas = word.split(".dot")

            elif word.endswith(".dotx"):

                rutas = word.split(".dotx")

            elif word.endswith(".dotm"):

                rutas = word.split(".dotm")

            pdf = ""

            for ruta in rutas:

                pdf = pdf + ruta

            pdf = pdf + "pdf"

            parse(word, pdf, start=0, end=0)

        else:

            print("el archivo ingresado no es word")
        
        system("cls")

    def Png(self):

        imagen = input("Arraste aqui la imagen para convertir: ")

        if(imagen.endswith(".jpg") or  imagen.endswith(".webp")):

            extension = ""

            if imagen.endswith(".jpg"):

                extension = imagen.split(".jpg")

            elif imagen.endswith(".webp"):

                extension = imagen.split(".webp")

            png = ""

            for ruta in extension:

                png = png + ruta 

            png = png + ".png"

            print(png)

            im = Image.open(imagen)

            im.save(png)

            im.close()

        else:

            print("El archivo ingresado no es una imagen...")
        
        system("cls")

    def Jpg(self):

        imagen = input("Arraste aqui la imagen para convertir: ")

        while True:

            try:

                if(imagen.endswith(".png") or imagen.endswith(".webp")):

                    rutas = ""

                    if imagen.endswith(".png"):

                        ruta = imagen.split(".png")

                    elif imagen.endswith(".webp"):

                        ruta = imagen.split(".webp")

                    jpg = ""

                    for ruta in rutas:

                        jpg = jpg + ruta 

                    jpg = jpg + ".jpg"

                    im = Image.open(imagen)

                    im.save(jpg)

                    im.close()

                    break
                else:
                    print("El archivo ingresado no es una imagen...")
                    sleep(15)
                    system("cls")
            except Exception as error:

                print(f"Error al convertir la imagen: %s" % error)
            
            system("cls")
    
    class mp3():

        def __init__(self):
            pass

        def oneFile(self):
            try:
                file = input("Arraste aqui el archivo: ")

                if file.endswith(".mp4"):

                    video = VideoFileClip(file)

                    sonido = video.audio

                    extension  = file.split('.mp4')[0]

                    mp3 = extension +".mp3"

                    sonido.write_audiofile(mp3) 

                    sonido.close()

                    video.close()
            except Exception as e:

                print(e)

        def multiFile():
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

            except Exception as e:

                print(e)


class compressor():

    def __init__(self):
        pass

    def Descompresor(self):

        while True:

            try:

                if(file.endswith('.rar')):

                    try:

                        file = input("Arraste aqui el archivo a descomprimir: ")

                        extract_archive(file)

                        break

                    except Exception as e:

                        print(e)

                        sleep(30)

                file = input("Arraste aqui el archivo a descomprimir: ")


                extract_archive(file)
                print("La extrasion a finalizado correctamente")
                sleep(15)
                system("cls")
                break

            except Exception as e:

                print(e)

                sleep(30)



    def Compresor(self):
        
        while True:

            try:

                file = input("Arraste aqui el archivo a comprimir: ")

                create_archive(file)

                print("La compresion a finalizado correctamente")

                sleep(15)

                system("cls")

                break

            except Exception as e:

                print(e)

class youlib():

    def videoHighResolution(self):

        while True:
            url = input("Ingrese la el link o la direccion url: ")
            try:

                if(url.startswith("https://www.youtube.com/watch?v=")):

                    yt = YouTube(url)

                    videos = yt.streams.get_highest_resolution()


                    videos.download("C:/Users/" + getlogin() + "/Downloads/")

                    print("La descarga del video es correcta..")

                    sleep(5)

                    system("cls")

                    break

                    
                else:

                    print("La direccion ingresada no es correcta")

            except Exception as error:

                print(f"Error al descargar un video {error}")

    
    def videoLowestResolution(self):

        while True:
            url = input("Ingrese la el link o la direccion url: ")
            try:

                if(url.startswith("https://www.youtube.com/watch?v=")):

                    yt = YouTube(url)

                    videos = yt.streams.get_lowest_resolution()

                    videos.download("C:/Users/" + getlogin() + "/Downloads/")

                    print("La descarga del video es correcta..")

                    sleep(15)

                    system("cls")

                    break

                else:

                    print("La direccion ingresada no es correcta")

            except Exception as error:
                
                print(f"Error al descargar un video {error}")

    def audio(self):
        while True:

            url = input("Ingrese la el link o la direccion url: ")
            
            try:

                if(url.startswith("https://www.youtube.com/watch?v=")):

                    chdir("C:/Users/" + getlogin() + "/Downloads/")

                    Path("Transformacion").mkdir(exist_ok=True)

                    yt = YouTube(url)

                    audio_streams  = yt.streams.get_lowest_resolution()

                    audio_streams.download("C:/Users/" + getlogin() + "/Downloads/Transformacion/")

                    chdir("C:/Users/" + getlogin() + "/Downloads/Transformacion/")

                    

                    for audio in listdir():

                        video = VideoFileClip(audio)

                        sonido = video.audio
                        
                        extension  = audio.split('.mp4')[0]
                        
                        mp3 = extension +".mp3"
                        
                        sonido.write_audiofile(mp3) 

                        sonido.close()
                        
                        video.close()
                    
                        move(mp3,"C:/Users/" + getlogin() + "/Downloads/")
                    
                    rmdir("C:/Users/" + getlogin() + "/Downloads/Transformacion")

                    print("La descarga del video es correcta..")

                    sleep(15)

                    system("cls")

                    break
                else:

                    print("La direccion ingresada no es correcta")
                    pass

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

class windows():

    libwindows = Windows()
    downloads = Download()

    def __init__(self):
        pass


    def activarw(self):
        self.libwindows.activadorwindow()
        system("cls")
    def activarO(self):
        try:
            self.libwindows.activadorOffices()
            system("cls")
        except Exception as e:
            input(e)
    def installofice(self):
        self.downloads.downloadOffice()
        self.activarO()
        system("cls")