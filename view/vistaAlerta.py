from tkinter import messagebox


class vistaAlerta():

    def __init__(self):

        self.__alertas = messagebox
        pass


    def informacion(self,info):
        self.__alertas.showinfo("Información", info)


    def error(self,error):
        self.__alertas.showerror("Error",error)