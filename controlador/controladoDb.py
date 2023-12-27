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
            return  [0,"La base de datos fue creada"]
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

        conexion = self.baseDatos.connect("hestia.db")
        try:
            Datos = conexion.execute("SELECT * FROM configuraciones")

            return [0, Datos]

        except self.baseDatos.OperationalError as e:
            print(e)
            return [1, "Hubo un error al momento de ingresar los datos"]

        finally:
            conexion.close()

    def actulizarDatos(self,color,ubicacion):
        conexion = self.baseDatos.connect("hestia.db")
        try:
            conexion.execute("UPDATE SET configuraciones VALUES (color = ?, ubicacion = ?)",(color,ubicacion))


            return[0,"Los datos se hay actulizado"]

        except self.baseDatos.OperationalError as e:

            print(e)

            return[1,"Hubo un error al momento de actulizar los datos "]

        finally:

            conexion.close()
