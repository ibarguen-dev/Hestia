from os import getlogin, chdir, listdir
from pathlib import Path
from shutil import move
from controls.ControllerDb import ControllerDb
from Model.ModelConfiguration import ModelConfiguration
from tkinter import messagebox

class ControllerSettings():

    """
    Clase que gestiona la configuración del programa, incluyendo la interacción con la base de datos.
    """

    def __init__(self):

        """
        Constructor de la clase. Inicializa instancias de otras clases y realiza validaciones iniciales.
        """

        self.__controllerDb = ControllerDb()
        self.__validateDatabase()
        self.__modelConfiguration = ModelConfiguration()
        self.__alerts = messagebox


    def __validateDatabase(self):

        """
        Método privado para validar la existencia de la base de datos al iniciar la aplicación.
        Crea la base de datos si no existe y realiza una inserción inicial.

        Returns:
            None
        """

        errores = 0

        try:
            if not Path("hestia.db").exists():

                print("no existe la base de datos")

                respuesta = self.__controllerDb.createDatabase()
                print(respuesta)
                if (respuesta == 0):
                    self.__controllerDb.inputData("System", "C:/Users/" + getlogin() + "/Downloads")


        except Exception as e:
            errores = 2
            print(e)

        finally:
            if errores == 2:
                messagebox.showerror("Error","Hubo un error al momento de crear la base de datos")


    def Database(self):

        """
        Método privado para validar la existencia de la base de datos al iniciar la aplicación.
        Crea la base de datos si no existe y realiza una inserción inicial.

        Returns:
            None
        """

        return self.__controllerDb.returnData()


    def inputData(self, ruta, rutavieja):

        """
        Método para cambiar la ruta del disco duro y actualizar la base de datos.

        Args:
            ruta (str): La nueva ruta a la que se deben mover los archivos.
            rutavieja (str): La ruta anterior que se utilizará para mover archivos de vuelta en caso de error.

        Returns:
            None
        """

        answer = None
        errores = 0
        try:
            answer = self.__modelConfiguration.validaciones(ruta)

            if answer:
                self.__controllerDb.updateData("System",ruta)
                chdir(rutavieja)
                for carpetas in listdir():
                    move(carpetas,ruta)
            else:
                errores =1
        except Exception as e:
            print(e)
            errores = 2

        finally:
            if errores == 0:
                self.__alerts.showinfo("Información", "Ruta guardad")
            else:
                self.__alerts.showerror("Error", "Hubo un error al momento de guardar la ruta")
