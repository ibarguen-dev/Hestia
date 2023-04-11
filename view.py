from settings import setting, convert, compressor, youlib, automatization
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
                *   2. Comprimir y descomprimer archivos                                                          *
                *   3. Descargar videos de youtube                                                                *
                *   4. Organizar archivos                                                                         *
                *   5. Salir                                                                                      *
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

                    break

                case "2":

                    self.converts.Word()

                    break

                case "3":

                    self.converts.Png()

                    break

                case "4":

                    self.converts.Jpg()

                    break

                case "5":
                    system("cls")
                    break

                case _:

                    print (f"La opcion ingresada no existe {respuesta}")


    def compresore (self):

        while True:

            print('''
                ********************************************** MENU DE OPCIONES ************************************
                * 1. Comprimir                                                                                     *
                * 2. Extraer                                                                                       *
                * 3. Salir                                                                                         *                                          
                ****************************************************************************************************
            ''')

            respuestas = input('Ingrese una opcion del menu: ')

            match respuestas:
                case "1":

                    self.compresors.Compresor()

                    break

                case "2":

                    self.compresors.Descompresor()

                    break

                case "3":
                    system("cls")
                    break

                case _:
                    print(f"Esta opcion del menu no existe: {respuestas}")

    def youtube (self):

        while True:

            print('''
                ********************************************** MENU DE OPCIONES ************************************
                * 1. Video de alta resolucion                                                                      *
                * 2. Video de baja resolucion                                                                      *  
                * 3. Salir                                                                                         *                                                                                                      
                ****************************************************************************************************
            ''')

            respuesta = input("Ingrese una opcion del menu: ")

            match  respuesta:
            
                case "1":

                    self.youtubes.videoHighResolution()

                    break
                
                case "2":

                    self.youtubes.videoLowestResolution()

                    break

                case "3":
                    system("cls")
                    break

                case _:

                    print(f"Esta opcion no existe{respuesta}")

    def clean(self):

        self.automatizations.auto()       
