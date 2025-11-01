import flet as ft
import os
from view.view import HestiaApp
from controls.ControllerSettings import ControllerSettings
from controls.ControllerBoot import ControllerBoot
try:
     # Instancia de nuestra clase de aplicación
    controllerSettings = ControllerSettings()
    controllerBoot = ControllerBoot()
    thema = "SYSTEM"


    # Obtener datos de configuración de la base de datos
    databaseResult = controllerSettings.Database()

    # Verificar si la obtención de datos de la base de datos fue exitosa
    if databaseResult[0] == 0:
        # Obtener la ruta actual de la aplicación
        addres = os.getcwd()

        # Crear una copia del diccionario de datos de configuración
        dictionaryData = databaseResult[1].copy()

        # Crear una instancia de la clase Vista con los datos de configuración
        # vista = Vista(diccionarioDatos["color"], diccionarioDatos["ubicacion"],aplicacion)
        
        controllerBoot.folders("C:/Users/" + os.getlogin() + "/Downloads")
        def main(page: ft.Page):
            
            app = HestiaApp(page,dictionaryData["ubicacion"])
            
        # Iniciar la aplicación utilizando la vista creada
        ft.app(target=main)
        
    else:

        # Mostrar un mensaje de error si no se pueden obtener los datos de la base de datos
        print("error no se encontro ninguna información")

        # Se ingresa los datos a las bases de datos
        controllerSettings.inputData(thema, "C:/Users/" + os.getlogin() + "/Downloads")
        controllerBoot.folders("C:/Users/" + os.getlogin() + "/Downloads")
        # Obtener la ruta actual de la aplicación
        address = os.getcwd()

        # Crear una copia del diccionario de datos de configuración
        diccionarioDatos = databaseResult[1].copy()

        # Crear una instancia de la clase Vista con los datos de configuración
        # vista = Vista(diccionarioDatos["color"], diccionarioDatos["ubicacion"],aplicacion)

except ImportError:
    print("Flet is not installed. Please install it using 'pip install flet'.")