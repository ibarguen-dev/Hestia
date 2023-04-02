from requests import get
from time import sleep
from os import getlogin, system,chdir,remove

def app():
    try:
        #verifiicar = Database()
        #respuesta  = verifiicar.ReadSetting()
        #if(respuesta == None):
        try:
            chdir ('C:/Users/'+getlogin()+'/Downloads/')
            url = "https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe"
            response = get(url)
            if response.status_code == 200:
            
                # Guarda el archivo de video
                with open("python-3.11.2-amd64.exe", "wb") as f:
                
                    f.write(response.content)
                    print("Descargado con exito")
                    sleep(15)
                system("C:/Users/"+ getlogin()+ "/Downloads/python-3.11.2-amd64.exe")
                remove('python-3.11.2-amd64.exe')
            else:
            
                print("Error al descargar el video")
                sleep(12)
        except Exception as e:
        
            print("Error al office el video: ", e)
            sleep(12)
        #else:
            #print("ok")
    except Exception as e:
        print("Error:", e)

app()