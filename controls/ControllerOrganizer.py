from os import chdir, listdir, path
from shutil import move
from time import sleep
import threading
class ControllerOrganizer():

    """
    Clase que organiza archivos en carpetas específicas según su tipo/formato.
    """

    def __init__(self,adress:str,page, show_error_callback, show_info_callback):

        """
        Constructor de la clase. Inicializa la ubicación y realiza la creación de carpetas.

        Args:
            ubicacion (str): La ubicación del directorio a organizar.
        """

        self.__adress = adress
        self.page = page
        self.show_error = show_error_callback
        self.show_info = show_info_callback

        
        
    def oraganizer(self):
        self.show_info("Organizando archivos...")
        oraganizer_thread = threading.Thread(target=self.file)
        oraganizer_thread.daemon = True
        oraganizer_thread.start()

    def file(self):
        
        """
        Método para organizar archivos en carpetas específicas según su tipo/formato.

        Returns:
            None
        """
        try:
            chdir(self.__adress)

            for files in listdir():
                ruta = self.__adress

                if files.endswith((".docx", ".docm", ".dotx", ".dotm")):
                    self.__move_file(files, ruta, "Word")

                elif files.endswith((".xlsx", ".xlsm", ".xltx", ".xltm", "xlsb", ".xlam")):
                    self.__move_file(files, ruta, "Excel")

                elif files.endswith((".pptx", ".pptm", ".potx", ".potm", ".ppam", ".ppsx", ".ppsm", ".sldx", ".sldm")):
                    self.__move_file(files, ruta, "PowerPoint")

                elif files.endswith((".svg", ".jpg", ".png", ".gif", ".jpeg")):
                    self.__move_file(files, ruta, "Imagenes y Videos/Imagenes")

                elif files.endswith((".mp4", ".avi", ".mov", ".flv", ".mkv", ".wmv")):
                    self.__move_file(files, ruta, "Videos")

                elif files.endswith(".mp3"):
                    self.__move_file(files, ruta, "Audios")

                elif files.endswith(".txt"):
                    self.__move_file(files, ruta, "Texto")

                elif files.endswith((".exe", ".msi")):
                    self.__move_file(files, ruta, "Ejecutables")

                elif files.endswith(".pdf"):
                    self.__move_file(files, ruta, "PDF")
                    
                elif files.endswith((".rar",".zip",".tar",".tar.gz",".tgz")):
                    self.__move_file(files, ruta, "Comprimidos")
                    
                elif files not in ["Word", "PDF", "Imagenes",  "Videos", "Excel", "PowerPoint", "Otros", "Ejecutables",
                                "Audios", "Texto","Comprimidos","Descomprimidos"]:
                    self.__move_file(files, ruta, "Otros")
            self.show_info("Los archivos fueron organizados")
        except Exception as e:
            print(e)
            self.show_error("Error al organizar archivos")


    def __move_file(self, filename, current_path, target_folder):
        """
        Método privado para mover un archivo a una carpeta específica.

        Args:
            filename (str): El nombre del archivo a mover.
            current_path (str): La ruta actual del archivo.
            target_folder (str): La carpeta de destino.

        Returns:
            None
        """
        try:
            chdir(current_path)

            target_path = path.join(current_path, target_folder, filename)

            if not path.exists(target_path):
                move(filename, target_path)
            else:
                print(f"El archivo {filename} ya se encuentra en la carpeta {target_folder}")
                sleep(5)

        except Exception as e:
            self.show_error("Error al organizar archivos")
            print(e)
