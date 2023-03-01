from tkinter import *
from tkinter import messagebox
#5.-agregar funcion de mensaje
def mostrarmensaje():
    messagebox.showinfo("informacion","te informo que")
    messagebox.showerror("error","perdon te falle")
    print(messagebox.askokcancel("pregunta","seguro que quieres guardar?"))
    
    
    
#6.-Funcion agregar Botones
def agregarBoton():
    botonverde.config(text="+",bg="green")
    botonnuevo=Button(seccion3,text="Boton nuevo")
    botonnuevo.pack()
#1.Generar una ventana 
ventana= Tk()
ventana.title("Ejemplo 3 Frames")
ventana.geometry("600x400")

#2. Agregar frames
seccion1= Frame(ventana,bg="red") 
seccion1.pack(expand=True,fill='both')

seccion2= Frame(ventana,bg="gray") 
seccion2.pack(expand=True,fill='both')

seccion3= Frame(ventana,bg="purple") 
seccion3.pack(expand=True,fill='both')

#3.Agregamos botones
botonazul=Button(seccion1,text="soy el boton azul",bg="blue",command=mostrarmensaje)
botonazul.place(x=60,y=60,width=100,height=30)
botonamarillo=Button(seccion2,text="soy el boton amarillo",bg="yellow")
botonamarillo.grid(row=1,column=2)
botonnegro=Button(seccion2,text="soy el boton rojo",bg="#fc002a")
botonnegro.grid(row=0,column=0)
botonverde=Button(seccion3,text="soy el boton verde",fg="green",command=agregarBoton)
botonverde.pack()


ventana.mainloop()