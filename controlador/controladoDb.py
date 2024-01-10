import sqlite3

class BaseDatos():

    def __init__(self):

        self.baseDatos = sqlite3


    def crearBaseDatos(self):
        conexion = self.baseDatos.connect("hestia.db")

        try:

            conexion.execute("""CREATE TABLE configuraciones(
                color text,
                ubicacion text)
            """)
            return 0
        except self.baseDatos.OperationalError as e:
            print(e)
            return [1,"Hubo un error al momento de crear la base de datos"]
        finally:
            conexion.close()



    def ingresarDatos(self,color,ubicacion):
        conexion = self.baseDatos.connect("hestia.db")
        try:
            conexion.execute("INSERT INTO configuraciones VALUES (?,?)",(color,ubicacion))
            conexion.commit()
        except self.baseDatos.OperationalError as e:
            print(e)
            return [1,"Hubo un error al momento de ingresar los datos"]
        finally:
            conexion.close()

    def devolverDatos(self):
        listaDatos = {}
        conexion = self.baseDatos.connect("hestia.db")
        try:
            datos = conexion.execute("SELECT * FROM configuraciones")

            for fila in datos:
                listaDatos = {"color":fila[0],"ubicacion":fila[1]}

            return [0, listaDatos]

        except self.baseDatos.OperationalError as e:
            print(e)
            return [1, "Hubo un error al momento de ingresar los datos"]

        finally:
            conexion.close()

    def actulizarDatos(self,color,ubicacion):
        conexion = self.baseDatos.connect("hestia.db")
        try:
            codigoActulizar = "UPDATE  configuraciones SET color = ?, ubicacion = ?"
            conexion.execute(codigoActulizar,(color,ubicacion))

            conexion.commit()
            return[0,"Los datos se hay actulizado"]

        except self.baseDatos.OperationalError as e:

            print(e)

            return[1,"Hubo un error al momento de actulizar los datos "]

        finally:

            conexion.close()
