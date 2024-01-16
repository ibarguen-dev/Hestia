from pdf2docx import parse
from Modelo.modeloPdfWord import modeloPdfWord
from view.vistaAlerta import vistaAlerta
from docx2pdf  import convert

class controladorPdfWord():

    def __init__(self):

        self.__modeloPdfWord = modeloPdfWord()

        self.__vistaAlerta = vistaAlerta()

    # metodo para convertir los pdf a word convertidor
    def pdf(self,archivos):

        validador = 0

        try:

            for archivo in archivos:

                nombre = self.__modeloPdfWord.word(archivo)

                nombre = nombre + ".pdf"

                convert(archivo, nombre)

                del nombre

        except Exception as e:

            print(f"Hubo un error al convertir el pdf: {str(e)}")

            validador = 1

        finally:

            if validador == 0:
                self.__vistaAlerta.informacion("pdf convertido a word")
            else:
                self.__vistaAlerta.error("hubo un error al momento de convertir el pdf a word")


    # metodo para convertir los word a pdf
    def word(self,archivos):
        validador = 0
        try:

            for archivo in archivos:

                nombre = self.__modeloPdfWord.pdf(archivo)

                nombre = nombre + ".docx"

                parse(archivo,nombre, start=0, end=0)

                del nombre

        except Exception as e:

            print(f"Hubo un error al convertir el word: {str(e)}")
            validador = 1


        finally:

            if validador == 0:
                self.__vistaAlerta.informacion("pdf convertido a word")
            else:
                self.__vistaAlerta.error("hubo un error al momento de convertir el pdf a word")

