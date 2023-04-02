class menu():

    def __init__(self):
        self.menu()

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
                *   4. Office y Windows                                                                           *
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
                    

                    break

                case "2":


                    break

                case "3":


                    break

                case "4":


                    break

                case "5":
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


                    break

                case "2":


                    break

                case "3":
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


                    break
                
                case "2":


                    break

                case "3":

                    break

                case _:
                    print(f"Esta opcion no existe{respuesta}")
                    
    def office(self):

        while True:

            print('''
                ********************************************** MENU DE OPCIONES ************************************
                * 1. Instalar office  y activarlo                                                                  *
                * 2. Activar office                                                                                *  
                * 3. Activar windows                                                                               *   
                *    4Salir                                                                                        *                                                                                                      
                ****************************************************************************************************
            ''')

            respuesta = input("Ingrese una opcion del menu: ")

            match respuesta:
                case "1":


                    break

                case "2":


                    break

                case "2":


                    break

                case "3":
                    break