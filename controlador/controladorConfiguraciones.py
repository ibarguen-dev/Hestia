from os import getlogin, chdir, listdir
from pathlib import Path
from shutil import move
from controlador.controladoDb import BaseDatos
from Modelo.modeloConfiguracion import modeloConfiguracion
from tkinter import messagebox

class Configuraciones():

    def __init__(self):
        self.__baseDatos = BaseDatos()

        self.__validarBaseDatos()

        self.__modeloConfiguracion = modeloConfiguracion()

        self.__alertas = messagebox

    def __validarBaseDatos(self):
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

        return self.__baseDatos.devolverDatos()

    def ingresarDatos(self, ruta, rutavieja):
        respusta = None
        errores = 0
        try:
            respusta = self.__modeloConfiguracion.validaciones(ruta)

            if respusta:
                self.__baseDatos.actulizarDatos("System",ruta)
                chdir(rutavieja)
                #for carpetas in listdir():
                    #move(carpetas,ruta)
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
