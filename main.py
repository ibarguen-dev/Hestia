
from automatizador import windows
from convertidor import pdfAWord,wordAPdf


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
                        *   1. Convertir de pdf a word o de word a pdf                                                    *
                        *   2. Comprimir y descomprimer rachivos                                                          *
                        ***************************************************************************************************   
    ''')









while True:
    try:
        windows()
        menu()
        respuesta = input("Ingrese un una opcion del menu: ")
        match respuesta:
            case "1":
                while True:
                    pdf = input("Ingrese uno  para 1 pdf a word o 2 para word a pdf: ")
                    match pdf:
                        case "1":
                            pdfAWord()
                            break
                        case "2":
                            wordAPdf()
                            break
                        case _:
                            print("La opncion ingresada no existe ")
            case "2":
                break
            case _:
                print("La opncion ingresada no existe")
            

    except Exception as e:
        print(e)





