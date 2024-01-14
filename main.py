from view.Vista import Vista
import os
from controlador.controladorConfiguraciones import Configuraciones

try:
    # Crear una instancia de la clase Configuraciones
    configuracionObjecto = Configuraciones()

    # Obtener datos de configuración de la base de datos
    resultadoBaseDatos = configuracionObjecto.datosBaseDatos()

    # Verificar si la obtención de datos de la base de datos fue exitosa
    if resultadoBaseDatos[0] == 0:

        # Obtener la ruta actual de la aplicación
        aplicacion = os.getcwd()

        # Crear una copia del diccionario de datos de configuración
        diccionarioDatos = resultadoBaseDatos[1].copy()

        # Crear una instancia de la clase Vista con los datos de configuración
        vista = Vista(diccionarioDatos["color"], diccionarioDatos["ubicacion"],aplicacion)

        # Iniciar la aplicación utilizando la vista creada
        vista.iniciar_aplicacion()

    else:
        # Mostrar un mensaje de error si no se pueden obtener los datos de la base de datos
        print("error no se encontro ninguna información")

        # Se ingresa los datos a las bases de datos
        configuracionObjecto.ingresarDatos("System", "C:/Users/" + os.getlogin() + "/Downloads")

        # Obtener la ruta actual de la aplicación
        aplicacion = os.getcwd()

        # Crear una copia del diccionario de datos de configuración
        diccionarioDatos = resultadoBaseDatos[1].copy()

        # Crear una instancia de la clase Vista con los datos de configuración
        vista = Vista(diccionarioDatos["color"], diccionarioDatos["ubicacion"],aplicacion)

        # Iniciar la aplicación utilizando la vista creada
        vista.iniciar_aplicacion()

except Exception as e:
    # Capturar y mostrar cualquier excepción ocurrida durante la ejecución
    print(e)
