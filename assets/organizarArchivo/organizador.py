from os import chdir, listdir, path, getlogin
from pathlib import Path
from shutil import move


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
        Path("Ejecutables").mkdir(exist_ok=True)

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

        #
        Path("Videos").mkdir(exist_ok=True)

        #
        
        #        

    def files(self):

        chdir("C:/Users/" + getlogin() + "/Downloads/")
        
        for files in listdir():
            #
            ruta = "C:/Users/" + getlogin() + "/Downloads/"
            
            if files.endswith(".docx") or files.endswith(".docm") or files.endswith(".dotx") or files.endswith(".dotm"):
            
                chdir("C:/Users/" + getlogin() + "/Downloads/")
                
                if not path.exists(ruta+"Word/"+files):
                    
                    move(files, ruta+ "Word/")
  
            elif files.endswith(".xlsx") or files.endswith(".xlsm") or files.endswith(".xltx") or files.endswith(".xltm") or files.endswith("xlsb") or files.endswith("xlam"):

                chdir("C:/Users/" + getlogin() + "/Downloads/")
                
                if not path.exists(ruta + "Execel/"+files):
                
                    move(files, ruta + "Execel/")

            elif files.endswith(".pptx") or files.endswith(".pptm") or files.endswith(".potx") or files.endswith(".potm") or files.endswith(".ppam") or files.endswith(".ppsx") or files.endswith(".ppsm") or files.endswith(".sldx") or files.endswith(".sldm"):

                chdir("C:/Users/" + getlogin() + "/Downloads/")

                if not path.exists(ruta + "PowerPoint/"+files):

                    move(files, ruta + "PowerPoint/")
  
            elif files.endswith(".svg") or files.endswith(".jpg") or files.endswith(".png") or files.endswith(".gif"):
            
                chdir("C:/Users/" + getlogin() + "/Downloads/")

                if not path.exists(ruta + "Imagenes y Videos/Imagenes/"+files):

                    move(files, ruta + "Imagenes y Videos/Imagenes/")

                
            elif files.endswith(".mp4") or files.endswith(".avi") or files.endswith(".mov") or files.endswith(".flv") or files.endswith(".mkv") or files.endswith(".wmv"):

                chdir("C:/Users/" + getlogin() + "/Downloads/")

                if not path.exists(ruta + "Imagenes y Videos/Videos/"+files):
                
                    move(files, ruta + "Imagenes y Videos/Videos/")

            #        
            elif files.endswith(".pdf"):
            
                chdir("C:/Users/" + getlogin() + "/Downloads/")

                if not path.exists(ruta + "PDF/"+files):    

                    move(files, ruta + "PDF/")

            
