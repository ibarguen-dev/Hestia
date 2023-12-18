from tkinter import *

def main ():
# Raiz de la interfas
    raiz = Tk()
    raiz.title("Hestia")
    raiz.geometry("550x550")
#Primer frame
    vistaPrincipal = Frame()
    vistaPrincipal.pack()
    vistaPrincipal.pack(fill="both",expand="True")
#Titulo de la aplicacion
    titulo = Label(vistaPrincipal,text="Hestia",font=("Arial",50))
    titulo.pack()
#vista del lista de la aplicacion

    vistaSecundaria = Frame()
#    vistaSecundaria.pack(row=0,grid=0)
#Fianl del la interfaz
    raiz.mainloop()

main()