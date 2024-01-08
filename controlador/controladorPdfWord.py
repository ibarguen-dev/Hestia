from pdf2docx import parse
from Modelo.modeloPdfWord import modeloPdfWord
from view.vistaAlerta import vistaAlerta
from docx2pdf  import convert

class controladorPdfWord():

    def __init__(self):

        self.__modeloPdfWord = modeloPdfWord()

        self.__vistaAlerta = vistaAlerta()

    def pdf(self,archivos):
        validador = 0
        try:
            nombre = None

            for archivo in archivos:

                nombre = self.__modeloPdfWord.pdf(archivo)

                nombre = nombre + ".docx"

                convert(archivo, nombre, start=0, end=0)

        except Exception as e:

            print(f"Hubo un error al convertir el pdf: {str(e)}")

        finally:

            del nombre

            if validador == 0:
                self.__vistaAlerta.informacion("pdf convertido a word")
            else:
                self.__vistaAlerta.error("hubo un error al momento de convertir el pdf a word")

    def word(self,archivos):
        validador = 0
        try:
            nombre = None

            for archivo in archivos:

                nombre = self.__modeloPdfWord.pdf(archivo)

                nombre = nombre + ".docx"

                parse(archivo,nombre, start=0, end=0)




        except Exception as e:

            print(f"Hubo un error al convertir el word: {str(e)}")
            validador = 1


        finally:

            del nombre

            if validador == 0:
                self.__vistaAlerta.informacion("pdf convertido a word")
            else:
                self.__vistaAlerta.error("hubo un error al momento de convertir el pdf a word")

