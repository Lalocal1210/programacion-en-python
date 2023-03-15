import tkinter as tk
from tkinter import messagebox
from tkinter import messagebox

import random

class MatriculaGenerator(tk.Frame):
    def __init__(self, ventana=None):
        super().__init__(ventana)
        self.ventana = ventana
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Nombre
        self.nombre_label = tk.Label(self, text="Nombre:",fg="green")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack()

        # Apellido Paterno
        self.ap_paterno_label = tk.Label(self, text="Apellido Paterno:",fg="green")
        self.ap_paterno_label.pack()
        self.ap_paterno_entry = tk.Entry(self)
        self.ap_paterno_entry.pack()

        # Apellido Materno
        self.ap_materno_label = tk.Label(self, text="Apellido Materno:",fg="green")
        self.ap_materno_label.pack()
        self.ap_materno_entry = tk.Entry(self)
        self.ap_materno_entry.pack()

        # Año de Nacimiento
        self.ano_nacimiento_label = tk.Label(self, text="Año de Nacimiento:",fg="purple")
        self.ano_nacimiento_label.pack()
        self.ano_nacimiento_entry = tk.Entry(self)
        self.ano_nacimiento_entry.pack()

        #Año actual
        self.añoa_label = tk.Label(self, text="Año actual:",fg="purple")
        self.añoa_label.pack()
        self.añoa_entry = tk.Entry(self)
        self.añoa_entry.pack()

        # Carrera
        self.carrera_label = tk.Label(self, text="Carrera:",fg="blue")
        self.carrera_label.pack()
        self.carrera_entry = tk.Entry(self)
        self.carrera_entry.pack()
        

        # Botón para generar la matrícula
        self.generate_button = tk.Button(self, text="Generar Matrícula", command=self.generate_matricula, fg="orange")
        self.generate_button.pack()

    def generate_matricula(self):
        # Obtener la información del usuario
        nombre = self.nombre_entry.get()
        ap_paterno = self.ap_paterno_entry.get()
        ap_materno = self.ap_materno_entry.get()
        ano_nacimiento = self.ano_nacimiento_entry.get()
        carrera = self.carrera_entry.get()
        añoa = self.añoa_entry.get()
    


        # Generar los dígitos aleatorios de la matrícula
        digitos_aleatorios = ''.join([str(random.randint(0, 9)) for i in range(3)])

        # Generar la matrícula
        matricula = f"{añoa[-2:]}{ano_nacimiento[-2:]}{nombre[0]}{ap_paterno[0]}{ap_materno[0]}{digitos_aleatorios}{carrera[:3].upper()}"

        # Mostrar la matrícula en un MessageBox
        tk.messagebox.showinfo("Matrícula Generada", matricula,fg="black")

root = tk.Tk()
app = MatriculaGenerator(ventana=root)
app.mainloop()

