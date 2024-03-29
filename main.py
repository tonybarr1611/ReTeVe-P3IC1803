from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from PIL import Image, ImageTk
import sv_ttk
import os
from modules.programar_citas import programar_citas
from modules.configuracion import configuracion
from modules.cancelar_citas import cancelar_citas
from modules.ingreso_citas import ingreso_citas
from modules.tableros_citas import tablero_citas
from modules.fallas_citas import fallas_citas

# Funcion acerca de
def acerca_de():
    MessageBox.showinfo("Acerca de", "ReTeVe\n\nVersión 1.0\n\nDesarrollado por:\n- Anthony Barrantes Jimenez\n- Francisco Kuo Liu\n\n 19/06/2023")

# Función principal de la ventana principal
def main(ventana):
    # Se crea la ventana con su titulo, geometria y se bloquea el tamaño de la ventana
    ventana.title("ReTeVe")
    ventana.geometry("700x700")
    ventana.minsize(700,700)
    ventana.maxsize(700,700)
    
    # Icono de la ventana
    ventana.iconbitmap("assets/logo.ico")
    # Despliega una imagen en el centro de la ventana, parte superior
    logo = ImageTk.PhotoImage(Image.open("assets/title_logo.png").resize((360, 96), Image.LANCZOS))
    logo_label = Label(ventana, image=logo)
    logo_label.image = logo 
    logo_label.place(x= 160, y= 50)

    # Botones
    boton_programar = Button(ventana, text="Programar citas", command=programar_citas, bg="#CFC9F2", height=2, width=30)
    boton_programar.place(relx= 0.5, y= 200, anchor=N)
    
    boton_cancelar = Button(ventana, text="Cancelar citas", command=cancelar_citas, bg="#0A6AA6", height=2, width=30)
    boton_cancelar.place(relx= 0.5, y = 250, anchor=N)
    
    boton_ingreso = Button(ventana, text="Ingreso de vehículos a la estación", command=ingreso_citas, bg="#0D7BA6", height=2, width=30)
    boton_ingreso.place(relx= 0.5, y = 300, anchor=N)
    
    boton_tablero = Button(ventana, text="Tablero de revisión", command=tablero_citas, bg="#91F2F2", height=2, width=30)
    boton_tablero.place(relx= 0.5, y = 350, anchor=N)
    
    boton_lista = Button(ventana, text="Lista de fallas", command=fallas_citas, bg="#0D7BA6", height=2, width=30)
    boton_lista.place(relx= 0.5, y = 400, anchor=N)
    
    boton_configuracion = Button(ventana, text="Configuración del sistema", command=configuracion, bg="#CFC9F2", height=2, width=30)
    boton_configuracion.place(relx= 0.5, y = 450, anchor=N)
    
    boton_ayuda = Button(ventana, text="Ayuda", command= lambda: os.system("assets\manual.pdf"), bg="#0A6AA6", height=2, width=30)
    boton_ayuda.place(relx= 0.5, y = 500, anchor=N)
    
    boton_acerca_de = Button(ventana, text="Acerca de", command=acerca_de, bg="#0D7BA6", height=2, width=30)
    boton_acerca_de.place(relx= 0.5, y = 550, anchor=N)
    
    boton_salir = Button(ventana, text="Salir", command=lambda: exit(), bg="#91F2F2", height=2, width=30)
    boton_salir.place(relx= 0.5, y = 600, anchor=N)
    
# Inicia la ventana principal
root = Tk()
main(root)
sv_ttk.set_theme("dark")
root.mainloop()

