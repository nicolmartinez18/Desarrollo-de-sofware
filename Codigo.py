import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
print("libreria leida")

#Crear interfaz

ventana = tk.Tk()
ventana.title("Interfaz Grafica")
ventana.geometry("400x500")

#Crear Comandos
def imagen():
    img=Image.open("C:/Users/HP/Downloads/imagen 1.jpeg")
    new_img=img.resize((300,556))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana, image=render)
    img1.image=render
    img1.place(x=10, y=30)
    
    img=Image.open("C:/Users/HP/Downloads/imagen 2.jpeg")
    new_img=img.resize((300,556))
    render=ImageTk.PhotoImage(new_img)
    img2=Label(ventana, image=render)
    img2.image=render
    img2.place(x=10, y=30)
    
def mensaje():
    salir=messagebox.askquestion("salir", "¿deseas salir  de la interfaz?")
    if salir=="yes":
        ventana.quit()
        ventana.detroy()
        
        
# Crear botones
boton = tk.Button(ventana, text = "abrir imagen", height=2, width=28)
boton.place(x=100, y=350)

boton1 = tk.Button(ventana, text= "salir", height=2, width=28)
boton1.place(x=100, y=450)


ventana.mainloop()

