from os import  getlogin
from  pathlib import Path
from  controlador.controladoDb import  BaseDatos

class Configuraciones():

    def __init__(self):
        self.baseDatos = BaseDatos()

        self.__validarBaseDatos()


    def __validarBaseDatos(self):

        if not Path("hestia.db").exists():

            print("no existe la base de datos")

            respuesta = self.baseDatos.crearBaseDatos()
            print(respuesta)
            if(respuesta[0] == 0):

                self.baseDatos.ingresarDatos("System","C:/Users/"+ getlogin() +"/Downloads")

        else:

            print("si existe la base datos")