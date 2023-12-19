from tkinter import *

def main ():
# Raiz de la interfas
    raiz = Tk()
    raiz.title("Hestia")
    raiz.geometry("550x550")
#Primer frame
    vistaPrincipal = Frame()
    vistaPrincipal.pack()
    vistaPrincipal.config(width="300",height="550")
#Titulo de la aplicacion
    titulo = Label(vistaPrincipal,text="Hestia",font=("Arial",50))
    titulo.pack()
#vista del lista de la aplicacion

    vistaSecundaria = Frame()
    vistaSecundaria.pack()

#Subtitulo
    subTitulo = Label(vistaSecundaria,text="Menu",font=("Arial",30))
    subTitulo.grid(row=0,column=0)
# convertidores
    puntoUno = Label(vistaSecundaria,text="1. Convertidores")
    puntoUno.grid(row=1,column=0)

#
    puntoDos = Label(vistaSecundaria,text="2. Descargar vidoes y audios de youtube")
    puntoDos.grid(row=2,column=0)
#
    puntoTres = Label(vistaSecundaria,text="3. Organizar archivos")
    puntoTres.grid(row=3,column=0)
#
    texto = Entry(vistaSecundaria)
    texto.grid(row=4,column=0)
#Final del la interfaz
    raiz.mainloop()

main()