from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox
from verify_email import verify_email
from datetime import datetime
from modules.abb import *

def programar_citas():
    programador = iniciar_arbol()
    
    # Crear ventana para programar citas
    def crear_cita_window():
        
        window = Tk()
        window.title("Programar cita")
        
        # Funcion para enviar la cita
        def enviar_cita():
            tipo = tipo_cita_checkbutton.get()
            placa = placa_entry.get()
            vehiculo = tipo_vehiculo_listbox.get(ACTIVE)
            marca = marca_entry.get()
            modelo = modelo_entry.get()
            propietario = propietario_entry.get()
            telefono = telefono_entry.get()
            correo = correo_entry.get()
            direccion = direccion_entry.get()
            fecha_year = int(fecha_year_entry.get())
            fecha_month = int(fecha_month_entry.get())
            fecha_day = int(fecha_day_entry.get())
            tiempo_hora = int(tiempo_hora_entry.get())
            tiempo_minutos = int(tiempo_minutos_entry.get())           
            
            # Validacion de datos
            if placa_entry.get() == "" or len(placa_entry.get()) > 8 :
                MessageBox.showerror("Error", "El numero de placa debe ser de 1 a 8 caracteres")
                return
            
            if len(tipo_vehiculo_listbox.curselection()) == 0:
                MessageBox.showerror("Error", "Debe seleccionar un tipo de vehiculo")
                return
            
            if len(marca_entry.get()) < 3 or len(marca_entry.get()) > 15:
                MessageBox.showerror("Error", "La marca debe ser de 3 a 15 caracteres")
                return
            
            if len(modelo_entry.get()) < 1 or len(modelo_entry.get()) > 15:
                MessageBox.showerror("Error", "El modelo debe ser de 1 a 15 caracteres")
                return
            
            if len(propietario_entry.get()) < 6 or len(propietario_entry.get()) > 40:
                MessageBox.showerror("Error", "El nombre del propietario debe ser de 6 a 40 caracteres")
                return
            
            if len(telefono_entry.get()) != 20 or telefono_entry.get().isdigit() == False:
                MessageBox.showerror("Error", "El numero de telefono debe ser de 20 digitos")
                return
            
            if not verify_email(correo_entry.get()):
                MessageBox.showerror("Error", "El correo electronico no es valido")
                return
            
            if len(direccion_entry.get()) < 10 or len(direccion_entry.get()) > 40:
                MessageBox.showerror("Error", "La direccion debe ser de 10 a 40 caracteres")
                return
            
            
            # Validar cita fecha y tiempo
            if len(str(fecha_year)) != 4:
                MessageBox.showerror("Error", "El año debe ser un numero de 4 digitos")
                return
            if len(str(fecha_month)) > 2 or fecha_month > 12 or fecha_month < 1:
                MessageBox.showerror("Error", "El mes debe ser un numero de 2 digitos")
                return
            if len(str(fecha_day)) > 2 or fecha_day > 31 or fecha_day < 1:
                MessageBox.showerror("Error", "El dia debe ser un numero de 2 digitos")
                return
            if len(str(tiempo_hora)) > 2 or tiempo_hora > 23 or tiempo_hora < 0:
                MessageBox.showerror("Error", "La hora debe ser un numero de 2 digitos")
                return
            if len(str(tiempo_minutos)) > 2 or tiempo_minutos > 59 or tiempo_minutos < 0:
                MessageBox.showerror("Error", "Los minutos deben ser un numero de 2 digitos")
                return
            
            if len(str(fecha_month)) == 1:
                fecha_month = "0" + str(fecha_month)
            if len(str(fecha_day)) == 1:
                fecha_day = "0" + str(fecha_day)
            if len(str(tiempo_hora)) == 1:
                tiempo_hora = "0" + str(tiempo_hora)
            if len(str(tiempo_minutos)) == 1:
                tiempo_minutos = "0" + str(tiempo_minutos)
             
            fecha_actual = datetime.now()
            fecha_actual = int(str(fecha_actual.year).rjust(4, "0") + str(fecha_actual.month).rjust(2, "0") + str(fecha_actual.day).rjust(2, "0") + str(fecha_actual.hour).rjust(2, "0") + str(fecha_actual.minute).rjust(2, "0"))
            hora_cita = int(str(fecha_year) + str(fecha_month) + str(fecha_day) + str(tiempo_hora) + str(tiempo_minutos))
            if fecha_actual > hora_cita:
                MessageBox.showerror("Error", "La fecha y hora de la cita no puede ser menor a la fecha y hora actual")
                return
            if int(str(hora_cita)[:8]) - int(str(fecha_actual)[:8]) > 10000:
                MessageBox.showerror("Error", "La cita debe estar en un plazo de un año")
                return
            
            programador.agregar_nodo(tipo, placa, vehiculo, marca, modelo, propietario, telefono, correo, direccion, hora_cita)
            guardar_arbol(programador)
            MessageBox.showinfo("Cita programada", "La cita ha sido programada exitosamente")
            window.destroy()
        
        # Elementos del formulario
        tipo_cita_checkbutton = StringVar()
        tipo_cita_label = Label(window, text="Tipo de cita")
        primera_cita = Radiobutton(window, text="Primera cita", variable=tipo_cita_checkbutton, value="Primera cita")
        reinspeccion_cita = Radiobutton(window, text="Reinspección", variable=tipo_cita_checkbutton, value="Reinspeccion")
        tipo_cita_checkbutton.set("Primera cita")
        
        placa_label = Label(window, text="Placa")
        placa_entry = Entry(window)
        
        tipo_vehiculo_label = Label(window, text="Tipo de vehiculo")
        tipo_vehiculo_listbox = Listbox(window, height=8, width=50, selectmode=SINGLE)
        tipos_vehiculo = ["Vehiculo carga liviana <= 3500 kg", 
                        "Vehiculo carga liviana (3500 kg < vehiculo < 8000 kg)", 
                        "Vehiculo carga pesada >= 8000 kg", 
                        "Taxis",
                        'Autobuses, buses, microbuses',
                        'Motocicletas',
                        'Equipo especial de obras',
                        'Equipo especial agricola']
        for tipo in tipos_vehiculo:
            tipo_vehiculo_listbox.insert(END, tipo)
        
        marca_label = Label(window, text="Marca")
        marca_entry = Entry(window)
        
        modelo_label = Label(window, text="Modelo")
        modelo_entry = Entry(window)
        
        propietario_label = Label(window, text="Propietario")
        propietario_entry = Entry(window)
        
        telefono_label = Label(window, text="Telefono")
        telefono_entry = Entry(window)
        
        correo_label = Label(window, text="Correo")
        correo_entry = Entry(window)
        
        direccion_label = Label(window, text="Direccion")
        direccion_entry = Entry(window)
        
        tipo_horario_var = IntVar()
        tipo_horario_label = Label(window, text="Tipo de horario")
        tipo_horario_manual = Radiobutton(window, text="Manual", variable=tipo_horario_var, value=0)
        tipo_horario_automatica = Radiobutton(window, text="Automatica", variable=tipo_horario_var, value=1)
        
        fecha_label = Label(window, text="Fecha")
        fecha_year_entry = Entry(window, width=5)
        fecha_month_entry = Entry(window, width=5)
        fecha_day_entry = Entry(window, width=5)
        
        # Funcion que asegura que solo se puedan ingresar numeros en los campos de fecha y tiempo
        
        def validar_numero_input(action, value_if_allowed):
            if value_if_allowed.strip().isdigit() or value_if_allowed == "":
                return True
            else:
                return False
        
        validar_numero_input_cmd = (window.register(validar_numero_input), '%d', '%P')
        
        
        fecha_year_entry.insert(0, 'AAAA')
        fecha_year_entry.config(fg="grey")
        fecha_year_entry.bind("<FocusIn>", lambda event: focus_in(event, fecha_year_entry, 'AAAA'))
        fecha_year_entry.bind("<FocusOut>", lambda event: focus_out(event, fecha_year_entry, 'AAAA'))
        fecha_year_entry.config(validate="key", validatecommand=validar_numero_input_cmd)
        
        fecha_month_entry.insert(0, 'MM')
        fecha_month_entry.config(fg="grey")
        fecha_month_entry.bind("<FocusIn>", lambda event: focus_in(event, fecha_month_entry, 'MM'))
        fecha_month_entry.bind("<FocusOut>", lambda event: focus_out(event, fecha_month_entry, 'MM'))
        fecha_month_entry.config(validate="key", validatecommand=validar_numero_input_cmd)
        
        fecha_day_entry.insert(0, 'DD')
        fecha_day_entry.config(fg="grey")
        fecha_day_entry.bind("<FocusIn>", lambda event: focus_in(event, fecha_day_entry, 'DD'))
        fecha_day_entry.bind("<FocusOut>", lambda event: focus_out(event, fecha_day_entry, 'DD'))
        fecha_day_entry.config(validate="key", validatecommand=validar_numero_input_cmd)
        
        tiempo_label = Label(window, text="Tiempo")
        tiempo_hora_entry = Entry(window, width=5)
        tiempo_minutos_entry = Entry(window, width=5)
        
        tiempo_hora_entry.insert(0, 'HH')
        tiempo_hora_entry.config(fg="grey")
        tiempo_hora_entry.bind("<FocusIn>", lambda event: focus_in(event, tiempo_hora_entry, 'HH'))
        tiempo_hora_entry.bind("<FocusOut>", lambda event: focus_out(event, tiempo_hora_entry, 'HH'))
        tiempo_hora_entry.config(validate="key", validatecommand=validar_numero_input_cmd)
        
        tiempo_minutos_entry.insert(0, 'MM')
        tiempo_minutos_entry.config(fg="grey")
        tiempo_minutos_entry.bind("<FocusIn>", lambda event: focus_in(event, tiempo_minutos_entry, 'MM'))
        tiempo_minutos_entry.bind("<FocusOut>", lambda event: focus_out(event, tiempo_minutos_entry, 'MM'))
        tiempo_minutos_entry.config(validate="key", validatecommand=validar_numero_input_cmd)
        

        
        # Funciones que permiten que los campos de fecha y tiempo se comporten como placeholders
         
        def focus_in(event, entry, text):
            if entry.get() == text:
                entry.delete(0, END)
                entry.config(fg="black")
        
        def focus_out(event, entry, text):
            if entry.get().strip() == '':
                entry.delete(0, END)
                entry.insert(0, text)
                entry.config(fg="grey")
        
        enviar_boton = Button(window, text="Enviar", command=enviar_cita)
        

        # Posicionamiento de los elementos
        tipo_cita_label.grid(row=0, column=0, padx=10, pady=7)
        primera_cita.grid(row=0, column=1, padx=10, pady=7)
        reinspeccion_cita.grid(row=0, column=2, padx=10, pady=7)

        placa_label.grid(row=1, column=0, padx=10, pady=7)
        placa_entry.grid(row=1, column=1, padx=10, pady=7)

        tipo_vehiculo_label.grid(row=2, column=0, padx=10, pady=7)
        tipo_vehiculo_listbox.grid(row=2, column=1, columnspan=2, padx=10, pady=7)

        marca_label.grid(row=3, column=0, padx=10, pady=7)
        marca_entry.grid(row=3, column=1, padx=10, pady=7)

        modelo_label.grid(row=4, column=0, padx=10, pady=7)
        modelo_entry.grid(row=4, column=1, padx=10, pady=7)

        propietario_label.grid(row=5, column=0, padx=10, pady=7)
        propietario_entry.grid(row=5, column=1, padx=10, pady=7)

        telefono_label.grid(row=6, column=0, padx=10, pady=7)
        telefono_entry.grid(row=6, column=1, padx=10, pady=7)

        correo_label.grid(row=7, column=0, padx=10, pady=7)
        correo_entry.grid(row=7, column=1, padx=10, pady=7)

        direccion_label.grid(row=8, column=0, padx=10, pady=7)
        direccion_entry.grid(row=8, column=1, padx=10, pady=7)

        tipo_horario_label.grid(row=9, column=0, padx=10, pady=7)
        tipo_horario_manual.grid(row=9, column=1, padx=10, pady=7)
        tipo_horario_automatica.grid(row=9, column=2, padx=10, pady=7)

        fecha_label.grid(row=10, column=0, padx=10, pady=7)
        fecha_year_entry.grid(row=10, column=1, padx=5, pady=7)
        fecha_month_entry.grid(row=10, column=2, padx=5, pady=7, sticky=W)
        fecha_day_entry.grid(row=10, column=3, padx=5, pady=7, sticky=W)

        tiempo_label.grid(row=11, column=0, padx=10, pady=7)
        tiempo_hora_entry.grid(row=11, column=1, padx=5, pady=7)
        tiempo_minutos_entry.grid(row=11, column=2, padx=5, pady=7, sticky=W)
        

        enviar_boton.grid(row=12, column=1, padx=10, pady=7)

            
        window.mainloop()

    crear_cita_window()
