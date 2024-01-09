from tkinter import *
from customtkinter import *
from tkinter import messagebox
from tkinter import filedialog
from controlador.controladorYotube import controladorYoutube
from controlador.controladorPdfWord import controladorPdfWord
from controlador.controladorOrganizador import controladorOrganizador
from controlador.controladorImagen import controladorImagen

class Vista:

    def __init__(self, color, ubicacion):

        self.__color = color

        self.__ubicacion = ubicacion

        self.__youtube = controladorYoutube()

        self.__controladorPdfWord = controladorPdfWord()

        self.__controladorImagen = controladorImagen()

        self.__archivosPdf = None

        self.__archivosWord = None

        self.__archivosPng = None

        self.__archivosJpg = None

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

        self.__menuJpg = CTkButton(self.__menu, text="JPG",command=lambda: self.__mostrar_ventanas("Jpg"))

        self.__menuJpg.grid(row=5, column=0, padx=10, pady=(10, 0), sticky="w")

        self.__menuPng = CTkButton(self.__menu,text="PNG",command=lambda:self.__mostrar_ventanas("Png"))

        self.__menuPng.grid(row=6,column=0,padx=10,pady=(10,0),sticky="w")

        self.__frameInicio = CTkFrame(self.__ventana, width=200, height=200)

        self.__frameYoutube = CTkFrame(self.__ventana, width=200, height=200)

        self.__frameWord = CTkFrame(self.__ventana, width=200, height=200)

        self.__framePdf = CTkFrame(self.__ventana, width=200, height=200)

        self.__framePng = CTkFrame(self.__ventana,width=200,height=200)

        self.__frameJpg = CTkFrame(self.__ventana,width=200,height=200)

        self.__mostrar_ventanas("Inicio")

        self.__ventanaEmergenteRaiz = None

    def __ocultar_ventanas(self):
        self.__frameInicio.grid_forget()
        self.__frameYoutube.grid_forget()
        self.__frameWord.grid_forget()
        self.__framePdf.grid_forget()
        self.__frameJpg.grid_forget()
        self.__framePng.grid_forget()

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
                                                       command=lambda: print())

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
                                          command=lambda: self.__youtube.Descargar(self.__inputYoutube.get(), "Audio"
                                                                                   , self.__ubicacion))

            self.__ButonAudio.grid(row=6, column=0, pady=5)

        elif nombre == "Word":

            self.__frameWord.grid(row=0, column=3, sticky="n", padx=50)

            self.__titulo = CTkLabel(self.__frameWord, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=0, column=0, padx=100, pady=20, )

            self.__informacionWord = CTkLabel(self.__frameWord, text="Convertir Documentos a pdf", font=("Arial", 15))

            self.__informacionWord.grid(row=1, column=0, pady=5)

            self.__botonWord = CTkButton(self.__frameWord,
                                         text="Subir archivos",
                                         command=lambda: self.__subirDocumentosWord(), font=("Arial", 12))

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
                                        text="Subir archivos",
                                        command=lambda:self.__subirDocumentosPdf())

            self.__botonPdf.grid(row=2,column=0,pady=5)

            self.__botonPdfConvertidor = CTkButton(self.__framePdf,
                                        text="Convertir a Word",
                                        command=lambda:self.__controladorPdfWord.word(self.__archivosPdf))

        elif nombre == "Png":

            self.__framePng.grid(row=0, column=3, sticky="n", padx=50)

            self.__titulo = CTkLabel(self.__framePng, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=0, column=0, padx=100, pady=20, )

            self.__informacionPng = CTkLabel(self.__framePng, text="Convertir Imagenes a Png", font=("Arial", 15))

            self.__informacionPng.grid(row=1, column=0, pady=5)

            self.__botonPng = CTkButton(self.__framePng,
                                        text="Subir imagenes",
                                        command=lambda: self.__subirImagenesPng())

            self.__botonPng.grid(row=2, column=0, pady=5)

            self.__botonPngConvertidor = CTkButton(self.__framePng,
                                                   text="Convertir a png",
                                                   command=lambda:self.__controladorImagen.png(self.__archivosPng))

        elif nombre == "Jpg":

            self.__frameJpg.grid(row=0, column=3, sticky="n", padx=50)

            self.__titulo = CTkLabel(self.__frameJpg, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=0, column=0, padx=100, pady=20, )

            self.__informacionJpg = CTkLabel(self.__frameJpg, text="Convertir Imagenes a Jpg", font=("Arial", 15))

            self.__informacionJpg.grid(row=1, column=0, pady=5)

            self.__botonJpg = CTkButton(self.__frameJpg,
                                        text="Subir imagenes",
                                        command=lambda: self.__subirImagenesJpg())

            self.__botonJpg.grid(row=2, column=0, pady=5)

            self.__botonJpgConvertidor = CTkButton(self.__frameJpg,
                                                   text="Convertir a jpg",
                                                   command=lambda: self.__controladorImagen.jpg(self.__archivosJpg))


    def iniciar_aplicacion(self):
        self.__ventana.mainloop()

    def __subirDocumentosWord(self):

        self.__subirDocumento = filedialog.askopenfilenames(title="Seleccionar archivos",
                                                            filetypes=[("Archivos de word", "*.docx")])

        if self.__subirDocumento != "":

            self.__botonPdfConvertidor.grid(row=3, column=0, pady=10)

            self.__archivosWord = self.__subirDocumento

    def __subirDocumentosPdf(self):

        self.__subirDocumento = filedialog.askopenfilenames(title="Seleccionar archivos",
                                                            filetypes=[("Archivos de pdf", "*.pdf")])
        print(self.__subirDocumento)
        if self.__subirDocumento != "":

            self.__botonPdfConvertidor.grid(row=3, column=0, pady=10)

            self.__archivosPdf = self.__subirDocumento


    def __subirImagenesPng(self):

        self.__archivosPng = None

        self.__subirImagenes = filedialog.askopenfilenames(title="Seleccionar imagenes",

                                                            filetypes=(
                                                            [
                                                                ("Imagenes", "*.jpeg"),
                                                                ("Imagenes", "*.jpg"),
                                                                ("Imagenes", "*.svg")
                                                            ]))
        print(self.__subirImagenes)

        if self.__subirImagenes != "":

            self.__botonPngConvertidor.grid(row=3, column=0, pady=10)

            self.__archivosPng = self.__subirImagenes

    def __subirImagenesJpg(self):
        self.__archivosJpg = None

        self.__subirImagenes = filedialog.askopenfilenames(title="Seleccionar imagenes",

                                                            filetypes=(
                                                                [
                                                                    ("Imagenes", "*.jpeg"),
                                                                    ("Imagenes", "*.png"),
                                                                    ("Imagenes", "*.svg")
                                                                ]))
        print(self.__subirImagenes)

        if self.__subirImagenes != "":

            self.__botonJpgConvertidor.grid(row=3, column=0, pady=10)

            self.__archivosJpg = self.__subirImagenes