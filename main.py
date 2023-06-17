from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from PIL import Image, ImageTk
import sv_ttk
import os
from modules.programar_citas import programar_citas

# Funcion que asegura que solo se puedan ingresar numeros en los campos de fecha y tiempo

def validar_numero_input(action, value_if_allowed):
    if value_if_allowed.strip().isdigit() or value_if_allowed == "":
        return True
    else:
        return False


# Funcion configuracion
def configuracion():
    window = Toplevel()
    window.title("Configuración")

    configuracion_label = Label(window, text="Configuración", font=("Arial", 20), fg='white', bg='#0A6AA6')
    cantidad_lineas_label = Label(window, text="Cantidad de líneas de revisión:", fg='white', font=("Arial", 12))
    cantidad_lineas_combobox = ttk.Combobox(window, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
    horario_label = Label(window, text="Horario de atención:", fg='white', font=("Arial", 12))
    hora_inicio_label = Label(window, text="Hora inicio", fg='white', font=("Arial", 12))
    hora_inicio_combobox = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
    hora_inicio_combobox.current(6)
    hora_final_label = Label(window, text="Hora final", fg="white", font=("Arial", 12))
    hora_final_combobox = ttk.Combobox(window, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
    hora_final_combobox.current(21)
    minutos_revision_label = Label(window, text="Minutos de revisión:", fg='white', font=("Arial", 12))
    minutos_revision_combobox = ttk.Combobox(window, values=[5, 10, 15, 20, 25, 30, 35, 40, 45])
    dias_maximo_reinspeccion_label = Label(window, text="Días máximos de días naturales para reinspección:", fg='white', font=("Arial", 12))
    dias_maximo_reinspeccion_combobox = ttk.Combobox(window, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60])
    fallas_graves_maximo_label = Label(window, text="Fallas graves máximas para sacar vehículo de circulación:", fg='white', font=("Arial", 12))
    fallas_graves_maximo_entry = Entry(window, width=20, font=("Arial", 12))
    validar_numero_input_cmd = (window.register(validar_numero_input), '%d', '%P')
    fallas_graves_maximo_entry.config(validate="key", validatecommand=validar_numero_input_cmd)
    cantidad_meses_citas_label = Label(window, text="Cantidad de meses para programar citas:", fg='white', font=("Arial", 12))
    cantidad_meses_citas_combobox = ttk.Combobox(window, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    iva_label = Label(window, text="IVA agregado sobre la tarifa:", fg='white', font=("Arial", 12))
    iva_combobox = ttk.Combobox(window, values=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 
                                                1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 
                                                2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 
                                                3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 
                                                4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 
                                                5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 
                                                6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 
                                                7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 
                                                8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 
                                                9.0, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 
                                                10.0, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 
                                                11.0, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 
                                                12.0, 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 12.7, 12.8, 12.9, 13.0])
    configurar_boton = Button(window, text="Configurar", width=10, height=2, bg='#0A6AA6', fg='white', font=("Arial", 12), command=lambda: MessageBox.showinfo("Configuración", "Configuración guardada con éxito"))
    
    configuracion_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    cantidad_lineas_label.grid(row=1, column=0, padx=10, pady=10)
    cantidad_lineas_combobox.grid(row=1, column=1, padx=10, pady=10)
    horario_label.grid(row=2, column=0, padx=10, pady=10)
    hora_inicio_label.grid(row=3, column=0, padx=10, pady=10)
    hora_inicio_combobox.grid(row=3, column=1, padx=10, pady=10)
    hora_final_label.grid(row=4, column=0, padx=10, pady=10)
    hora_final_combobox.grid(row=4, column=1, padx=10, pady=10)
    minutos_revision_label.grid(row=5, column=0, padx=10, pady=10)
    minutos_revision_combobox.grid(row=5, column=1, padx=10, pady=10)
    dias_maximo_reinspeccion_label.grid(row=6, column=0, padx=10, pady=10)
    dias_maximo_reinspeccion_combobox.grid(row=6, column=1, padx=10, pady=10)
    fallas_graves_maximo_label.grid(row=7, column=0, padx=10, pady=10)
    fallas_graves_maximo_entry.grid(row=7, column=1, padx=10, pady=10)
    cantidad_meses_citas_label.grid(row=8, column=0, padx=10, pady=10)
    cantidad_meses_citas_combobox.grid(row=8, column=1, padx=10, pady=10)
    iva_label.grid(row=9, column=0, padx=10, pady=10)
    iva_combobox.grid(row=9, column=1, padx=10, pady=10)
    configurar_boton.grid(row=10, column=0, columnspan=2, padx=10, pady=10)
    

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
    
    boton_cancelar = Button(ventana, text="Cancelar citas", command=lambda: print("Cancelar citas"), bg="#0A6AA6", height=2, width=30)
    boton_cancelar.place(relx= 0.5, y = 250, anchor=N)
    
    boton_ingreso = Button(ventana, text="Ingreso de vehículos a la estación", command=lambda: print("Ingreso de vehículos a la estación"), bg="#0D7BA6", height=2, width=30)
    boton_ingreso.place(relx= 0.5, y = 300, anchor=N)
    
    boton_tablero = Button(ventana, text="Tablero de revisión", command=lambda: print("Tablero de revisión"), bg="#91F2F2", height=2, width=30)
    boton_tablero.place(relx= 0.5, y = 350, anchor=N)
    
    boton_lista = Button(ventana, text="Lista de fallas", command=lambda: print("Lista de fallas"), bg="#0D7BA6", height=2, width=30)
    boton_lista.place(relx= 0.5, y = 400, anchor=N)
    
    boton_configuracion = Button(ventana, text="Configuración del sistema", command=configuracion, bg="#CFC9F2", height=2, width=30)
    boton_configuracion.place(relx= 0.5, y = 450, anchor=N)
    
    boton_ayuda = Button(ventana, text="Ayuda", command=lambda: print("Ayuda"), bg="#0A6AA6", height=2, width=30)
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

