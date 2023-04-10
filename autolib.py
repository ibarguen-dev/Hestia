from os import chdir, listdir, path, getlogin
from pathlib import Path
from shutil import move
from patoolib import extract_archive


class automa():

    def __init__ (self):

        pass

    def documnts(self, path):

        chdir(path)

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
        chdir("C:/Users/" + getlogin() + "/Downloads/")
        #        

        for files in listdir():
            #
            if files.endswith(".docx") or files.endswith(".docm") or files.endswith(".dotx") or files.endswith(".dotm"):
            
                chdir("C:/Users/" + getlogin() + "/Downloads/")
                    #
                move(files, path+ "Word/")
  
            elif files.endswith(".xlsx") or files.endswith(".xlsm") or files.endswith(".xltx") or files.endswith(".xltm") or files.endswith("xlsb") or files.endswith("xlam"):

                chdir("C:/Users/" + getlogin() + "/Downloads/")


                move(files, path + "PowerPoint/")

            elif files.endswith(".pptx") or files.endswith(".pptm") or files.endswith(".potx") or files.endswith(".potm") or files.endswith(".ppam") or files.endswith(".ppsx") or files.endswith(".ppsm") or files.endswith(".sldx") or files.endswith(".sldm"):

                chdir("C:/Users/" + getlogin() + "/Downloads/")

                move(files, path + "PowerPoint/")
  
            elif files.endswith(".svg") or files.endswith(".jpg") or files.endswith(".png") or files.endswith(".gif"):
            
                chdir("C:/Users/" + getlogin() + "/Downloads/")
                    #
                move(files, path + "Imagenes y Videos/Imagenes/")

                
            elif files.endswith(".mp4") or files.endswith(".avi") or files.endswith(".mov") or files.endswith(".flv") or files.endswith(".mkv") or files.endswith(".wmv"):

                chdir("C:/Users/" + getlogin() + "/Downloads/")
                    #
                move(files, path + "Imagenes y Videos/Videos/")

            #        
            elif files.endswith(".pdf"):
            
                chdir("C:/Users/" + getlogin() + "/Downloads/")
                    #
                move(files, path + "PDF/")

            else:
            
                chdir("C:/Users/" + getlogin() + "/Downloads/")
                    #
                move(files, path + "Otros/")

