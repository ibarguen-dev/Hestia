from view.Vista import Vista

from controlador.controladorConfiguraciones import Configuraciones


try:

    configuracionObjecto = Configuraciones()

    resultadoBaseDatos  = configuracionObjecto.datosBaseDatos()

    if(resultadoBaseDatos[0] == 0):

        diccionarioDatos = resultadoBaseDatos[1].copy()

        vista = Vista(diccionarioDatos["color"],diccionarioDatos["ubicacion"])

        vista.iniciar_aplicacion()

    else:

        print("error")

except Exception as e:

    print(e)

