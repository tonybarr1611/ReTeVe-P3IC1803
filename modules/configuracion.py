from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from PIL import Image, ImageTk
import sv_ttk

# Funcion que asegura que solo se puedan ingresar numeros en los campos de fecha y tiempo
def validar_numero_input(action, value_if_allowed):
    if value_if_allowed.strip().isdigit() or value_if_allowed == "":
        return True
    else:
        return False


# Funcion configuracion
def configuracion():
    window = Toplevel()
    sv_ttk.set_theme("dark")
    window.title("Configuración")

    configuracion_label = Label(window, text="Configuración", font=("Arial", 20), fg='white', bg='#0A6AA6')
    cantidad_lineas_label = Label(window, text="Cantidad de líneas de revisión:", fg='white', font=("Arial", 12))
    cantidad_lineas_combobox = ttk.Combobox(window, values= [i for i in range(1, 26)])
    horario_label = Label(window, text="Horario de atención:", fg='white', font=("Arial", 12))
    hora_inicio_label = Label(window, text="Hora inicio", fg='white', font=("Arial", 12))
    hora_inicio_combobox = ttk.Combobox(window, values=[i for i in range(0, 24)])
    hora_inicio_combobox.current(6)
    hora_final_label = Label(window, text="Hora final", fg="white", font=("Arial", 12))
    hora_final_combobox = ttk.Combobox(window, values=[i for i in range(0, 24)])
    hora_final_combobox.current(21)
    minutos_revision_label = Label(window, text="Minutos de revisión:", fg='white', font=("Arial", 12))
    minutos_revision_combobox = ttk.Combobox(window, values=[5, 10, 15, 20, 25, 30, 35, 40, 45])
    dias_maximo_reinspeccion_label = Label(window, text="Días máximos de días naturales para reinspección:", fg='white', font=("Arial", 12))
    dias_maximo_reinspeccion_combobox = ttk.Combobox(window, values=[i for i in range(1, 61)])
    fallas_graves_maximo_label = Label(window, text="Fallas graves máximas para sacar vehículo de circulación:", fg='white', font=("Arial", 12))
    fallas_graves_maximo_entry = Entry(window, width=20, font=("Arial", 12))
    validar_numero_input_cmd = (window.register(validar_numero_input), '%d', '%P')
    fallas_graves_maximo_entry.config(validate="key", validatecommand=validar_numero_input_cmd)
    cantidad_meses_citas_label = Label(window, text="Cantidad de meses para programar citas:", fg='white', font=("Arial", 12))
    cantidad_meses_citas_combobox = ttk.Combobox(window, values=[i for i in range(1, 13)])
    iva_label = Label(window, text="IVA agregado sobre la tarifa:", fg='white', font=("Arial", 12))
    
    iva_combobox = ttk.Combobox(window, values=[i / 10 for i in range(131)])
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