from view.Vista import Vista
import os
from controlador.controladorConfiguraciones import Configuraciones

try:
    configuracionObjecto = Configuraciones()

    resultadoBaseDatos = configuracionObjecto.datosBaseDatos()

    if resultadoBaseDatos[0] == 0:
        aplicacion = os.getcwd()
        diccionarioDatos = resultadoBaseDatos[1].copy()

        vista = Vista(diccionarioDatos["color"], diccionarioDatos["ubicacion"],aplicacion)

        vista.iniciar_aplicacion()

    else:

        print("error")

except Exception as e:

    print(e)
