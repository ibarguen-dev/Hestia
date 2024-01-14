import sqlite3

class BaseDatos():

    """
    Clase que gestiona la base de datos para almacenar y recuperar configuraciones.
    """

    def __init__(self):

        """
        Constructor de la clase. Inicializa el objeto de base de datos (sqlite3).
        """

        self.baseDatos = sqlite3


    def crearBaseDatos(self):

        """
        Crea la estructura de la base de datos si no existe.

        Returns:
            int: 0 si la operación es exitosa, lista [1, mensaje de error] si hay un error.
        """

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

        """
        Ingresa datos de configuración en la base de datos.

        Args:
            color (str): El color a almacenar.
            ubicacion (str): La ubicación a almacenar.

        Returns:
            None
        """

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

        """
        Retorna los datos de configuración almacenados en la base de datos.

        Returns:
            list: [0, dict] si la operación es exitosa, [1, mensaje de error] si hay un error.
        """

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

        """
         Actualiza los datos de configuración en la base de datos.

         Args:
             color (str): El nuevo color a almacenar.
             ubicacion (str): La nueva ubicación a almacenar.

         Returns:
             list: [0, mensaje] si la operación es exitosa, [1, mensaje de error] si hay un error.
         """

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
