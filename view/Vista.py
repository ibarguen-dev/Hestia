from tkinter import *
from tkinter import messagebox
from controlador import yotubeControlador

class Vista:

    def __init__(self):

        self.youtube = yotubeControlador.youtubeController()

        self.ventana = Tk()

        self.ventana.title("Hestia")

        self.ventana.geometry("400x500")

        self.barraMenu = Menu(self.ventana)

        self.ventana.config(menu=self.barraMenu, width=550, height=550)
# ----------------------------------------------------------------------------------------------------------------------
        self.inicioMenu = Menu(self.barraMenu, tearoff=0)
        self.inicioMenu.add_command(label="Abrir",command=lambda: self.mostrar_ventanas("Inicio"))
#-----------------------------------------------------------------------------------------------------------------------
        self.convertidoresMenu = Menu(self.barraMenu,tearoff=0)

        self.convertidoresMenu.add_command(label="Convertir PDF a WORD",)

        self.convertidoresMenu.add_command(label="Convertir WORD a PDF")

        self.convertidoresMenu.add_separator()

        self.convertidoresMenu.add_command(label="Convertir Imagen A PNG")

        self.convertidoresMenu.add_command(label="Convertir Imagen A JPG")
#-----------------------------------------------------------------------------------------------------------------------

        self.youtubeMenu = Menu(self.barraMenu,tearoff=0)
        self.youtubeMenu.add_command(label="Abrir",command=lambda :self.mostrar_ventanas("Youtube"))
#-----------------------------------------------------------------------------------------------------------------------

        self.configuracionMenu = Menu(self.barraMenu, tearoff=0)

        self.configuracionMenu.add_command(label="Cambiar el disco duro")

        self.configuracionMenu.add_command(label="Buscar actualizaciones")

        self.configuracionMenu.add_command(label="Cambiar el color")


#-----------------------------------------------------------------------------------------------------------------------

        self.ayudaMenu = Menu(self.barraMenu,tearoff=0)

        self.ayudaMenu.add_command(label="Manual de hestia")

        self.ayudaMenu.add_command(label="Acerca de...")

        self.ayudaMenu.add_command(label="Licencia")

#-----------------------------------------------------------------------------------------------------------------------
        self.barraMenu.add_cascade(label="Inicio",menu=self.inicioMenu)

        self.barraMenu.add_cascade(label="Convertidores", menu=self.convertidoresMenu)

        self.barraMenu.add_cascade(label="Youtube", menu=self.youtubeMenu)

        self.barraMenu.add_cascade(label="Configuracion", menu=self.configuracionMenu)

        self.barraMenu.add_cascade(label="Ayuda", menu=self.ayudaMenu)
#-----------------------------------------------------------------------------------------------------------------------

        self.vistaInicio = Frame(self.ventana)

        self.vistaYoutube = Frame(self.ventana)


    def ocultar_ventanas(self):
        self.vistaInicio.pack_forget()
        self.vistaYoutube.pack_forget()


    def mostrar_ventanas(self,nombre):

        self.ocultar_ventanas()

        if (nombre == "Inicio"):

            self.vistaInicio.pack()

            self.titulo = Label(self.vistaInicio, text="Hestia", font=("Arial", 50))

            self.titulo.grid(row=0, column=0)

            self.informacion = Label(self.vistaInicio, text="Organizar archivos", font=("Arial", 12))

            self.informacion.grid(row=1, column=0)

            self.button = Button(self.vistaInicio, text="Aceptar", font=("Arial", 10))

            self.button.grid(row=3, column=0)

        elif (nombre == "Youtube"):

            self.vistaYoutube.pack()
#-----------------------------------------------------------------------------------------------------------------------
            self.titulo = Label(self.vistaYoutube, text="Hestia", font=("Arial", 50))

            self.titulo.grid(row=0, column=0)
#-----------------------------------------------------------------------------------------------------------------------
            self.informacion = Label(self.vistaYoutube, text="Descargar videos o audios de youtube", font=("Arial", 15))

            self.informacion.grid(row=1, column=0,)
#-----------------------------------------------------------------------------------------------------------------------
            self.link = Label(self.vistaYoutube, text="Ingrear Link", font=("Arial", 10))

            self.link.grid(row=2, column=0)
#----------------------------------------------------------------------------------------------------------------------
            self.input = Entry(self.vistaYoutube)

            self.input.grid(row=3, column=0)

            self.ButonAlta = Button(self.vistaYoutube,text="Alta calidad",command=lambda:self.Youtube("Alta") )

            self.ButonAlta.grid(row=4, column=0)

            self.ButonBaja = Button(self.vistaYoutube,text="Baja calidad",command=lambda:self.youtube("Baja"))

            self.ButonBaja.grid(row=5, column=0)

            self.ButonAudio = Button(self.vistaYoutube,text="Audios",command=lambda:self.youtube("Audios"))

            self.ButonAudio.grid(row=6, column=0)

        elif (nombre == "c"):
            pass

    def iniciar_aplicacion(self):
        self.mostrar_ventanas("Inicio")
        self.ventana.mainloop()



    def Youtube(self,boton):

        link = self.input.get()

        resultado =  self.youtube.Descargar(link,boton)

        estado = resultado[0]

        mensaje = resultado[1]

        self.Notificacion(estado,mensaje)

    def Notificacion(self,estado,mensaje):

        if(estado == 0):
            messagebox.showinfo("Exito",mensaje)
        else:
            messagebox.showerror("Error",mensaje)


vista = Vista()
vista.iniciar_aplicacion()

