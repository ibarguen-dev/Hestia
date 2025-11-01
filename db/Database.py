import sqlite3

class DataBase():

    """
    Clase que gestiona la base de datos para almacenar y recuperar configuraciones.
    """

    def __init__(self):

        """
        Constructor de la clase. Inicializa el objeto de base de datos (sqlite3).
        """

        self.dataBase = sqlite3


    def createDatabase(self):

        """
        Crea la estructura de la base de datos si no existe.

        Returns:
            int: 0 si la operación es exitosa, lista [1, mensaje de error] si hay un error.
        """

        connections = self.dataBase.connect("hestia.db")

        try:

            connections.execute("""CREATE TABLE configuraciones(
                color text,
                ubicacion text)
            """)
            return 0
        except self.dataBase.OperationalError as e:
            print(e)
            return [1,"Hubo un error al momento de crear la base de datos"]
        finally:
            connections.close()



    def inputData(self,color,ubicacion):

        """
        Ingresa datos de configuración en la base de datos.

        Args:
            color (str): El color a almacenar.
            ubicacion (str): La ubicación a almacenar.

        Returns:
            None
        """

        connections = self.dataBase.connect("hestia.db")
        try:
            connections.execute("INSERT INTO configuraciones VALUES (?,?)",(color,ubicacion))
            connections.commit()
        except self.dataBase.OperationalError as e:
            print(e)
            return [1,"Hubo un error al momento de ingresar los datos"]
        finally:
            connections.close()

    def returnData(self):

        """
        Retorna los datos de configuración almacenados en la base de datos.

        Returns:
            list: [0, dict] si la operación es exitosa, [1, mensaje de error] si hay un error.
        """

        listaDatos = {}
        connections = self.dataBase.connect("hestia.db")
        try:
            datos = connections.execute("SELECT * FROM configuraciones")

            for fila in datos:
                listaDatos = {"color":fila[0],"ubicacion":fila[1]}

            return [0, listaDatos]

        except self.dataBase.OperationalError as e:
            print(e)
            return [1, "Hubo un error al momento de ingresar los datos"]

        finally:
            connections.close()

    def updateData(self,color,ubicacion):

        """
         Actualiza los datos de configuración en la base de datos.

         Args:
             color (str): El nuevo color a almacenar.
             ubicacion (str): La nueva ubicación a almacenar.

         Returns:
             list: [0, mensaje] si la operación es exitosa, [1, mensaje de error] si hay un error.
         """

        connections = self.dataBase.connect("hestia.db")
        try:
            codigoActulizar = "UPDATE  configuraciones SET color = ?, ubicacion = ?"
            connections.execute(codigoActulizar,(color,ubicacion))

            connections.commit()
            return[0,"Los datos se hay actulizado"]

        except self.dataBase.OperationalError as e:

            print(e)

            return[1,"Hubo un error al momento de actulizar los datos "]

        finally:

            connections.close()
