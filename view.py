from settings import *
from os import system
class menu():

    config = setting()

    converts = convert()

    compresors = compressor()

    youtubes = youlib()

    automatizations = automatization()


    def __init__(self):

        self.menu()

        self.config

    def menu(self):

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
                *   2. Descomprimer archivos                                                                      *
                *   3. Descargar videos y audio de youtube                                                        *
                *   4. Organizar archivos                                                                         *
                *   5. Office y windows                                                                           *
                *   6. Salir                                                                                      *
                ***************************************************************************************************   
        ''')

    def convertidores(self):

        print('''
                ********************************************** MENU DE OPCIONES ************************************
                * 1. Convertir un pdf a un word                                                                    *
                * 2. Convertir de word a pdf                                                                       *
                * 3. Convertir imagen a png                                                                        *
                * 4. Convertir imagen a jpg                                                                        *
                * 5. Salir                                                                                         *                                                 
                ****************************************************************************************************
        ''')
        
        respuesta = input("Ingrese una opcion del menu : ")

        while True:

            match respuesta:
                case "1":

                    self.converts.Pdf()

                case "2":

                    self.converts.Word()

                case "3":

                    self.converts.Png()

                case "4":

                    self.converts.Jpg()

                case "5":
                    system("cls")
                    break

                case _:

                    print (f"La opcion ingresada no existe {respuesta}")

            pas = input("Si deseas volver a menu principal ingrese y de lo contrario de enter: ")

            if pas == "y" or pas == "Y":

                break
            
            system("cls")


    def compresore (self):

        while True:

            print('''
                ********************************************** MENU DE OPCIONES ************************************
                * 1. Extraer                                                                                       *
                * 2. Salir                                                                                         *                                          
                ****************************************************************************************************
            ''')

            respuestas = input('Ingrese una opcion del menu: ')

            match respuestas:
                case "1":

                    self.compresors.Descompresor()
                case "2":
                    system("cls")
                    break

                case _:
                    print(f"Esta opcion del menu no existe: {respuestas}")

            pas = input("Si deseas volver a menu principal ingrese y de lo contrario de enter: ")

            if pas == "y" or pas == "Y":

                break
            
            system("cls")

    def youtube (self):

        while True:

            print('''
                ********************************************** MENU DE OPCIONES ************************************
                *   1. Video de alta resolucion                                                                    *
                *   2. Video de baja resolucion                                                                    *
                *   3  Descargar audio                                                                             *
                *   4. Salir                                                                                       *                                                                                                      
                ****************************************************************************************************
            ''')

            respuesta = input("Ingrese una opcion del menu: ")

            if respuesta == "3" or respuesta == "2" or respuesta == "1":

                self.youtubes.videoOrAudio(respuesta)
            
            elif respuesta == 4:
                system("cls")
                break
            
            else:
                print(f"Esta opcion no existe{respuesta}")

            pas = input("Ingrse Y se deseas volver al menu principal o de enter para continuarl con la opcion actual")

            if pas == "y" or pas == "Y":

                break

            system("cls")

    def clean(self):

        self.automatizations.auto()       

    def windowslib(self):

        libwindows = windows()
        
        print('''
        
            ********************************** MENU DE OPCIONES ******************************************
            *  1. Activar Windows                                                                        *
            *  2. Activar Office                                                                         *
            *  3. Intalar Office                                                                         *
            **********************************************************************************************
        ''')

        respuesta = input("Ingrese una opcion del menu: ")

        while True:
            
            match respuesta:
            
                case "1":
                
                    libwindows.activarw()
    
                    break
                
                case "2":
                
                    libwindows.activarO()
    
                    break
                
                case "3":
                
                    libwindows.installofice()
    
                    break
                
                case _:
                
                    print("La opcion ingresada no existe..")

            pas = input("Si deseas volver a menu principal ingrese y de lo contrario de enter: ")

            if pas == "y" or pas == "Y":

                break
            
            system("cls")
    


        

        