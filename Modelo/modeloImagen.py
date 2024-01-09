

class modeloImagen():

    def __init__(self):
        pass

    def verificar(self,ruta):
        nombre = None

        try:

            if ruta.endswith(".png"):
                nombre = ruta.split(".png")[0]
            elif ruta.endswith(".jpeg"):
                nombre = ruta.split(".jpeg")[0]
            elif ruta.endswith(".jpg"):
                nombre = ruta.split(".jpg")[0]
            elif ruta.endswith(".svg"):
                nombre = ruta.split(".svg")[0]

            return nombre
        except Exception as e:

            print(e)
        finally:
            del nombre