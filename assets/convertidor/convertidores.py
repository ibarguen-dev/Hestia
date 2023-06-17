from os import system

from time import sleep

from os import system

from time import sleep

from pdf2docx import parse

from docx2pdf  import convert

from PIL import Image


class convertidoresConfig():

    def __init__ (self):
        self.filesvalidations
        self.files
        self.imagenes
        
    

    def filesvalidations(self,file):

        files = ""
        print(file)
        organizar = file.split(" ")

        for i in organizar:

            files = files + i


        if files.endswith(".docx")  or files.endswith(".pdf"):

            rutas = ""

            if files.endswith(".docx"):

                rutas = files.split(".docx")[0]

            elif files.endswith(".pdf"):

                rutas = files.split(".pdf")[0]


                input(rutas)

            return rutas
        
        else:

            return False
        

    def files(self):
        
        
        while True:

            print('''
                ********************************************** ADVERTENCIA *****************************************
                * La aplicación solo puede convertir documentos de Word con extensión .docx                        *
                ****************************************************************************************************
            ''')

            print('''
                ********************************************** MENU DE OPCIONES ************************************
                * 1. Convertir PDF a WORD                                                                          *
                * 2. Convertir WORD a PDF                                                                          *
                ****************************************************************************************************
            ''')

            options = input("Ingresa una opcion: ")

            try:
                archivo = input("Arraste aqui el archivo que desea  convertir: ")

                respusta = self.filesvalidations(archivo)

                if respusta != False:

                    output =""

                    for ruta in respusta:

                        output = output + ruta

                    if options == "1":

                        output = output + ".docx"

                        parse(archivo,output, start=0, end=0)

                    elif options == "2":
                    
                        output = output + ".pdf"
                        convert(archivo,output)

                    print("El archivo ya se Ha convertido")

                    break
                
                else:
                
                    print("El archivo ingresado no se puede convertir") 

                system("cls")
            
            except Exception as e:

                input(e) 
                break
    

    def validadorImagen(self,imagen):

        if imagen.endswith(".jpg") or imagen.endswith(".webp") or imagen.endswith("jpeg") or  imagen.endswith(".gif") or imagen.endswith(".tiff") or imagen.endswith(".svg"):
           

            extension = ""

            if imagen.endswith(".jpg"):
                
                extension = imagen.split(".jpg")[0]
            
            elif imagen.endswith(".jpeg"):
                
                extension = imagen.split(".jpeg")[0]

            elif imagen.endswith(".webp"):

                extension = imagen.split(".webp")[0]

            elif imagen.endswith(".gif"):

                extension = imagen.split(".gif")[0]

            elif imagen.endswith(".tiff"):

                extension = imagen.split(".tiff")[0]

            elif imagen.endswith(".svg"):

                extension = imagen.split(".svg")[0]



            return extension
        
        else:

            return False

    def imagenes(self):

        while True:    
            try:

                print('''
                    ********************************************** MENU DE OPCIONES ************************************
                    * 1. convertir A PNG                                                                               *
                    * 2. convertir A JPG                                                                               *
                    ****************************************************************************************************
                ''')
                options = input("Ingrese una opción: ")
                if(options == "1" or options == "2"):
                    imagen = input("Arreste aquí la imagen que desea convertir: ")

                    resultados = self.validadorImagen(imagen)

                    if resultados != False:

                        file = "" 

                        for resultado in resultados:

                            file = file + resultado

                        if options == "1":

                            file = file + ".png"

                        elif options == "2":

                            file =  file + ".jpg"

                        im = Image.open(imagen)

                        im.save(file)

                        im.close()

                        print("La imagen se ha convertido")

                        sleep(5)

                        system("cls")

                        break
                    else:
                        print("El archivo ingresado no se puede convertir, por favor intente de nuevo")   
                else:
                    print("La opción ingresada no existe")   
                        

            except Exception as e:

                print(e)

