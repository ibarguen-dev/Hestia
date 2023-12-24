from tkinter import *
from tkinter import messagebox
from tkinter import  filedialog
from controlador import yotubeControlador
from controlador import  pdfwordControlador
class Vista:

    def __init__(self):

        self.__youtube = yotubeControlador.youtubeController()

        self.__convertidoresDocumentos = pdfwordControlador.PdfWord()

        self.__ventana = Tk()

        self.__ventana.title("Hestia")

        self.__ventana.geometry("400x350")

        self.__barraMenu = Menu(self.__ventana)

        self.__ventana.config(menu=self.__barraMenu, width=550, height=550)
# ----------------------------------------------------------------------------------------------------------------------
        self.__inicioMenu = Menu(self.__barraMenu, tearoff=0)
        self.__inicioMenu.add_command(label="Abrir",command=lambda: self.__mostrar_ventanas("Inicio"))
#-----------------------------------------------------------------------------------------------------------------------
        self.__convertidoresMenu = Menu(self.__barraMenu,tearoff=0)

        self.__convertidoresMenu.add_command(label="Convertir PDF a WORD o WORD a PDF",command=lambda: self.__mostrar_ventanas("Documentos"))

        self.__convertidoresMenu.add_separator()

        self.__convertidoresMenu.add_command(label="Convertir Imagen A PNG o JPG",command=lambda:self.__mostrar_ventanas("Imagenes"))

#-----------------------------------------------------------------------------------------------------------------------

        self.__youtubeMenu = Menu(self.__barraMenu,tearoff=0)
        self.__youtubeMenu.add_command(label="Abrir",command=lambda :self.__mostrar_ventanas("Youtube"))
#-----------------------------------------------------------------------------------------------------------------------

        self.__configuracionMenu = Menu(self.__barraMenu, tearoff=0)

        self.__configuracionMenu.add_command(label="Cambiar el disco duro")

        self.__configuracionMenu.add_command(label="Buscar actualizaciones")

        self.__configuracionMenu.add_command(label="Cambiar el color")


#-----------------------------------------------------------------------------------------------------------------------

        self.__ayudaMenu = Menu(self.__barraMenu,tearoff=0)

        self.__ayudaMenu.add_command(label="Manual de hestia")

        self.__ayudaMenu.add_command(label="Acerca de...")

        self.__ayudaMenu.add_command(label="Licencia")

#-----------------------------------------------------------------------------------------------------------------------
        self.__barraMenu.add_cascade(label="Inicio",menu=self.__inicioMenu)

        self.__barraMenu.add_cascade(label="Convertidores", menu=self.__convertidoresMenu)

        self.__barraMenu.add_cascade(label="Youtube", menu=self.__youtubeMenu)

        self.__barraMenu.add_cascade(label="Configuracion", menu=self.__configuracionMenu)

        self.__barraMenu.add_cascade(label="Ayuda", menu=self.__ayudaMenu)
#-----------------------------------------------------------------------------------------------------------------------

        self.__vistaInicio = Frame(self.__ventana)

        self.__vistaYoutube = Frame(self.__ventana)

        self.__vistaDocumento =Frame(self.__ventana)

        self.__vistaImagen = Frame(self.__ventana)


    def __ocultar_ventanas(self):
        self.__vistaInicio.pack_forget()
        self.__vistaYoutube.pack_forget()
        self.__vistaDocumento.pack_forget()
        self.__vistaImagen.pack_forget()

    def __mostrar_ventanas(self,nombre):

        self.__ocultar_ventanas()

        if (nombre == "Inicio"):

            self.__vistaInicio.pack()

            self.__titulo = Label(self.__vistaInicio, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=0, column=0)

            self.__informacion = Label(self.__vistaInicio, text="Organizar archivos", font=("Arial", 12))

            self.__informacion.grid(row=1, column=0)

            self.__button = Button(self.__vistaInicio, text="Aceptar", font=("Arial", 12))

            self.__button.grid(row=3, column=0)

        elif (nombre == "Youtube"):

            self.__vistaYoutube.pack()
#-----------------------------------------------------------------------------------------------------------------------
            self.__titulo = Label(self.__vistaYoutube, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=0, column=0)
#-----------------------------------------------------------------------------------------------------------------------
            self.__informacion = Label(self.__vistaYoutube, text="Descargar videos o audios de youtube", font=("Arial", 15))

            self.__informacion.grid(row=1, column=0,)
#-----------------------------------------------------------------------------------------------------------------------
            self.__link = Label(self.__vistaYoutube, text="Ingrear Link", font=("Arial", 10))

            self.__link.grid(row=2, column=0)
#----------------------------------------------------------------------------------------------------------------------
            self.__input = Entry(self.__vistaYoutube)

            self.__input.grid(row=3, column=0)

            self.__ButonAlta = Button(self.__vistaYoutube,text="Alta calidad",command=lambda:self.__Youtube("Alta") )

            self.__ButonAlta.grid(row=4, column=0)

            self.__ButonBaja = Button(self.__vistaYoutube,text="Baja calidad",command=lambda:self.__youtube("Baja"))

            self.__ButonBaja.grid(row=5, column=0)

            self.__ButonAudio = Button(self.__vistaYoutube,text="Audios",command=lambda:self.__youtube("Audios"))

            self.__ButonAudio.grid(row=6, column=0)

#-----------------------------------------------------------------------------------------------------------------------


        elif(nombre == "Documentos"):

            self.__vistaDocumento.pack()

            self.__titulo = Label(self.__vistaDocumento, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=0, column=0)

            self.__informacion = Label(self.__vistaDocumento, text="Convertir Documentos", font=("Arial", 15))

            self.__informacion.grid(row=1, column=0)

            self.__botonWord = Button(self.__vistaDocumento, text="Convertir a word", command=lambda:self.__SubirDocumentos("word"), font=("Arial",12))

            self.__botonWord.grid(row=2,column=0)

        elif(nombre == "Imagenes"):

            self.__vistaImagen.pack()

            self.__titulo = Label(self.__vistaImagen, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=0, column=0)

            self.__informacion = Label(self.__vistaImagen, text="Convertir Imagenes", font=("Arial", 15))

            self.__informacion.grid(row=1, column=0)

            self.__botonPng = Button(self.__vistaImagen, text="Convertir a Png",font=("Arial",12))

            self.__botonPng.grid(row=2,column=0)

            self.__botonJpg =Button(self.__vistaImagen,text="Convertir a jpg",font=("Arial,12"))

            self.__botonJpg.grid(row=3,column=0)


    def iniciar_aplicacion(self):
        self.__mostrar_ventanas("Inicio")
        self.__ventana.mainloop()


    def __SubirDocumentos(self,documento):
        self.__subirDocumento = filedialog.askopenfilename(title="Abrir")
        archivo = self.__subirDocumento


        if(documento=="pdf" or documento == "word" ):
            self.__Word_Pdf(documento,archivo)
        else:
            self.__Png_o_Jpg(documento,archivo)


    def __Youtube(self,boton):

        link = self.__input.get()

        estado = None

        mensaje = None

        if(link != ""):

            resultado =  self.__youtube.Descargar(link,boton)

            estado = resultado[0]

            mensaje = resultado[1]
        else:
            estado = 1

            mensaje = "El campo esta vacio"

        self.__Notificacion(estado,mensaje)

        del estado

        del mensaje


    def __Png_o_Jpg(self,tipo,archivo):

        nombre= None
        if (archivo.endswith(".jpg") or archivo.endswith(".webp") or archivo.endswith("jpeg") or archivo.endswith(
            ".gif") or archivo.endswith(".tiff") or archivo.endswith(".svg")):

            if archivo.endswith(".jpg"):

                nombre = archivo.split(".jpg")[0]

            elif archivo.endswith(".jpeg"):

                nombre = archivo.split(".jpeg")[0]

            elif archivo.endswith(".webp"):

                nombre = archivo.split(".webp")[0]

            elif archivo.endswith(".gif"):

                nombre = archivo.split(".gif")[0]

            elif archivo.endswith(".tiff"):

                nombre = archivo.split(".tiff")[0]

            elif archivo.endswith(".svg"):

                nombre = archivo.split(".svg")[0]




    def __Word_Pdf(self,documento,archivo):
        nombre = None
        mensaje = None
        if archivo.endswith(".docx"):
            nombre = archivo.split(".docx")[0]

        elif archivo.endswith(".pdf"):
            nombre = archivo.split(".pdf")[0]
        else:

            resultado = [1, "El documento ingresado no es un pdf o un docuemto de word"]


        resultado = self.__convertidoresDocumentos.pdf(nombre, archivo)

        estado = resultado[0]

        mensaje = resultado[1]

        self.__Notificacion(estado, mensaje)

    def __Notificacion(self,estado,mensaje):

        if(estado == 0):
            messagebox.showinfo("Exito",mensaje)
        else:
            messagebox.showerror("Error",mensaje)


vista = Vista()
vista.iniciar_aplicacion()



