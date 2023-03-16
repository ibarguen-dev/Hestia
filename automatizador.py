import os
from pathlib import Path
from shutil import move




def windows():
    # verifica si la ruta docuemtos no existe 
    if not os.path.exists("C:/Users/" + os.getlogin() + "/Documentos"):
        # se dirige a la ruta Docuemets
        os.chdir("C:/Users/" + os.getlogin() + "/Documents/")
    #
    else:
        # se dirigie a la ruta Docuemtos
        os.chdir("C:/Users/" + os.getlogin() + "/Documentos/")
    
    
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
    os.chdir("Imagenes y Videos/")
    
    #
    Path("Imagenes").mkdir(exist_ok=True)
    
    #
    Path("Videos").mkdir(exist_ok=True)
    
    #
    os.chdir("C:/Users/" + os.getlogin() + "/Downloads/")
    #

    '''for files in os.listdir():
        #
        if files.endswith(".rar") or files.endswith(".zip") or files.endswith(".7z"):
            #
            Compresor.DescompresorHestia(files)
    '''#        
    rutadocumentos = ""
    #
    if not os.path.exists("C:/Users/" + os.getlogin() + "/Documentos"):
        #
        rutadocumentos = "/Documents/"
        #
    #
    else:
        #
        rutadocumentos = "/Documentos/"
    #
    for files in os.listdir():
        #
        if files.endswith(".docx") or files.endswith(".docm") or files.endswith(".dotx") or files.endswith(".dotm"):
        
            #
            os.chdir("C:/Users/" + os.getlogin() + rutadocumentos + "PowerPoint/")

            #
            if not os.path.exists(files):
            
                #
                os.chdir("C:/Users/" + os.getlogin() + "/Downloads/")

                #
                move(files, "C:/Users/" + os.getlogin() + rutadocumentos + "Word/")


            #
            else:
            
                #
                print("Error el archivo ya existe")
        #        
        elif files.endswith(".xlsx") or files.endswith(".xlsm") or files.endswith(".xltx") or files.endswith(".xltm") or files.endswith("xlsb") or files.endswith("xlam"):
            
            #
            os.chdir("C:/Users/" + os.getlogin() + rutadocumentos + "PowerPoint/")


            #
            if not os.path.exists(files):
            
            
                #
                os.chdir("C:/Users/" + os.getlogin() + "/Downloads/")


                #
                move(files, "C:/Users/" + os.getlogin() + rutadocumentos + "PowerPoint/")


            #
            else:
            
            
                #
                print("El archivo ya existe")


        #
        elif files.endswith(".pptx") or files.endswith(".pptm") or files.endswith(".potx") or files.endswith(".potm") or files.endswith(".ppam") or files.endswith(".ppsx") or files.endswith(".ppsm") or files.endswith(".sldx") or files.endswith(".sldm"):
            
            
            os.chdir("C:/Users/" + os.getlogin() + rutadocumentos + "PowerPoint/")

            
            if not os.path.exists(files):
            
                
                os.chdir("C:/Users/" + os.getlogin() + "/Downloads/")

                
                move(files, "C:/Users/" + os.getlogin() + rutadocumentos + "PowerPoint/")

            
            else:
            
                print("El archivo ya existe")

        #        
        elif files.endswith(".svg") or files.endswith(".jpg") or files.endswith(".png") or files.endswith(".gif"):
        
        
            os.chdir("C:/Users/" + os.getlogin() + rutadocumentos + "Imagenes y Videos/Imagenes/")

            #
            if not os.path.exists(files):
            
                #
                os.chdir("C:/Users/" + os.getlogin() + "/Downloads/")

                #
                move(files, "C:/Users/" + os.getlogin() + rutadocumentos + "Imagenes y Videos/Imagenes/")
            #
            else:
            
                #
                print("El archivo ya existe")

        #        
        elif files.endswith(".mp4") or files.endswith(".avi") or files.endswith(".mov") or files.endswith(".flv") or files.endswith(".mkv") or files.endswith(".wmv"):
            
            #
            os.chdir("C:/Users/" + os.getlogin() + rutadocumentos + "Imagenes y Videos/Videos/")

            #
            if not os.path.exists(files):
            
                #
                os.chdir("C:/Users/" + os.getlogin() + "/Downloads/")

                #
                move(files, "C:/Users/" + os.getlogin() + rutadocumentos + "Imagenes y Videos/Videos/")

            #    
            else:
            
                #
                print("El archivo ya existe")

        #        
        elif files.endswith(".pdf"):
        
        
            #
            os.chdir("C:/Users/" + os.getlogin() + rutadocumentos + "/PDF/")

            #
            if not os.path.exists(files):
            
                #
                os.chdir("C:/Users/" + os.getlogin() + "/Downloads/")

                #
                move(files, "C:/Users/" + os.getlogin() + rutadocumentos + "PDF/")

            #    
            else:
            
                #
                print("El archivo ya existe")
        else:
        
            #
            os.chdir("C:/Users/" + os.getlogin() + rutadocumentos + "/Otros/")

            #
            if not os.path.exists(files):
            
                #
                os.chdir("C:/Users/" + os.getlogin() + "/Downloads/")

                #
                move(files, "C:/Users/" + os.getlogin() + rutadocumentos + "Otros/")
            
            else:
            
                #
                print("El archivo ya existe")

