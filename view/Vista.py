from tkinter import *
from customtkinter import *
from tkinter import messagebox
from tkinter import  filedialog
from controlador.yotubeControlador import youtubeController
from controlador.pdfwordControlador import  PdfWord
class Vista:

    def __init__(self):
        set_appearance_mode("System")
        self.__youtube = youtubeController()

        self.__convertidoresDocumentos = PdfWord()

        self.__ventana = CTk()

        self.__ventana.title("Hestia")

        self.__ventana.geometry("700x550")


        self.__ventana.grid_rowconfigure(0, weight=1)

        self.__menu = CTkFrame(self.__ventana)

        self.__menu.grid(row=0,column=0,padx=10, pady=(10, 0),sticky="nsew" )

        self.__menuInicio = CTkButton(self.__menu,text="Inicio",command=lambda:self.__mostrar_ventanas("Inicio"))

        self.__menuInicio.grid(row=0,column=0,padx=10, pady=(10, 0),sticky="w")

        self.__menuYoutube = CTkButton(self.__menu,text="Youtube",command=lambda:self.__mostrar_ventanas("Youtube"))

        self.__menuYoutube.grid(row=1,column=0,padx=10, pady=(10, 0),sticky="w")


        self.__frameInicio = CTkFrame(self.__ventana,width=200, height=200)



        self.__frameYoutube = CTkFrame(self.__ventana)

        self.__mostrar_ventanas("Inicio")

        self.__ventanaEmergenteRaiz = None

    def __ocultar_ventanas(self):
        self.__frameInicio.grid_forget()
        self.__frameYoutube.grid_forget()

    def __mostrar_ventanas(self,nombre):

        self.__ocultar_ventanas()

        if (nombre == "Inicio"):

            self.__frameInicio.grid(row=0,column=3,sticky="n",padx=50)

            self.__frameInicio.grid_columnconfigure(0,weight=3)

            self.__titulo = CTkLabel(self.__frameInicio, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=1,column=0,padx=100,pady=20,columnspan=2)

            self.__informacionInicio = CTkLabel(self.__frameInicio, text="Organizar archivos", font=("Arial", 20))

            self.__informacionInicio.grid(row=2,column=0,pady=20)

            self.__buttonInicioInformacion = CTkButton(self.__frameInicio, text="Información", font=("Arial", 12),command=lambda:self.__Manual("Inicio"))

            self.__buttonInicioInformacion.grid(row=2,column=1,columnspan=2)

            self.__buttonInicio = CTkButton(self.__frameInicio, text="Aceptar", font=("Arial", 20))

            self.__buttonInicio.grid(row=3,column=0,pady=20 ,padx=15,columnspan=2,sticky="ew")

        '''elif (nombre == "Youtube"):

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

            self.__botonJpg.grid(row=3,column=0)'''


    def iniciar_aplicacion(self):
        '''self.__mostrar_ventanas("Inicio")'''
        self.__ventana.mainloop()


    def __SubirDocumentos(self,documento):
        self.__subirDocumento = filedialog.askopenfilenames(title="Abrir")
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

    def __Word_Pdf(self,archivo):
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



    def __Manual(self,tipo):
        ventanaEmergente = CTkToplevel(self.__ventana)

        ventanaEmergente.geometry("400x300")

        manual = None

        if(tipo == "Inicio"):
            manual = CTkLabel(ventanaEmergente,text="Hola mundo")
            manual.pack()
        elif(tipo):
            pass
        elif(tipo):
            pass
        elif(tipo):
            pass

        if self.__ventanaEmergenteRaiz is None or not self.__ventanaEmergenteRaiz.winfo_exists():
            self.__ventanaEmergenteRaiz = ventanaEmergente  # create window if its None or destroyed
        else:
            self.__ventanaEmergenteRaiz.focus()  # if window exists focus it


    def __Notificacion(self,estado,mensaje):

        #if(estado == 0):
            messagebox.showinfo("Exito",mensaje)
        #else:
         #   messagebox.showerror("Error",mensaje)





