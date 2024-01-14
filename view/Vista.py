from tkinter import *
from customtkinter import *
from tkinter import messagebox
from tkinter import filedialog
from controlador.controladorYotube import controladorYoutube
from controlador.controladorPdfWord import controladorPdfWord
from controlador.controladorOrganizador import controladorOrganizador
from controlador.controladorImagen import controladorImagen
from  controlador.controladorConfiguraciones import Configuraciones
from os import  chdir ,getcwd
class Vista:

    def __init__(self, color, ubicacion,aplicacion):

        """
        Inicializa la aplicación principal.

        :param color: Color de la interfaz gráfica.
        :param ubicacion: Ruta de la ubicación para las carpetas de la aplicación.
        :param aplicacion: Ruta de la aplicación.
        """

        #Se dirigi a ala ubicación de la aplicación
        chdir(aplicacion)

        # Inicialización de variables
        self.__color = color
        self.__ubicacion = ubicacion
        self.__youtube = controladorYoutube()
        self.__controladorPdfWord = controladorPdfWord()
        self.__controladorImagen = controladorImagen()
        self.__Configuraciones = Configuraciones()
        self.__organizador = controladorOrganizador(self.__ubicacion)
        self.__archivosPdf = None
        self.__archivosWord = None
        self.__archivosPng = None
        self.__archivosJpg = None



        # Configuración de la apariencia de la interfaz gráfica
        set_appearance_mode(self.__color)
        self.__ventana = CTk()
        self.__ventana.title("Hestia")
        self.__ventana.geometry("700x550")
        self.__ventana.grid_rowconfigure(0, weight=1)

        # Configuración del menú lateral
        self.__menu = CTkFrame(self.__ventana)
        self.__menu.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.__menuInicio = CTkButton(self.__menu, text="Inicio", fg_color="#607D8B",
                                      command=lambda: self.__mostrar_ventanas("Inicio"))
        self.__menuInicio.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.__menuYoutube = CTkButton(self.__menu, text="Youtube", fg_color="#607D8B",
                                       command=lambda: self.__mostrar_ventanas("Youtube"))
        self.__menuYoutube.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.__menuWord = CTkButton(self.__menu, text="Word", fg_color="#607D8B",
                                    command=lambda: self.__mostrar_ventanas("Word"))
        self.__menuWord.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")
        self.__menuPdf = CTkButton(self.__menu, text="PDF", fg_color="#607D8B",
                                   command=lambda: self.__mostrar_ventanas("Pdf"))
        self.__menuPdf.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")
        self.__menuJpg = CTkButton(self.__menu, text="JPG", fg_color="#607D8B",
                                   command=lambda: self.__mostrar_ventanas("Jpg"))
        self.__menuJpg.grid(row=5, column=0, padx=10, pady=(10, 0), sticky="w")
        self.__menuPng = CTkButton(self.__menu, text="PNG", fg_color="#607D8B",
                                   command=lambda: self.__mostrar_ventanas("Png"))
        self.__menuPng.grid(row=6, column=0, padx=10, pady=(10, 0), sticky="w")
        self.__menuConfiguraciones = CTkButton(self.__menu, text="Configuraciones", fg_color="#607D8B",
                                               command=lambda:self.__mostrar_ventanas("Configuraciones"))
        self.__menuConfiguraciones.grid(row=7, column=0, padx=10, pady=(10, 0), sticky="w")

        # Configuración de los marcos de contenido
        self.__frameInicio = CTkFrame(self.__ventana, width=200, height=200)
        self.__frameYoutube = CTkFrame(self.__ventana, width=200, height=200)
        self.__frameWord = CTkFrame(self.__ventana, width=200, height=200)
        self.__framePdf = CTkFrame(self.__ventana, width=200, height=200)
        self.__framePng = CTkFrame(self.__ventana, width=200, height=200)
        self.__frameJpg = CTkFrame(self.__ventana, width=200, height=200)
        self.__frameConfiguracion = CTkFrame(self.__ventana, width=200, height=200)
        self.__mostrar_ventanas("Inicio")
        self.__ventanaEmergenteRaiz = None

    def __ocultar_ventanas(self):
        """
        Oculta todos los marcos de contenido para permitir la visualización de uno específico.
        """
        self.__frameInicio.grid_forget()
        self.__frameYoutube.grid_forget()
        self.__frameWord.grid_forget()
        self.__framePdf.grid_forget()
        self.__frameJpg.grid_forget()
        self.__framePng.grid_forget()
        self.__frameConfiguracion.grid_forget()

    def __mostrar_ventanas(self, nombre):
        """
        Muestra el marco correspondiente según el nombre proporcionado.

        :param nombre: Nombre de la sección a mostrar.
        """
        self.__ocultar_ventanas()

        if nombre == "Inicio":
            # Configuración y visualización para la sección de Inicio
            self.__frameInicio.grid(row=0, column=3, sticky="n", padx=50)

            self.__frameInicio.grid_columnconfigure(0, weight=3)

            self.__titulo = CTkLabel(self.__frameInicio, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=1, column=0, padx=100, pady=20, columnspan=2)

            self.__informacionInicio = CTkLabel(self.__frameInicio, text="Organizar archivos", font=("Arial", 20))

            self.__informacionInicio.grid(row=2, column=0, pady=20)

            self.__buttonInicio = CTkButton(self.__frameInicio, text="Aceptar", font=("Arial", 20),
                                            fg_color="#607D8B", command=lambda: self.__organizador.archivos())

            self.__buttonInicio.grid(row=3, column=0, pady=20, padx=15, columnspan=2, sticky="ew")

        elif nombre == "Youtube":
            # Configuración y visualización para la sección de Youtube
            self.__frameYoutube.grid(row=0, column=3, sticky="n", padx=50)

            self.__frameYoutube.grid_columnconfigure(0, weight=3)


            self.__titulo = CTkLabel(self.__frameYoutube, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=0, column=0, padx=100, pady=20, columnspan=2)

            self.__informacionYoutube = CTkLabel(self.__frameYoutube, text="Descargar videos o audios de youtube",
                                                 font=("Arial", 15))

            self.__informacionYoutube.grid(row=1, column=0)

            self.__link = CTkLabel(self.__frameYoutube, text="Ingresar Link", font=("Arial", 15))

            self.__link.grid(row=2, column=0)

            self.__inputYoutube = CTkEntry(self.__frameYoutube, width=250)

            self.__inputYoutube.grid(row=3, column=0, pady=20)

            self.__ButonAlta = CTkButton(self.__frameYoutube, text="Alta calidad", fg_color="#607D8B",
                                         command=lambda: self.__youtube.Descargar(
                                             self.__inputYoutube.get(), "Alta", self.__ubicacion)
                                         )
            self.__ButonAlta.grid(row=4, column=0, pady=5)

            self.__ButonBaja = CTkButton(self.__frameYoutube, text="Baja calidad", fg_color="#607D8B",
                                         command=lambda: self.__youtube.Descargar(
                                             self.__inputYoutube.get(), "Baja"
                                             , self.__ubicacion)
                                         )
            self.__ButonBaja.grid(row=5, column=0, pady=5)

            self.__ButonAudio = CTkButton(self.__frameYoutube, text="Audios", fg_color="#607D8B",
                                          command=lambda: self.__youtube.Descargar(
                                              self.__inputYoutube.get(), "Audio"
                                              , self.__ubicacion)
                                          )
            self.__ButonAudio.grid(row=6, column=0, pady=5)

        elif nombre == "Word":
            # Configuración y visualización para la sección de Word
            self.__frameWord.grid(row=0, column=3, sticky="n", padx=50)

            self.__titulo = CTkLabel(self.__frameWord, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=0, column=0, padx=100, pady=20, )

            self.__informacionWord = CTkLabel(self.__frameWord, text="Convertir Documentos a PDF", font=("Arial", 15))

            self.__informacionWord.grid(row=1, column=0, pady=5)

            self.__botonWord = CTkButton(self.__frameWord, fg_color="#607D8B",
                                         text="Subir archivos",
                                         command=lambda: self.__subirDocumentosWord(), font=("Arial", 12))

            self.__botonWord.grid(row=2, column=0, pady=10)

            self.__botonWordConvertidor = CTkButton(self.__frameWord,
                                                    text="Convertir PDF",
                                                    command=lambda: self.__controladorPdfWord.pdf(self.__archivosWord))

        elif nombre == "Pdf":
            # Configuración y visualización para la sección de PDF
            self.__framePdf.grid(row=0, column=3, sticky="n", padx=50)

            self.__titulo = CTkLabel(self.__framePdf, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=0, column=0, padx=100, pady=20, )

            self.__informacionPdf = CTkLabel(self.__framePdf, text="Convertir Documentos a WORD", font=("Arial", 15))

            self.__informacionPdf.grid(row=1, column=0, pady=5)

            self.__botonPdf = CTkButton(self.__framePdf,
                                        text="Subir archivos", fg_color="#607D8B",
                                        command=lambda: self.__subirDocumentosPdf())

            self.__botonPdf.grid(row=2, column=0, pady=5)

            self.__botonPdfConvertidor = CTkButton(self.__framePdf, fg_color="#607D8B",
                                                   text="Convertir a WORD",
                                                   command=lambda: self.__controladorPdfWord.word(self.__archivosPdf))

        elif nombre == "Png":
            # Configuración y visualización para la sección de PNG
            self.__framePng.grid(row=0, column=3, sticky="n", padx=50)

            self.__titulo = CTkLabel(self.__framePng, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=0, column=0, padx=100, pady=20, )

            self.__informacionPng = CTkLabel(self.__framePng, text="Convertir Imagenes a PNG", font=("Arial", 15))

            self.__informacionPng.grid(row=1, column=0, pady=5)

            self.__botonPng = CTkButton(self.__framePng,
                                        text="Subir imagenes", fg_color="#607D8B",
                                        command=lambda: self.__subirImagenesPng())

            self.__botonPng.grid(row=2, column=0, pady=5)

            self.__botonPngConvertidor = CTkButton(self.__framePng, text="Convertir a PNG", fg_color="#df3910",
                                                   command=lambda: self.__controladorImagen.png(self.__archivosPng))

        elif nombre == "Jpg":
            # Configuración y visualización para la sección de JPG
            self.__frameJpg.grid(row=0, column=3, sticky="n", padx=50)

            self.__titulo = CTkLabel(self.__frameJpg, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=0, column=0, padx=100, pady=20, )

            self.__informacionJpg = CTkLabel(self.__frameJpg, text="Convertir Imagenes a JPG", font=("Arial", 15))

            self.__informacionJpg.grid(row=1, column=0, pady=5)

            self.__botonJpg = CTkButton(self.__frameJpg, text="Subir imagenes", fg_color="#607D8B",
                                        command=lambda: self.__subirImagenesJpg())

            self.__botonJpg.grid(row=2, column=0, pady=5)

            self.__botonJpgConvertidor = CTkButton(self.__frameJpg,
                                                   text="Convertir a JPG",
                                                   command=lambda: self.__controladorImagen.jpg(self.__archivosJpg))

        elif nombre == "Configuraciones":
            # Configuración y visualización para la sección de Configuraciones
            self.__frameConfiguracion.grid(row=0,column=3,sticky="n",padx=50)

            self.__titulo = CTkLabel(self.__frameConfiguracion, text="Hestia", font=("Arial", 50))

            self.__titulo.grid(row=0, column=0, padx=100, pady=20)

            self.__ruta = CTkLabel(self.__frameConfiguracion,text="Ubicacion de las carpetas",font=("Arial",15))

            self.__ruta.grid(row=1,column=0, padx=100, pady=5)

            self.__inputUbucacion = CTkEntry(self.__frameConfiguracion,width=200)

            self.__inputUbucacion.insert(0,self.__ubicacion)

            self.__inputUbucacion.grid(row=2,column=0,padx=100,pady=5)

            self.__buttonConfiguracion = CTkButton(self.__frameConfiguracion, text="Guardar", font=("Arial",15)
                                                   ,fg_color="#607D8B",
                                                   command=lambda :self.__Configuraciones.ingresarDatos(
                                                       self.__inputUbucacion.get(),self.__ubicacion
                                                   ))

            self.__buttonConfiguracion.grid(row=3,column=0,padx=100,pady=5)

    def iniciar_aplicacion(self):
        self.__ventana.mainloop()

    def __subirDocumentosWord(self):

        """
        Permite al usuario seleccionar y cargar archivos Word.

        Almacena las rutas de los archivos seleccionados en la variable __archivosWord.
        Habilita el botón de conversión a PDF si se seleccionan archivos.

        :return: None
        """

        self.__subirDocumento = filedialog.askopenfilenames(title="Seleccionar archivos",
                                                            filetypes=[("Archivos de word", "*.docx")])
        # Verifica si se seleccionaron archivos
        if self.__subirDocumento != "":
            self.__botonPdfConvertidor.grid(row=3, column=0, pady=10)

            self.__archivosWord = self.__subirDocumento

    def __subirDocumentosPdf(self):

        """
        Permite al usuario seleccionar y cargar archivos PDF.

        Almacena las rutas de los archivos seleccionados en la variable __archivosPdf.
        Habilita el botón de conversión a Word si se seleccionan archivos.

        :return: None
        """
        self.__subirDocumento = filedialog.askopenfilenames(title="Seleccionar archivos",
                                                            filetypes=[("Archivos de PDF", "*.pdf")])
        print(self.__subirDocumento)

        # Verifica si se seleccionaron archivos
        if self.__subirDocumento:
            self.__botonPdfConvertidor.grid(row=3, column=0, pady=10)
            self.__archivosPdf = self.__subirDocumento

    def __subirImagenesPng(self):

        """
        Permite al usuario seleccionar y cargar imágenes con extensiones .jpeg, .jpg o .svg.

        Almacena las rutas de los archivos seleccionados en la variable __archivosPng.

        :return: None
        """
        self.__archivosPng = None

        # Utiliza el cuadro de diálogo para seleccionar múltiples archivos
        self.__subirImagenes = filedialog.askopenfilenames(title="Seleccionar imágenes",
                                                           filetypes=(
                                                               [("Imágenes", "*.jpeg"),
                                                                ("Imágenes", "*.jpg"),
                                                                ("Imágenes", "*.svg")]))
        print(self.__subirImagenes)

        if self.__subirImagenes != "":
            self.__botonPngConvertidor.grid(row=3, column=0, pady=10)

            self.__archivosPng = self.__subirImagenes

    def __subirImagenesJpg(self):

        """
        Permite al usuario seleccionar y cargar imágenes con extensiones .jpeg, .jpg o .svg.

        Almacena las rutas de los archivos seleccionados en la variable __archivosPng.

        :return: None
        """

        self.__archivosJpg = None

        # Utiliza el cuadro de diálogo para seleccionar múltiples archivos
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
