from os import system
from assets.convertidor.convertidores import convertidoresConfig

class ViewConvertidores():

    Config = convertidoresConfig()

    def __init__(self):
        self.Config
        pass

    def menuConvertidores(self):
                
        print('''
                ********************************************** MENU DE OPCIONES ************************************
                * 1. Convertir un PDF a un WORD o WORD a PDF                                                       *
                * 2. Convertir imagen                                                                              *
                * 3. Salir                                                                                         *                                                 
                ****************************************************************************************************
        ''')

        respuesta = input("Ingrese una opcion del menu : ")

        while True:

            match respuesta:
                case "1":

                    self.Config.files()

                case "2":

                    self.Config.imagenes()

                case "3":

                    system("cls")

                    break

                case _:

                    print (f"La opcion ingresada no existe {respuesta}")

            pas = input("Si deseas volver a menu principal ingrese [y] de lo contrario de enter: ")

            if pas == "y" or pas == "Y":

                break
            
            system("cls")