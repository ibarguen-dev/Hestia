import tkinter as tk

class Modelo:
    def __init__(self):
        self.valor = 0

    def obtener_valor(self):
        return self.valor

    def establecer_valor(self, nuevo_valor):
        self.valor = nuevo_valor

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador

        self.ventana = tk.Tk()
        self.ventana.title("Ejemplo MVC")

        self.etiqueta = tk.Label(self.ventana, text="Valor:")
        self.etiqueta.pack()

        self.entry_valor = tk.Entry(self.ventana)
        self.entry_valor.pack()

        self.boton_actualizar = tk.Button(self.ventana, text="Actualizar", command=self.actualizar_valor)
        self.boton_actualizar.pack()

    def actualizar_valor(self):
        nuevo_valor = int(self.entry_valor.get())
        self.controlador.actualizar_valor(nuevo_valor)

    def mostrar_valor(self, nuevo_valor):
        self.entry_valor.delete(0, tk.END)
        self.entry_valor.insert(0, str(nuevo_valor))

    def iniciar_aplicacion(self):
        self.ventana.mainloop()

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

        # Conectar la vista con el controlador
        self.vista.controlador = self

    def actualizar_valor(self, nuevo_valor):
        self.modelo.establecer_valor(nuevo_valor)
        self.vista.mostrar_valor(self.modelo.obtener_valor())

if __name__ == "__main__":
    # Crear instancias del modelo, vista y controlador
    modelo = Modelo()
    vista = Vista(None)
    controlador = Controlador(modelo, vista)

    # Conectar la vista con el controlador después de su creación
    vista.controlador = controlador

    # Iniciar la aplicación
    vista.iniciar_aplicacion()
