
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

                url = "https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe"

                response = get(url)
                
                if response.status_code == 200:
                
                    try:

                        with open("python-3.11.2-amd64.exe", "wb") as f:
                        
                            f.write(response.content)

                            sleep(1)

                        system('"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" github.com')

                        system("C:/Users/"+ getlogin()+ "/Downloads/python-3.11.2-amd64.exe")

                        remove("C:/Users/"+ getlogin()+ "/Downloads/python-3.11.2-amd64.exe")

                        break
                    except Exception as e:

                        print("Error :"+e)

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

                url = "https://download1496.mediafire.com/sk1en9twswmgd5k1GwShdW-6YrM5PTZMosqfX93mq1FwZ-GRdDh-8IaLmN29XUamhN31rC1_be8K1rGDI938WHSH_A4g7lo/hp5etmv70x4echi/winrar-x64-621es.exe"

                response = get(url)

                if response.status_code == 200:

                    try:

                        with open("winrar-x64-621es.exe","wb") as f:

                            f.write(response.content)
                        
                        system("C:/Users/"+ getlogin()+ "/Downloads/winrar-x64-621es.exe")

                        remove("C:/Users/"+ getlogin()+ "/Downloads/winrar-x64-621es.exe")

                        break

                    except Exception as e:

                        print("Error :" + e)
            
            except Exception as e:
                print("Error :" + e)