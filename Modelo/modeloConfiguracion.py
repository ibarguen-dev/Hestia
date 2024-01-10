import re


class modeloConfiguracion():

    def __init__(self):
        pass

    def validaciones(self, ruta):

        try:
            patron = r'^[cC-zZ]:/(?:[^/:]+/)*[^/:]+$'
            return bool(re.match(patron, ruta))
        except Exception as e:
            print(e)
        finally:
            pass
