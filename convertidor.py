from pdf2docx import parse
from PIL import Image
from os import system
from time import sleep

def Pdf():
    while True:
        try:
            pdf = input("Arrastre aquí el PDF para convertir: ")
            if(pdf.endswith(".pdf")):
                rutas = pdf.split(".pdf")
                word =""
                for ruta in rutas:
                    word = word + ruta
                word = word + ".docx"
                parse(pdf,word, start=0, end=0)
                print("El archivo ya se ha convertido")
                break
            else:
               print("El archivo ingresado no es PDF")
               sleep(7)
               system("cls")
        except Exception as e:
            print(e)
            sleep(7)
            system("cls")
def Word():
    
    
    while True:
        word = input("Arrastre aquí el WORD para convertir: ")
        
        try:
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
                break
            else:
                print("El archivo ingresado no es WORD")
                sleep(7)
        except Exception as e:
            print(e)
            sleep(7)
            system("cls")
def Png():
    
    while True:
        try:
            imagen = input("Arrastre aquí la imagen para convertir: ")
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
                break
            else:
                print("El archivo ingresado no es una imagen...")
                sleep(7)
                system("cls")
        except Exception as e:
            print(e)
            sleep(7)
            system("cls")
def Jpg():

    

    while True:
        imagen = input("Arrastre aquí la imagen para convertir: ")
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
                sleep(7)
                system("cls")
        except Exception as error:
            print(f"Error al convertir la imagen: %s" % error)
            sleep(7)
            system("cls")