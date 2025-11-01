from pdf2docx import parse
from Model.ModelConvert import ModelConvert
from docx2pdf  import convert
import threading
class ControllerConvertFile():

    def __init__(self, page,  show_error_callback, show_info_callback):
        self.page = page
        self.show_error = show_error_callback
        self.show_info = show_info_callback
        self.__modelConvert = ModelConvert()

        

    # metodo para convertir los pdf a word convertidor
    def pdf(self,file):
        name = self.__modelConvert.verify_file_word(file)
        conversion_thread = threading.Thread(
            target=self._perform_word_to_pdf_threaded,
            args=(file,name)
        )
        conversion_thread.daemon = True
        conversion_thread.start()


    # metodo para convertir los word a pdf
    def word(self,file):
        name = self.__modelConvert.verify_file_pdf(file)
        conversion_thread = threading.Thread(
            target=self._perform_pdf_to_word_threaded,
            args=(file,name)
        )
        conversion_thread.daemon = True
        conversion_thread.start()
        

    def  _perform_word_to_pdf_threaded(self,file,name):
        validador = 0

        try:

            name = name + ".pdf"

            convert(file, name)

            del name

        except Exception as e:

            print(f"Hubo un error al convertir el pdf: {str(e)}")

            validador = 1

        finally:

            if validador == 0:
                self.page.run_task(self._notify_error("Error al convertir la imagen:"))
                print("Error en la conversión de imagen")
            else:
                self.page.run_task(self._notify_error("hubo un error al momento de convertir el pdf a word"))
    
    def  _perform_pdf_to_word_threaded(self,file,name):
        validador = 0
        try:

            name = self.__modelConvert.verify_file_pdf(file)

            name = name + ".docx"

            parse(file,name, start=0, end=0)

            del name

        except Exception as e:

            print(f"Hubo un error al convertir el word: {str(e)}")
            validador = 1


        finally:

            if validador == 0:
                self.page.run_task(self._notify_error("Error al convertir la imagen:"))
                print("Error en la conversión de imagen")
            else:
                self.page.run_task(self._notify_error("hubo un error al momento de convertir el pdf a word"))
    
    def _perform_image_to_pdf_threaded(self,file):
        pass
    
    async def _notify_success(self,text:str):
        """Función async para notificar éxito en el hilo principal"""
        self.show_info(text)

    async def _notify_error(self,text:str):
        """Función async para notificar error en el hilo principal"""
        self.show_error(text)