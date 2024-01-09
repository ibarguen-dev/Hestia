from Modelo.modeloImagen import modeloImagen
from PIL import Image
from view.vistaAlerta import vistaAlerta
class controladorImagen():


    def __init__(self):
        self.__modeloImagen = modeloImagen()
        self.__imagen = None
        self.__alertas = vistaAlerta()
    def png(self,rutas):
        resultado = 0
        try:
            for ruta in rutas:
                self.__imagen = None

                nombre = self.__modeloImagen.verificar(ruta)

                nombre = nombre + ".png"

                self.__imagen = Image.open(ruta)

                self.__imagen.save(nombre)

                self.__imagen.close()


        except Exception as e:
            resultado = 1
            print(e)

        finally:
            self.__imagen.close()

            if resultado == 0:
                self.__alertas.informacion("las imagen se an convertido a png")
            else:
                self.__alertas.error("hubo un error al momento de convertir las imagenes")

    def jpg(self,rutas):

        resultado = 0

        try:
            for ruta in rutas:
                self.__imagen = None

                nombre = self.__modeloImagen.verificar(ruta)

                nombre = nombre + ".jpg"

                self.__imagen = Image.open(ruta)

                self.__imagen.save(nombre)

                self.__imagen.close()



        except Exception as e:
            resultado = 1
            print(e)

        finally:
            self.__imagen.close()

            if resultado == 0:
                self.__alertas.informacion("las imagen se an convertido a jpg")
            else:
                self.__alertas.error("hubo un error al momento de convertir las imagenes")