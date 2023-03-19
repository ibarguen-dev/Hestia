from pdf2docx import parse
from PIL import Image
from os import system


def Pdf():
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
       
def Word():
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
#
def Png():
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
#

def Jpg():

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
                system("cls")
        except Exception as error:
            print(f"Error al convertir la imagen: %s" % error)