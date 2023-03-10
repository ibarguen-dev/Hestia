import os
from pathlib import Path
from shutil import move
from pdf2docx import  Converter, parse
from patoolib import extract_archive

print('''


                                                        **************************************************************************************************
                                                        *    8 8888        8 8 8888888888     d888888o. 8888888 8888888888 8 8888          .8.           *
                                                        *    8 8888        8 8 8888         .`8888:' `88.     8 8888       8 8888         .888.          *
                                                        *    8 8888        8 8 8888         8.`8888.   Y8     8 8888       8 8888        :88888.         *   
                                                        *    8 8888        8 8 8888         `8.`8888.         8 8888       8 8888       . `88888.        *
                                                        *    8 8888        8 8 888888888888  `8.`8888.        8 8888       8 8888      .8. `88888.       *
                                                        *    8 8888        8 8 8888           `8.`8888.       8 8888       8 8888     .8`8. `88888.      *
                                                        *    8 8888888888888 8 8888            `8.`8888.      8 8888       8 8888    .8' `8. `88888.     *
                                                        *    8 8888        8 8 8888        8b   `8.`8888.     8 8888       8 8888   .8'   `8. `88888.    *
                                                        *    8 8888        8 8 8888        `8b.  ;8.`8888     8 8888       8 8888  .888888888. `88888.   *
                                                        *    8 8888        8 8 888888888888 `Y8888P ,88P'     8 8888       8 8888 .8'       `8. `88888.  * 
                                                        ************************************************************************************************** 


                                                        

''')


def menu():
    print('''
                                                        ******************************************** MENU DE OPCIONES *************************************
                                                        *   1. Convertir de pdf a word o de word a pdf                                                    *
                                                        *   2. Convertir un archivo de mp4 a mp3                                                          *
                                                        *   3. Descargar office y instalar office                                                         *
                                                        *   4. Descomprimir archivos                                                                      *
                                                        *   5. Hacer copias de seguridad del equipo                                                       *
                                                        *   6. Mas informacion de Hestia                                                                  *
                                                        ***************************************************************************************************   
    ''')


menu()


def convertDocumento():
    pdf = input("Ingrese el nombre del pdf: ")
    parse(pdf+".pdf",pdf+".docx",start=0, end=0)


def Descomprimir(files):
    extract_archive(files)
    os.remove(files)


def CreacionTrsaladoFiles():
    if not os.path.exists("C:/Users/" + os.getlogin() + "/Documentos"):
        os.chdir("C:/Users/" + os.getlogin() + "/Documents/")
    else:
        os.chdir("C:/Users/" + os.getlogin() + "/Documentos/")

    if not os.path.exists("PDF"):
        Path("PDF").mkdir(exist_ok=True)
        Path("Word").mkdir(exist_ok=True)
        Path("Ejecutables").mkdir(exist_ok=True)
        Path("Imagenes y Videos").mkdir(exist_ok=True)
        Path("Excel").mkdir(exist_ok=True)
        Path("PowerPoint").mkdir(exist_ok=True)
        Path("Otros").mkdir(exist_ok=True)
        os.chdir("Imagenes y Videos/")
        Path("Imagenes").mkdir(exist_ok=True)
        Path("Videos").mkdir(exist_ok=True)

    os.chdir("C:/Users/" + os.getlogin() + "/Downloads/")
    for files in os.listdir():

        if files.endswith(".rar") or files.endswith(".zip") or files.endswith(".7z") or files.endswith(".ace") or \
                files.endswith(".adf") or files.endswith(".alz") or files.endswith(".ape") or files.endswith(".a") \
                or files.endswith(".arc") or files.endswith(".arj") or files.endswith(".bz2") or files.endswith(".cab") \
                or files.endswith(".Z") or files.endswith(".cpio") or files.endswith(".deb") or files.endswith(".dms") \
                or files.endswith(".flac") or files.endswith(".gz") or files.endswith(".lzma") or files.endswith(".lrz") \
                or files.endswith(".lha") or files.endswith(".lzh") or files.endswith(".lz") or files.endswith(".lzo") \
                or files.endswith(".rpm") or files.endswith(".rz") or files.endswith(".shn") or files.endswith(".tar") \
                or files.endswith(".xz") or files.endswith(".jar") or files.endswith(".zoo") or files.endswith(".zpaq"):
            Descomprimir(files)
    rutadocumentos = ""
    if not os.path.exists("C:/Users/" + os.getlogin() + "/Documentos"):
        rutadocumentos = "/Documents/"
    else:
        rutadocumentos = "/Documentos/"
    for files in os.listdir():
        if files.endswith(".docx") or files.endswith(".docm") or files.endswith(".dotx") or files.endswith(".dotm"):

            os.chdir("C:/Users/" + os.getlogin() + rutadocumentos + "PowerPoint/")
            if not os.path.exists(files):
                os.chdir("C:/Users/" + os.getlogin() + "/Downloads/")
                move(files, "C:/Users/" + os.getlogin() + rutadocumentos + "Word/")

            else:
                print("Error el archivo ya existe")

        elif files.endswith(".xlsx") or files.endswith(".xlsm") or files.endswith(".xltx") or files.endswith(".xltm") \
                or files.endswith("xlsb") or files.endswith("xlam"):

            os.chdir("C:/Users/" + os.getlogin() + rutadocumentos + "PowerPoint/")
            if not os.path.exists(files):
                os.chdir("C:/Users/" + os.getlogin() + "/Downloads/")
                move(files, "C:/Users/" + os.getlogin() + rutadocumentos + "PowerPoint/")
            else:
                print("El archivo ya existe")

        elif files.endswith(".pptx") or files.endswith(".pptm") or files.endswith(".potx") or files.endswith(".potm") \
                or files.endswith(".ppam") or files.endswith(".ppsx") or files.endswith(".ppsm") or files.endswith(
            ".sldx") \
                or files.endswith(".sldm"):

            os.chdir("C:/Users/" + os.getlogin() + rutadocumentos + "PowerPoint/")
            if not os.path.exists(files):
                os.chdir("C:/Users/" + os.getlogin() + "/Downloads/")
                move(files, "C:/Users/" + os.getlogin() + rutadocumentos + "PowerPoint/")
            else:
                print("El archivo ya existe")

        elif files.endswith(".svg") or files.endswith(".jpg") or files.endswith(".png") or files.endswith(".gif"):

            os.chdir("C:/Users/" + os.getlogin() + rutadocumentos + "Imagenes y Videos/Imagenes/")
            if not os.path.exists(files):
                os.chdir("C:/Users/" + os.getlogin() + "/Downloads/")
                move(files, "C:/Users/" + os.getlogin() + rutadocumentos + "Imagenes y Videos/Imagenes/")
            else:
                print("El archivo ya existe")


        elif files.endswith(".mp4") or files.endswith(".avi") or files.endswith(".mov") or files.endswith(".flv")\
                or files.endswith(".mkv") or files.endswith(".wmv"):

            os.chdir("C:/Users/" + os.getlogin() + rutadocumentos + "Imagenes y Videos/Videos/")
            if not os.path.exists(files):
                os.chdir("C:/Users/" + os.getlogin() + "/Downloads/")
                move(files, "C:/Users/" + os.getlogin() + rutadocumentos + "Imagenes y Videos/Videos/")
            else:
                print("El archivo ya existe")

        else:
            os.chdir("C:/Users/" + os.getlogin() + rutadocumentos + "/Otros/")
            if not os.path.exists(files):
                os.chdir("C:/Users/" + os.getlogin() + "/Downloads/")
                move(files, "C:/Users/" + os.getlogin() + rutadocumentos + "Otros/")
            else:
                print("El archivo ya existe")


while True:
    CreacionTrsaladoFiles()
    respuesta = int(input("Porfavor ingrese la opcion que quiere que HESTIA ejecute "))

'''
    match respuesta :
        case 1:
            convertDocumento()
        case 2:

        case 3:

        case 4:

        case 5:

        case 6:

    verificar = int(input("Si deseas que Hestia Siga ejecutandose ingrese el numero 1. Escriba su respuesta" ))
'''
