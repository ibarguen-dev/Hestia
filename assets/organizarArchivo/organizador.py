from os import chdir, listdir, path, getlogin
from pathlib import Path
from shutil import move
from time import sleep 

class automa():

    def __init__ (self):

        pass

    def documnts(self):

        chdir("C:/Users/"+ getlogin() +"/Downloads")

        # 
        Path("PDF").mkdir(exist_ok=True)

        # 
        Path("Word").mkdir(exist_ok=True)

        # 
        Path("Imagenes y Videos").mkdir(exist_ok=True)

        # 
        Path("Excel").mkdir(exist_ok=True)

        # 
        Path("PowerPoint").mkdir(exist_ok=True)

        # 
        Path("Otros").mkdir(exist_ok=True)

        # 
        chdir("Imagenes y Videos/")

        #
        Path("Imagenes").mkdir(exist_ok=True)

        Path("Videos").mkdir(exist_ok=True)

  
   

    def files(self):

        chdir("C:/Users/" + getlogin() + "/Downloads/")
        
        for files in listdir():
            
            ruta = "C:/Users/" + getlogin() + "/Downloads/"
            
            
            # Documentos de word

            if files.endswith(".docx") or files.endswith(".docm") or files.endswith(".dotx") or files.endswith(".dotm"):
            
                chdir("C:/Users/" + getlogin() + "/Downloads/")
                
                if not path.exists(ruta+"Word/"+files):
                    
                    move(files, ruta+ "Word/")

                else:

                    print(f"El archivo {files} ya se encuentra en la carpeta de Word")

                    sleep(5)

            # Documentos de excel

            elif files.endswith(".xlsx") or files.endswith(".xlsm") or files.endswith(".xltx") or files.endswith(".xltm") or files.endswith("xlsb") or files.endswith("xlam"):

                chdir("C:/Users/" + getlogin() + "/Downloads/")
                
                if not path.exists(ruta + "Excel/"+files):
                
                    move(files, ruta + "Excel/")
                 
                else:



                    print(f"El archivo {files} ya se encuentra en la carpeta de Excel") 
                    
                    sleep(5)
            # Documentos de powrpoint
                    
            elif files.endswith(".pptx") or files.endswith(".pptm") or files.endswith(".potx") or files.endswith(".potm") or files.endswith(".ppam") or files.endswith(".ppsx") or files.endswith(".ppsm") or files.endswith(".sldx") or files.endswith(".sldm"):

                chdir("C:/Users/" + getlogin() + "/Downloads/")

                if not path.exists(ruta + "PowerPoint/"+files):

                    move(files, ruta + "PowerPoint/")
            
                else:

            
                    print(f"El archivo {files} ya se encuentra en la carpeta de PowerPoint")

                    sleep(5)

            #Imagenes


            elif files.endswith(".svg") or files.endswith(".jpg") or files.endswith(".png") or files.endswith(".gif") or files.endswith(".jpeg"):
            
                chdir("C:/Users/" + getlogin() + "/Downloads/")

                if not path.exists(ruta + "Imagenes y Videos/Imagenes/"+files):

                    print("entre")

                    move(files, ruta + "Imagenes y Videos/Imagenes/")
                 
                else:
                    print(f"El archivo {files} ya se encuentra en la carpeta de Imagen")

                    sleep(5)

            elif files.endswith(".mp4") or files.endswith(".avi") or files.endswith(".mov") or files.endswith(".flv") or files.endswith(".mkv") or files.endswith(".wmv"):

                    chdir("C:/Users/" + getlogin() + "/Downloads/")

                    if not path.exists(ruta + "Imagenes y Videos/Videos/"+files):
                
             
                        move(files, ruta + "Imagenes y Videos/Videos/")
                 
                    else:


                        print(f"El archivo {files} ya se encuentra en la carpeta de Videos")

                        sleep(5)
            
            # Archivos PDF 
                   
            elif files.endswith(".pdf"):
            
                chdir("C:/Users/" + getlogin() + "/Downloads/")

                if not path.exists(ruta + "PDF/"+files):    

                    move(files, ruta + "PDF/")
            
                else:



                    print(f"El archivo {files} ya se encuentra en la carpeta de PDF")

                    sleep(5)
            

            elif files != "Word" and files != "PDF" and files != "Imagenes y Videos" and files != "Excel" and files != "PowerPoint" and files != "Otros":

                chdir("C:/Users/" + getlogin() + "/Downloads/")
   
                move(files,ruta + "Otros")
                
            