
from os import chdir, listdir, path, getlogin
from pathlib import Path
from shutil import move
from patoolib import extract_archive

def windows():
    # verifica si la ruta docuemtos no existe 
    if not path.exists("C:/Users/" + getlogin() + "/Documentos"):
        # se dirige a la ruta Docuemets
        chdir("C:/Users/" + getlogin() + "/Documents/")
    #
    else:
        # se dirigie a la ruta Docuemtos
        chdir("C:/Users/" + getlogin() + "/Documentos/")
    
    
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
        if files.endswith(".rar") or files.endswith(".zip") or files.endswith(".7z"):
            #
            try:
                extract_archive(files)
            except Exception as e:
                print(e)
    #        
    rutadocumentos = ""
    #
    if not path.exists("C:/Users/" + getlogin() + "/Documentos"):
        #
        rutadocumentos = "/Documents/"
        #
    #
    else:
        #
        rutadocumentos = "/Documentos/"
    #
    for files in listdir():
        #
        if files.endswith(".docx") or files.endswith(".docm") or files.endswith(".dotx") or files.endswith(".dotm"):
        
            #
            chdir("C:/Users/" + getlogin() + rutadocumentos + "PowerPoint/")
            #
            if not path.exists(files):
            
                #
                chdir("C:/Users/" + getlogin() + "/Downloads/")
                #
                move(files, "C:/Users/" + getlogin() + rutadocumentos + "Word/")

            #
            else:
            
                #
                print("Error el archivo ya existe")
        #        
        elif files.endswith(".xlsx") or files.endswith(".xlsm") or files.endswith(".xltx") or files.endswith(".xltm") or files.endswith("xlsb") or files.endswith("xlam"):
            
            #
            chdir("C:/Users/" + getlogin() + rutadocumentos + "PowerPoint/")

            #
            if not path.exists(files):
            
            
                #
                chdir("C:/Users/" + getlogin() + "/Downloads/")

                #
                move(files, "C:/Users/" + getlogin() + rutadocumentos + "PowerPoint/")

            #
            else:
            
            
                #
                print("El archivo ya existe")

        #
        elif files.endswith(".pptx") or files.endswith(".pptm") or files.endswith(".potx") or files.endswith(".potm") or files.endswith(".ppam") or files.endswith(".ppsx") or files.endswith(".ppsm") or files.endswith(".sldx") or files.endswith(".sldm"):
            
            
            chdir("C:/Users/" + getlogin() + rutadocumentos + "PowerPoint/")
            
            if not path.exists(files):
            
                
                chdir("C:/Users/" + getlogin() + "/Downloads/")
                
                move(files, "C:/Users/" + getlogin() + rutadocumentos + "PowerPoint/")
            
            else:
            
                print("El archivo ya existe")
        #        
        elif files.endswith(".svg") or files.endswith(".jpg") or files.endswith(".png") or files.endswith(".gif"):
        
        
            chdir("C:/Users/" + getlogin() + rutadocumentos + "Imagenes y Videos/Imagenes/")
            #
            if not path.exists(files):
            
                #
                chdir("C:/Users/" + getlogin() + "/Downloads/")
                #
                move(files, "C:/Users/" + getlogin() + rutadocumentos + "Imagenes y Videos/Imagenes/")
            #
            else:
            
                #
                print("El archivo ya existe")
        #        
        elif files.endswith(".mp4") or files.endswith(".avi") or files.endswith(".mov") or files.endswith(".flv") or files.endswith(".mkv") or files.endswith(".wmv"):
            
            #
            chdir("C:/Users/" + getlogin() + rutadocumentos + "Imagenes y Videos/Videos/")
            #
            if not path.exists(files):
            
                #
                chdir("C:/Users/" + getlogin() + "/Downloads/")
                #
                move(files, "C:/Users/" + getlogin() + rutadocumentos + "Imagenes y Videos/Videos/")
            #    
            else:
            
                #
                print("El archivo ya existe")
        #        
        elif files.endswith(".pdf"):
        
        
            #
            chdir("C:/Users/" + getlogin() + rutadocumentos + "/PDF/")
            #
            if not path.exists(files):
            
                #
                chdir("C:/Users/" + getlogin() + "/Downloads/")
                #
                move(files, "C:/Users/" + getlogin() + rutadocumentos + "PDF/")
            #    
            else:
            
                #
                print("El archivo ya existe")
        else:
        
            #
            chdir("C:/Users/" + getlogin() + rutadocumentos + "/Otros/")
            #
            if not path.exists(files):
            
                #
                chdir("C:/Users/" + getlogin() + "/Downloads/")
                #
                move(files, "C:/Users/" + getlogin() + rutadocumentos + "Otros/")
            
            else:
            
                #
                print("El archivo ya existe")
