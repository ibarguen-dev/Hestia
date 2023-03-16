from pdf2docx import parse
from PIL import Image

class Convertido:

    def pdfAWord():
        pdf = input("Arraste aqui el pdf para convertir: ")
        if(pdf.endswith(".pdf")):
            rutas = pdf.split(".pdf")
            word =""
            for ruta in rutas:
                word = word + ruta
            word + ".docx"
            parse(pdf,word, start=0, end=0)
            print("el aechivo ya se a convertido")
        else:
           print("el archivo ingresado no es pdf") 

    def wordAPdf():
        word = input("Arraste aqui el word para convertir: ")
        if(word.endswith(".docx")):
            rutas = word.split(".docx")
            pdf = ""
            for ruta in rutas:
                pdf = pdf + ruta
            parse(word, pdf, start=0, end=0)
        else:
            print("el archivo ingresado no es word")
    


    def jpgApng():
        jpg = input("Arraste aqui el jpg para convertir: ")
        if(jpg.endswith(".jpg")):
            img_png = Image.open(jpg)
            ruta = ""
            for extension in jpg:
                ruta = ruta + extension
            ruta = ruta + ".png"
            img_png.save(ruta)
        else:
            print("La imagen ingresada no es JPG")


    def pngAjpg():
        jpg = input("Arraste aqui el jpg para convertir: ")
        if(jpg.endswith(".png")):
            img_png = Image.open(jpg)
            ruta = ""
            for extension in jpg:
                ruta = ruta + extension
            ruta = ruta + ".jpg"
            img_png.save(ruta)
        else:
            print("La imagen ingresada no es PNG")