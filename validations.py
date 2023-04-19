from os import path, getlogin

class validation():

    def disk(self,name):

        routes = str(name)

        if(len(routes) == 1):

            match routes:

                case "A":

                    router = routes+":/"

                    return router 
                 
                case "B":

                    router = routes+":/"

                    return router
                 
                case "D":

                    router = routes+":/"

                    return router 
                
                case "E":

                    router = routes+":/"

                    return router 
                
                case "F":

                    router = routes+":/"

                    return router 
                
                case "G":

                    router = routes+":/"

                    return router 
                
                case "H":

                    router = routes+":/"

                    return router 
                
                case "I":

                    router = routes+":/"

                    return router 
                
                case "J":

                    router = routes+":/"

                    return router 
                
                case "K":

                    router = routes+":/"

                    return router 
                
                case "L":

                    router = routes+":/"

                    return router 
                
                case "M":

                    router = routes+":/"

                    return router 
                
                case "N":

                    router = routes+":/"

                    return router 
                
                case "O":

                    router = routes+":/"

                    return router 
                
                case "P":

                    router = routes+":/"

                    return router 
                
                case "Q":

                    router = routes+":/"

                    return router 
                
                case "R":

                    router = routes+":/"

                    return router 
                
                case "S":

                    router = routes+":/"

                    return router 
                
                case "T":

                    router = routes+":/"

                    return router 
                
                case "U":

                    router = routes+":/"

                    return router 
                
                case "V":

                    router = routes+":/"

                    return router 
                
                case "W":

                    router = routes+":/"

                    return router 
                
                case "X":

                    router = routes+":/"

                    return router 
                
                case "Y":

                    router = routes+":/"

                    return router 
                
                case "Z":

                    router = routes+":/"

                    return router 
                case _:

                    return "El carácter ingresado no se pude utilizar"
        else:
            return "Excedió  el número de caracteres"
    
    def oneDrive(self):

        if  path.exists("C:/Users/"+getlogin()+"/OneDrive"):

            return False
        
        else:

            return True

    def documentsNormal(self):   

        if path.exists("C:/Users/"+getlogin()+"/Documents"):

            return "Documents"
        
        else:

            return "Documentos"
    
    def documentsOneDriver(self):

        if path.exists("C:/Users/"+getlogin()+"/OneDrive/Documents"):

            return "Documents"
        
        else:

            return "Documentos"
    
    def filesvalidations(self,file):

        files = ""

        organizar = file.split(" ")

        for i in organizar:

            files = files + i


        if files.endswith(".docx") or files.endswith(".doc") or files.endswith(".docm") or files.endswith(".dot") or files.endswith(".dotx") or files.endswith(".dotm")\
            or files.endswith(".pdf"):

            rutas = ""

            if files.endswith(".doc"):

                rutas = files.split(".doc")[0]

            elif files.endswith(".doc"):

                rutas = files.split(".doc")[0]

            elif files.endswith(".docm"):

                rutas = files.split(".docm")[0]

            elif files.endswith(".dot"):

                rutas = files.split(".dot")[0]

            elif files.endswith(".dotx"):

                rutas = files.split(".dotx")[0]

            elif files.endswith(".dotm"):

                rutas = files.split(".dotm")[0]

            elif files.endswith(".pdf"):

                rutas = files.split(".pdf")[0]

            elif files.endswith(".docx"):
                
                rutas = files.split(".docx")[0]

            return rutas
        
        else:

            return False
        
    def images(imagen):

        if imagen.endswith(".jpg") or imagen.endswith(".webp") or  imagen.endswith(".gif") or imagen.endswith(".tiff") or imagen.endswith(".svg"):
           

            extension = ""

            if imagen.endswith(".jpg"):
                
                extension = imagen.split(".jpg")
            
            elif imagen.endswith(".webp"):

                extension = imagen.split(".webp")

            elif imagen.endswith(".gif"):

                extension = imagen.split(".gif")

            elif imagen.endswith(".tiff"):

                extension = imagen.split(".tiff")

            elif imagen.endswith(".svg"):

                extension = imagen.split(".svg")

            return extension
        
        else:

            return False


    def audiovalidations(self, filename):

        espacios = 0

        for filename in filename.split(" "):

            espacios = espacios + 1

            if  espacios == 1:

                return "Espacios"

            if filename.endswith(".mp4"):

                file = filename.split(".mp4")

                return file

            else:

                return False