from Modelo.modeloImagen import modeloImagen
from PIL import Image
from view.vistaAlerta import vistaAlerta
class controladorImagen():

    """
    Clase que gestiona la conversión de imágenes entre formatos (png y jpg).
    """

    def __init__(self):

        """
        Constructor de la clase. Inicializa instancias de otras clases y variables.
        """

        self.__modeloImagen = modeloImagen()
        self.__imagen = None
        self.__alertas = vistaAlerta()

    # metodo para la conversion de imagenes a png
    def png(self,rutas):

        """
        Método para convertir imágenes a formato PNG.

        Args:
            rutas (list): Lista de rutas de archivos de imagen a convertir.

        Returns:
            None
        """

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

    # metodo para la conversion de imagenes a jpg
    def jpg(self,rutas):

        """
        Método para convertir imágenes a formato JPG.

        Args:
            rutas (list): Lista de rutas de archivos de imagen a convertir.

        Returns:
            None
        """

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