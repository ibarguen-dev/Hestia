from os import chdir, listdir, path, getlogin
from pathlib import Path
from shutil import move
from time import sleep
from view import vistaAlerta

class controladorOrganizador():

    """
    Clase que organiza archivos en carpetas específicas según su tipo/formato.
    """

    def __init__(self,ubicacion):

        """
        Constructor de la clase. Inicializa la ubicación y realiza la creación de carpetas.

        Args:
            ubicacion (str): La ubicación del directorio a organizar.
        """

        self.__direccion = ubicacion
        self.__carpetas()
        self.__alertas = vistaAlerta.vistaAlerta()

    def __carpetas(self):

        """
        Método privado para crear las carpetas necesarias en el directorio de organización.

        Returns:
            None
        """

        try:
            chdir(self.__direccion)
            Path("PDF").mkdir(exist_ok=True)
            Path("Word").mkdir(exist_ok=True)
            Path("Imagenes y Videos").mkdir(exist_ok=True)
            Path("Excel").mkdir(exist_ok=True)
            Path("PowerPoint").mkdir(exist_ok=True)
            Path("Otros").mkdir(exist_ok=True)
            Path("Audios").mkdir(exist_ok=True)
            Path("Texto").mkdir(exist_ok=True)
            Path("Ejecutables").mkdir(exist_ok=True)
            chdir("Imagenes y Videos/")
            Path("Imagenes").mkdir(exist_ok=True)
            Path("Videos").mkdir(exist_ok=True)



        except Exception as e:
            self.__alertas.error(e)

    def archivos(self):
        """
        Método para organizar archivos en carpetas específicas según su tipo/formato.

        Returns:
            None
        """
        try:
            chdir(self.__direccion)

            for files in listdir():
                ruta = self.__direccion

                if files.endswith((".docx", ".docm", ".dotx", ".dotm")):
                    self.__mover_archivo(files, ruta, "Word")

                elif files.endswith((".xlsx", ".xlsm", ".xltx", ".xltm", "xlsb", ".xlam")):
                    self.__mover_archivo(files, ruta, "Excel")

                elif files.endswith((".pptx", ".pptm", ".potx", ".potm", ".ppam", ".ppsx", ".ppsm", ".sldx", ".sldm")):
                    self.__mover_archivo(files, ruta, "PowerPoint")

                elif files.endswith((".svg", ".jpg", ".png", ".gif", ".jpeg")):
                    self.__mover_archivo(files, ruta, "Imagenes y Videos/Imagenes")

                elif files.endswith((".mp4", ".avi", ".mov", ".flv", ".mkv", ".wmv")):
                    self.__mover_archivo(files, ruta, "Imagenes y Videos/Videos")

                elif files.endswith(".mp3"):
                    self.__mover_archivo(files, ruta, "Audios")

                elif files.endswith(".txt"):
                    self.__mover_archivo(files, ruta, "Texto")

                elif files.endswith((".exe", ".msi")):
                    self.__mover_archivo(files, ruta, "Ejecutables")

                elif files.endswith(".pdf"):
                    self.__mover_archivo(files, ruta, "PDF")

                elif files not in ["Word", "PDF", "Imagenes y Videos", "Excel", "PowerPoint", "Otros", "Ejecutables",
                                   "Audios", "Texto"]:
                    self.__mover_archivo(files, ruta, "Otros")

            self.__alertas.informacion("Los archivos fueron organizados")

        except Exception as e:
            self.__alertas.error(e)


    def __mover_archivo(self, filename, current_path, target_folder):
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
            self.__alertas.error(e)
