from pdf2docx import parse
from PIL import Image



def pdfAWord():
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
       
def wordAPdf():
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