import tkinter as tk
import random
from datetime import datetime

class MatriculaGenerator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Nombre
        self.nombre_label = tk.Label(self, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack()

        # Apellido Paterno
        self.ap_paterno_label = tk.Label(self, text="Apellido Paterno:")
        self.ap_paterno_label.pack()
        self.ap_paterno_entry = tk.Entry(self)
        self.ap_paterno_entry.pack()

        # Apellido Materno
        self.ap_materno_label = tk.Label(self, text="Apellido Materno:")
        self.ap_materno_label.pack()
        self.ap_materno_entry = tk.Entry(self)
        self.ap_materno_entry.pack()

        # Año de Nacimiento
        self.ano_nacimiento_label = tk.Label(self, text="Año de Nacimiento:")
        self.ano_nacimiento_label.pack()
        self.ano_nacimiento_entry = tk.Entry(self)
        self.ano_nacimiento_entry.pack()

        # Carrera
        self.carrera_label = tk.Label(self, text="Carrera:")
        self.carrera_label.pack()
        self.carrera_entry = tk.Entry(self)
        self.carrera_entry.pack()

        # Botón para generar la matrícula
        self.generate_button = tk.Button(self, text="Generar Matrícula", command=self.generate_matricula)
        self.generate_button.pack()

    def generate_matricula(self):
        # Obtener la información del usuario
        nombre = self.nombre_entry.get()
        ap_paterno = self.ap_paterno_entry.get()
        ap_materno = self.ap_materno_entry.get()
        ano_nacimiento = self.ano_nacimiento_entry.get()
        carrera = self.carrera_entry.get()

        # Obtener el año actual
        ano_actual = datetime.now().year % 100

        # Generar los dígitos aleatorios de la matrícula
        digitos_aleatorios = ''.join([str(random.randint(0, 9)) for i in range(3)])

        # Generar la matrícula
        matricula = f"{ano_actual}{ano_nacimiento[-2:]}{nombre[0]}{ap_paterno[0]}{ap_materno[0]}{digitos_aleatorios}{carrera[:3]}"

        # Mostrar la matrícula en un MessageBox
        tk.messagebox.showinfo("Matrícula Generada", matricula)

root = tk.Tk()
app = MatriculaGenerator(master=root)
app.mainloop()

