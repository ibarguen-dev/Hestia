from pdf2docx import parse

from docx2pdf  import convert

class PdfWord():

    def __init__(self):

        pass


    def pdf(self,nombre,archivo):
        try:
            archivoPdf = nombre + ".pdf"
            print(archivoPdf)
            print(archivo)
            convert("C:/Users/juane/Downloads/Cartadepresentacion.docx", "C:/Users/juane/Downloads/Cartadepresentacion.pdf")

            return [0,"El pdf creado"]
        except Exception as e:
            print(f"Hubo un error al convertir el pdf: {str(e)}")
            return  [1,f"Hubo un error al convertir el pdf: {str(e)}"]

        finally:

            del archivoPdf

    def word(self,nombre,archivo):
        try:
            archivoWord = nombre + ".docx"
            print("ok")
            parse(archivo,archivoWord, start=0, end=0)
            print("ok")
            return [0, "El pdf creado"]
        except Exception as e:
            print(f"Hubo un error al convertir el word: {str(e)}")
            return  [1,f"Hubo un error al convertir el word: {str(e)}"]

        finally:

            del archivoWord


