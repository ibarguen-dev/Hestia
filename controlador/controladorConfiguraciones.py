from os import getlogin, chdir, listdir
from pathlib import Path
from shutil import move
from controlador.controladoDb import BaseDatos
from Modelo.modeloConfiguracion import modeloConfiguracion
from tkinter import messagebox

class Configuraciones():

    """
    Clase que gestiona la configuración del programa, incluyendo la interacción con la base de datos.
    """

    def __init__(self):

        """
        Constructor de la clase. Inicializa instancias de otras clases y realiza validaciones iniciales.
        """

        self.__baseDatos = BaseDatos()
        self.__validarBaseDatos()
        self.__modeloConfiguracion = modeloConfiguracion()
        self.__alertas = messagebox


    def __validarBaseDatos(self):

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

                respuesta = self.__baseDatos.crearBaseDatos()
                print(respuesta)
                if (respuesta == 0):
                    self.__baseDatos.ingresarDatos("System", "C:/Users/" + getlogin() + "/Downloads")


        except Exception as e:
            errores = 2
            print(e)

        finally:
            if errores == 2:
                messagebox.showerror("Error","Hubo un error al momento de crear la base de datos")


    def datosBaseDatos(self):

        """
        Método privado para validar la existencia de la base de datos al iniciar la aplicación.
        Crea la base de datos si no existe y realiza una inserción inicial.

        Returns:
            None
        """

        return self.__baseDatos.devolverDatos()


    def ingresarDatos(self, ruta, rutavieja):

        """
        Método para cambiar la ruta del disco duro y actualizar la base de datos.

        Args:
            ruta (str): La nueva ruta a la que se deben mover los archivos.
            rutavieja (str): La ruta anterior que se utilizará para mover archivos de vuelta en caso de error.

        Returns:
            None
        """

        respusta = None
        errores = 0
        try:
            respusta = self.__modeloConfiguracion.validaciones(ruta)

            if respusta:
                self.__baseDatos.actulizarDatos("System",ruta)
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
                messagebox.showinfo("Información", "Ruta guardad")
            else:
                messagebox.showerror("Error", "Hubo un error al momento de guardar la ruta")
