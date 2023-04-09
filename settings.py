from db import Database

from download import Download

from os import getlogin, system

from time import sleep

from validations import validation

from pdf2docx import parse

from PIL import Image

from patoolib import extract_archive, create_archive

from pytube import YouTube

class setting():

    descargas = Download()

    database = Database()

    disks = validation()

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

                    self.app()

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

                    self.app()

                else:

                    print(response)

                    input()
            else:
                print(response)

                input()            

            

    def app(self):

        try:

            respuesta  = self.database.ReadSetting()

            if(respuesta == None):

                self.descargas.python()

                self.descargas.rar()

                self.ruta()

                self.database.InsertSettings("1","1")

            elif respuesta == Exception:

                print(respuesta)

            else:

                print("Todos los componentes listos...")

        except Exception as e:

            print("Error:", e)
    
    def ruta(self):
        respuesta = input("Quieres que HESTIA pase tus archivos a otros discos. Ingrese 1 para sí, o enter para no: ")

        if respuesta == "1":

            ruta = input("Ingrese la letra del disco a utilizar: ").upper()

            response = self.disks.disk(ruta)

            if response.endswith(":/"):

                response = self.database.InsertAddres(response)

                if(response == "True"):

                    print("Ruta guardad...")
                    
                    sleep(10) 

                else:

                    print(response)

            else: print("Response")           
        else:

            response = self.disks.disk("C")
        

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
    
        try:

            file = input("Arraste aqui el archivo a comprimir: ")
                
            create_archive(file)

            print("La compresion a finalizado correctamente")

            sleep(15)

            system("cls")

        except Exception as e:
                
            print(e)


class youlib():

    def videoHighResolution(self):

        url = input("Ingrese la el link o la direccion url: ")

        while True:

            try:

                if(url.startswith("https://www.youtube.com/watch?v=")):

                    yt = YouTube(url)

                    videos = yt.streams.get_highest_resolution()


                    videos.download("C:/Users/" + getlogin() + "/Downloads/")

                    print("La descarga del video es correcta..")

                    sleep(15)

                    system("cls")

                    break

                    
                else:

                    print("La direccion ingresada no es correcta")

            except Exception as error:

                print(f"Error al descargar un video {error}")

    
    def videoLowestResolution(self):

        url = input("Ingrese la el link o la direccion url: ")

        while True:

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
    
