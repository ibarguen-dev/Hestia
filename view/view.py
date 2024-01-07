from view.viewConvertidores import ViewConvertidores
from view.viewYoutube import ViewYoutube
from assets.organizarArchivo.organizador import automa
class view():

    viewconvertidores = ViewConvertidores()
    viewyoutube = ViewYoutube()
    assetsorganizador = automa()
    def __init__(self):
        self.menu()
        self.viewconvertidores
        self.viewyoutube
        self.assetsorganizador.documnts()
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
                *   2. Descargar videos y audio de youtube                                                        *
                *   3. Organizar archivos                                                                         *
                *   4. Salir                                                                                      *
                ***************************************************************************************************   
        ''')

    def convertidores(self):
        
        self.viewconvertidores.menuConvertidores()
    
    def youtube(self):
        self.viewyoutube.videos()

    def organaizarArchivos(self):
        self.assetsorganizador.files()


