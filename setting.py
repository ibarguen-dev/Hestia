from db import Database
from download import Download
from os import getlogin
from time import sleep
class settings():

    descargas = Download()

    database = Database()

    def __init__(self):
        self.database
        self.user()
    def user(self):
        
        print("Cargando...")
        response = self.database.ReadUser()

        if(response == None):
        
            while True:
                
                response =  self.database.InsertUser(getlogin())
        
                if(response == True):

                    self.app()
                    break 
        elif(response == False):
            pass

    def app(self):
        try:
            verifiicar = Database()

            respuesta  = verifiicar.ReadSetting()

            if(respuesta == None):

                self.descargas.python()

                self.descargas.rar()

                self.database.InsertSettings("1","1")
            else:

                print("Todos los componetes listos...")

        except Exception as e:

            print("Error:", e)

hola = settings()

hola.user()