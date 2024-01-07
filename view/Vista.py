from tkinter import *
from customtkinter import *
from tkinter import messagebox
from tkinter import filedialog
from controlador.controladorYotube import controladorYoutube
from controlador.controladorPdfWord import controladorPdfWord
from controlador.controladorOrganizador import controladorOrganizador


class Vista:

    def __init__(self, color, ubicacion):



        self.__color = color

        self.__ubicacion = ubicacion

        self.__youtube = controladorYoutube()

        self.__controladorPdfWord = controladorPdfWord()

        self.__archivosPdf = None

        self.__archivosWord = None

        self.__organizador = controladorOrganizador(self.__ubicacion)

        set_appearance_mode(self.__color)

        self.__ventana = CTk()

        self.__ventana.title("Hestia")

        self.__ventana.geometry("700x550")

        self.__ventana.grid_rowconfigure(0, weight=1)

        self.__menu = CTkFrame(self.__ventana)

        self.__menu.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.__menuInicio = CTkButton(self.__menu, text="Inicio", command=lambda: self.__mostrar_ventanas("Inicio"))

        self.__menuInicio.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.__menuYoutube = CTkButton(self.__menu, text="Youtube", command=lambda: self.__mostrar_ventanas("Youtube"))

        self.__menuYoutube.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.__menuWord = CTkButton(self.__menu, text="Word", command=lambda: self.__mostrar_ventanas("Word"))

        self.__menuWord.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")

        self.__menuPdf = CTkButton(self.__menu, text="PDF", command=lambda: self.__mostrar_ventanas("Pdf"))

        self.__menuPdf.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")

        self.__frameInicio = CTkFrame(self.__ventana, width=200, height=200)

        self.__frameYoutube = CTkFrame(self.__ventana, width=200, height=200)

        self.__frameWord = CTkFrame(self.__ventana, width=200, height=200)

        self.__framePdf = CTkFrame(self.__ventana, width=200, height=200)

        self.__mostrar_ventanas("Inicio")

        self.__ventanaEmergenteRaiz = None

    def __ocultar_ventanas(self):
        self.__frameInicio.grid_forget()
        self.__frameYoutube.grid_forget()
        self.__frameWord.grid_forget()
        self.__framePdf.grid_forget()

    def __mostrar_ventanas(self, nombre):

        self.__ocultar_ventanas()

        if nombre == "Inicio":

            self.__frameInicio.grid(row=0, column=3, sticky="n", padx=50)

            self.__frameInicio.grid_columnconfigure(0, weight=3)

            self.__titulo = CTkLabel(self.__frameInicio, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=1, column=0, padx=100, pady=20, columnspan=2)

            self.__informacionInicio = CTkLabel(self.__frameInicio, text="Organizar archivos", font=("Arial", 20))

            self.__informacionInicio.grid(row=2, column=0, pady=20)

            self.__buttonInicioInformacion = CTkButton(self.__frameInicio, text="Información", font=("Arial", 12),
                                                       command=lambda: self.__Manual("Inicio"))

            self.__buttonInicioInformacion.grid(row=2, column=1, columnspan=2)

            self.__buttonInicio = CTkButton(self.__frameInicio, text="Aceptar", font=("Arial", 20),
                                            command=lambda: self.__organizador.archivos())

            self.__buttonInicio.grid(row=3, column=0, pady=20, padx=15, columnspan=2, sticky="ew")

        elif nombre == "Youtube":
            self.__frameYoutube.grid(row=0, column=3, sticky="n", padx=50)

            self.__frameYoutube.grid_columnconfigure(0, weight=3)

            # -----------------------------------------------------------------------------------------------------------------------

            self.__titulo = CTkLabel(self.__frameYoutube, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=0, column=0, padx=100, pady=20, columnspan=2)

            # -----------------------------------------------------------------------------------------------------------------------
            self.__informacionYoutube = CTkLabel(self.__frameYoutube, text="Descargar videos o audios de youtube",
                                                 font=("Arial", 15))

            self.__informacionYoutube.grid(row=1, column=0)
            # -----------------------------------------------------------------------------------------------------------------------
            self.__link = CTkLabel(self.__frameYoutube, text="Ingrear Link", font=("Arial", 15))

            self.__link.grid(row=2, column=0)
            # ----------------------------------------------------------------------------------------------------------------------
            self.__inputYoutube = CTkEntry(self.__frameYoutube, width=250)

            self.__inputYoutube.grid(row=3, column=0, pady=20)

            self.__ButonAlta = CTkButton(self.__frameYoutube, text="Alta calidad",
                                         command=lambda: self.__youtube.Descargar(self.__inputYoutube.get(), "Alta"
                                                                                  , self.__ubicacion))

            self.__ButonAlta.grid(row=4, column=0, pady=5)

            self.__ButonBaja = CTkButton(self.__frameYoutube, text="Baja calidad",
                                         command=lambda: self.__youtube.Descargar(self.__inputYoutube.get(), "Baja"
                                                                                  , self.__ubicacion))

            self.__ButonBaja.grid(row=5, column=0, pady=5)

            self.__ButonAudio = CTkButton(self.__frameYoutube, text="Audios",
                                          command=lambda: self.__youtube.Descargar(self.__inputYoutube.get(), "Baja"
                                                                                   , self.__ubicacion))

            self.__ButonAudio.grid(row=6, column=0, pady=5)


        # -----------------------------------------------------------------------------------------------------------------------

        elif nombre == "Word":

            self.__frameWord.grid(row=0, column=3, sticky="n", padx=50)

            self.__titulo = CTkLabel(self.__frameWord, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=0, column=0, padx=100, pady=20, )

            self.__informacionWord = CTkLabel(self.__frameWord, text="Convertir Documentos a pdf", font=("Arial", 15))

            self.__informacionWord.grid(row=1, column=0, pady=5)

            self.__botonWord = CTkButton(self.__frameWord,
                                         text="Subir archivos",
                                         command=lambda: self.__SubirDocumentosWord(), font=("Arial", 12))

            self.__botonWord.grid(row=2, column=0, pady=10)

            self.__botonWordConvertidor = CTkButton(self.__frameWord,
                                                    text="Convertir pdf",
                                                    command=lambda:self.__controladorPdfWord.pdf(self.__archivosWord))



        elif nombre == "Pdf":

            self.__framePdf.grid(row=0, column=3, sticky="n", padx=50)

            self.__titulo = CTkLabel(self.__framePdf, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=0, column=0, padx=100, pady=20, )

            self.__informacionPdf = CTkLabel(self.__framePdf, text="Convertir Documentos a Word", font=("Arial", 15))

            self.__informacionPdf.grid(row=1, column=0, pady=5)

            self.__botonPdf = CTkButton(self.__framePdf,
                                        text="Subir archivos", )

            self.__botonPdfConvertidor = CTkButton(self.__framePdf,
                                        text="Convertir a Word",
                                        command=lambda:self.__controladorPdfWord.word(self.__archivosPdf))



        '''elif nombre == "Imagenes":

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

    def __SubirDocumentosWord(self):

        self.__subirDocumento = filedialog.askopenfilenames(title="Seleccionar archivos",
                                                            filetypes=[("Archivos de word", "*.docx")])

        if self.__subirDocumento != "":

            self.__botonPdfConvertidor.grid(row=3, column=0, pady=10)

            self.__archivosPdf = self.__subirDocumento

    def __SubirDocumentosPdf(self):

        self.__subirDocumento = filedialog.askopenfilenames(title="Seleccionar archivos",
                                                            filetypes=[("Archivos de pdf", "*.pdf")])

        if self.__subirDocumento != "":

            self.__botonPdf.grid(row=2, column=0, pady=10)

            self.__archivosWord = self.__subirDocumento


    # def __Png_o_Jpg(self,tipo,archivo):

    #    nombre= None
    #    if (archivo.endswith(".jpg") or archivo.endswith(".webp") or archivo.endswith("jpeg") or archivo.endswith(
    #       ".gif") or archivo.endswith(".tiff") or archivo.endswith(".svg")):

    #        if archivo.endswith(".jpg"):

    #            nombre = archivo.split(".jpg")[0]

    #        elif archivo.endswith(".jpeg"):

    #            nombre = archivo.split(".jpeg")[0]

    #        elif archivo.endswith(".webp"):

    #            nombre = archivo.split(".webp")[0]

    #        elif archivo.endswith(".gif"):

    #            nombre = archivo.split(".gif")[0]

    #        elif archivo.endswith(".tiff"):

    #            nombre = archivo.split(".tiff")[0]

    #        elif archivo.endswith(".svg"):

    #            nombre = archivo.split(".svg")[0]

    # def __Word_Pdf(self,archivo):
    #    nombre = None
    #    mensaje = None
    #    if archivo.endswith(".docx"):
    #        nombre = archivo.split(".docx")[0]

    #    elif archivo.endswith(".pdf"):
    #        nombre = archivo.split(".pdf")[0]
    #    else:

    #        resultado = [1, "El documento ingresado no es un pdf o un docuemto de word"]

    #    resultado = self.__convertidoresDocumentos.pdf(nombre, archivo)

    #    estado = resultado[0]

    #    mensaje = resultado[1]

    #    self.__Notificacion(estado, mensaje)

    # def __Manual(self,tipo):
    #    ventanaEmergente = CTkToplevel(self.__ventana)

    #    ventanaEmergente.geometry("400x300")

    #    manual = None

    #    if(tipo == "Inicio"):
    #        manual = CTkLabel(ventanaEmergente,text="Hola mundo")
    #        manual.pack()
    #    elif(tipo):
    #        pass
    #    elif(tipo):
    #        pass
    #    elif(tipo):
    #        pass

    #    if self.__ventanaEmergenteRaiz is None or not self.__ventanaEmergenteRaiz.winfo_exists():
    #        self.__ventanaEmergenteRaiz = ventanaEmergente  # create window if its None or destroyed
    #    else:
    #        self.__ventanaEmergenteRaiz.focus()  # if window exists focus it

    def __Notificacion(self, estado, mensaje):

        if (estado == 0):
            messagebox.showinfo("Exito", mensaje)
        else:
            messagebox.showerror("Error", mensaje)
