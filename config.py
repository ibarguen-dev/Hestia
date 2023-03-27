#Biblioteca de convertidores
from convertidor import Pdf, Word, Png, Jpg
#
from compresor import Descompresor
#
from libyoutebe import videoAltaResolucion, videoBajaResolucion
#
from time import sleep
def menu():
    print('''


            **************************************************************************************************
            *    8 8888        8 8 8888888888     d888888o. 8888888 8888888888 8 8888          .8.           *
            *    8 8888        8 8 8888         .`8888:' `88.     8 8888       8 8888         .888.          *
            *    8 8888        8 8 8888         8.`8888.   Y8     8 8888       8 8888        :88888.         *   
            *    8 8888        8 8 8888         `8.`8888.         8 8888       8 8888       . `88888.        *
            *    8 8888        8 8 888888888888  `8.`8888.        8 8888       8 8888      .8. `88888.       *
            *    8 8888        8 8 8888           `8.`8888.       8 8888       8 8888     .8`8. `88888.      *
            *    8 8888888888888 8 8888            `8.`8888.      8 8888       8 8888    .8' `8. `88888.     *
            *    8 8888        8 8 8888        8b   `8.`8888.     8 8888       8 8888   .8'   `8. `88888.    *
            *    8 8888        8 8 8888        `8b.  ;8.`8888     8 8888       8 8888  .888888888. `88888.   *
            *    8 8888        8 8 888888888888 `Y8888P ,88P'     8 8888       8 8888 .8'       `8. `88888.  * 
            ************************************************************************************************** 


                                                        

    ''')



    print('''
            ******************************************** MENU DE OPCIONES *************************************
            *   1. Convertidores                                                                              *
            *   2. Descomprimer archivos                                                          *
            *   3. Descargar videos de youtube                                                                *
            *   4. Cerrar la aplicación                                                                       *
            ***************************************************************************************************   
    ''')


def convertidores():

    print('''
            ********************************************** MENU DE OPCIONES ************************************
            * 1. Convertir un PDF a un WORD                                                                    *
            * 2. Convertir de WORD a PDF                                                                       *
            * 3. Convertir imagen a PNG                                                                        *
            * 4. Convertir imagen a JPG                                                                        *
            * 5. Salir                                                                                         *                                                 
            ****************************************************************************************************
    ''')

    respuesta = input("Ingrese una opción del menú: ")

    while True:
        match respuesta:

            case "1":

                Pdf()
                break

            case "2":

                Word()
                break

            case "3":

                Png()
                break

            case "4":

                Jpg()
                break

            case "5":

                break

            case _:
                print (f"La opción ingresa no existe, elija una de las opciones del menú")

def compresore ():




    while True:

        print('''
            ********************************************** MENU DE OPCIONES ************************************
            * 1. Comprimir                                                                                     *
            * 2. Salir                                                                                         *                              
            ****************************************************************************************************
        ''')

        respuestas = input('Ingrese una opción del menú: ')
        
        match respuestas:

            case "1":

                Descompresor()
                break

            case "2":

                break

            case _:
                print(f"La opción ingresa no existe, elija una de las opciones del menú")

def youtube ():

    while True:
        print('''
            ********************************************** MENÚ DE OPCIONES ************************************
            * 1. Video de alta resolución                                                                      *
            * 2. Video de baja resolución                                                                      *  
            * 3. Salir                                                                                         *                                                                                                         
            ****************************************************************************************************
        ''')

        respuesta = input("Ingrese una opción del menú: ")

        match  respuesta:
        
            case "1":
                videoAltaResolucion()
                break
            
            case "2":
                
                videoBajaResolucion()
                break

            case "3":
                break

            case _:
                print("La opción ingresa no existe, elija una de las opciones del menú")
                sleep(5)
                break