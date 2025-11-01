from os import chdir
from pathlib import Path
from controls.ControllerDb import ControllerDb
from controls.ControllerOrganizer import ControllerOrganizer

class ControllerBoot:
    
    
    def __init__(self,):
        self._dataBase = ControllerDb()
        
        

    def folders(self,address):
        """
        Método privado para crear las carpetas necesarias en el directorio de organización.

        Returns:
            None
        """

        try:
            if address != "":
                chdir(address)
                Path("PDF").mkdir(exist_ok=True)
                Path("Word").mkdir(exist_ok=True)
                Path("Imagenes").mkdir(exist_ok=True)
                Path("Excel").mkdir(exist_ok=True)
                Path("PowerPoint").mkdir(exist_ok=True)
                Path("Otros").mkdir(exist_ok=True)
                Path("Audios").mkdir(exist_ok=True)
                Path("Texto").mkdir(exist_ok=True)
                Path("Ejecutables").mkdir(exist_ok=True)
                Path("Videos").mkdir(exist_ok=True)
                Path("Comprimidos").mkdir(exist_ok=True)
                Path("Descomprimidos").mkdir(exist_ok=True)
                
        except Exception as e:
            print(e)
            
        finally:
            pass
