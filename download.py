
from os import getlogin, system,chdir,remove
from requests import get
from time import sleep

class Download():

    def __init__(self):
        pass

    def python(self):

        while True :

            try:

                chdir ('C:/Users/'+getlogin()+'/Downloads/')

                url = "https://www.python.org/ftp/python/3.11.3/python-3.11.3.exe"

                response = get(url)
                
                if response.status_code == 200:
                
                    try:

                        with open("python-3.11.3.exe", "wb") as f:
                        
                            f.write(response.content)

                            sleep(1)

                        system('"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" github.com')

                        system("C:/Users/"+ getlogin()+ "/Downloads/python-3.11.3.exe")

                        remove("C:/Users/"+ getlogin()+ "/Downloads/python-3.11.3.exe")

                        system("python.exe -m pip install --upgrade pip")

                        system("pip install patool")

                        system("pip install pdf2docx")

                        system("pip install Pillow")

                        system("pip install  pytube")

                        break
                    except Exception as e:

                        print("Error")

                        sleep(10)
                else:
                
                    print("Error al descargar ")

                    sleep(10)

            except Exception as e:
            
                print("Error : ", e)

                sleep(10)

    def rar(self):

        while True:

            try:

                chdir('C:/Users/'+getlogin()+'/Downloads/')

                url = "https://d.winrar.es/d/52z1680789825/C2bBY2XX4KRNNBxOCukymw/winrar-x32-621es.exe"

                response = get(url)

                if response.status_code == 200:

                    try:

                        with open("winrar-x32-621es.exe","wb") as f:

                            f.write(response.content)
                        
                        system("C:/Users/"+ getlogin()+ "/Downloads/winrar-x32-621es.exe")

                        remove("C:/Users/"+ getlogin()+ "/Downloads/winrar-x32-621es.exe")

                        break

                    except Exception as e:

                        print("Error :" + e)
            
            except Exception as e:

                print("Error :" + e)
