from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from PIL import Image, ImageTk
import sv_ttk
import json

# Funcion que asegura que solo se puedan ingresar numeros en los campos de fecha y tiempo
def validar_numero_input(action, value_if_allowed):
    if value_if_allowed.strip().isdigit() or value_if_allowed == "":
        return True
    else:
        return False


# Funcion configuracion
def configuracion():
    def guardar_configuracion():
        with open("modules/configuracion.dat", "r") as file:
            configuracion_dict = json.loads(file.read())
        if configuracion_dict['cantidad_lineas'] != cantidad_lineas_combobox.get():
            with open("modules/estaciones.dat", "r") as file:
                estaciones_dict = json.loads(file.read())
                if len(estaciones_dict) > int(cantidad_lineas_combobox.get()):
                    print(int(cantidad_lineas_combobox.get()), len(estaciones_dict))
                    for n in range(int(cantidad_lineas_combobox.get()), len(estaciones_dict)):
                        print(n)
                        if estaciones_dict[str(n + 1)]['espera'] == {} and estaciones_dict[str(n + 1)]["revision"] == {"1": "", "2": "", "3": "", "4": "", "5": ""}:
                            del estaciones_dict[str(n + 1)]
                        else:
                            return MessageBox.showerror("Configuración", "No se puede reducir la cantidad de líneas mientras haya citas en espera o en revisión")
                else:
                    for n in range(len(estaciones_dict), int(cantidad_lineas_combobox.get())):
                        estaciones_dict[str(n + 1)] = ({"espera": {}, "revision": {"1": "", "2": "", "3": "", "4": "", "5": ""}})
                with open("modules/estaciones.dat", "w") as file:
                    file.write(json.dumps(estaciones_dict))

        configuracion_dict = {}
        configuracion_dict['cantidad_lineas'] = cantidad_lineas_combobox.get()
        configuracion_dict['hora_inicio'] = hora_inicio_combobox.get()
        configuracion_dict['hora_final'] = hora_final_combobox.get()
        configuracion_dict['minutos_revision'] = minutos_revision_combobox.get()
        configuracion_dict['dias_maximo_reinspeccion'] = dias_maximo_reinspeccion_combobox.get()
        if fallas_graves_maximo_entry.get() == "" or fallas_graves_maximo_entry.get() == "0":
            return MessageBox.showerror("Configuración", "El número de fallas graves máximo no puede ser 0")
        configuracion_dict['fallas_graves_maximo'] = fallas_graves_maximo_entry.get()
        configuracion_dict['cantidad_meses_citas'] = cantidad_meses_citas_combobox.get()
        configuracion_dict['iva'] = iva_combobox.get()
        if tarifa1_entry.get() == "" or tarifa2_entry.get() == "" or tarifa3_entry.get() == "" or tarifa4_entry.get() == "" or tarifa5_entry.get() == "" or tarifa6_entry.get() == "" or tarifa7_entry.get() == "" or tarifa8_entry.get() == "":
            return MessageBox.showerror("Configuración", "No puede haber campos vacíos (tarifas)")
        if not tarifa1_entry.get().isnumeric() or not tarifa2_entry.get().isnumeric() or not tarifa3_entry.get().isnumeric() or not tarifa4_entry.get().isnumeric() or not tarifa5_entry.get().isnumeric() or not tarifa6_entry.get().isnumeric() or not tarifa7_entry.get().isnumeric() or not tarifa8_entry.get().isnumeric():
            return MessageBox.showerror("Configuración", "Las tarifas deben ser números")
        if int(tarifa1_entry.get()) == 0 or int(tarifa2_entry.get()) == 0 or int(tarifa3_entry.get()) == 0 or int(tarifa4_entry.get()) == 0 or int(tarifa5_entry.get()) == 0 or int(tarifa6_entry.get()) == 0 or int(tarifa7_entry.get()) == 0 or int(tarifa8_entry.get()) == 0:
            return MessageBox.showerror("Configuración", "Las tarifas no pueden ser 0")
        configuracion_dict['Vehiculo carga liviana <= 3500 kg'] = tarifa1_entry.get()
        configuracion_dict['Vehiculo carga liviana (3500 kg < vehiculo < 8000 kg)'] = tarifa2_entry.get()
        configuracion_dict['Vehiculo carga pesada >= 8000 kg'] = tarifa3_entry.get()
        configuracion_dict['Taxis'] = tarifa4_entry.get()
        configuracion_dict['Autobuses, buses, microbuses'] = tarifa5_entry.get()
        configuracion_dict['Motocicletas'] = tarifa6_entry.get()
        configuracion_dict['Equipo especial de obras'] = tarifa7_entry.get()
        configuracion_dict['Equipo especial agricola'] = tarifa8_entry.get()
        
        with open('modules/configuracion.dat', 'w') as file:
            file.write(json.dumps(configuracion_dict))
            
        return MessageBox.showinfo("Configuración", "Configuración guardada con éxito")
    
    def cargar_configuracion():
        with open('modules/configuracion.dat', 'r') as file:
            configuracion_dict = json.loads(file.read())
        cantidad_lineas_combobox.set(int(configuracion_dict['cantidad_lineas']))
        hora_inicio_combobox.set(int(configuracion_dict['hora_inicio']))
        hora_final_combobox.set(int(configuracion_dict['hora_final']))
        minutos_revision_combobox.set(int(configuracion_dict['minutos_revision']))
        dias_maximo_reinspeccion_combobox.set(int(configuracion_dict['dias_maximo_reinspeccion']))
        fallas_graves_maximo_entry.insert(0, configuracion_dict['fallas_graves_maximo'])
        cantidad_lineas_combobox.set(int(configuracion_dict['cantidad_lineas']))
        cantidad_meses_citas_combobox.set(int(configuracion_dict['cantidad_meses_citas']))
        iva_combobox.set(float(configuracion_dict['iva']))
        tarifa1_entry.insert(0, configuracion_dict['Vehiculo carga liviana <= 3500 kg'])
        tarifa2_entry.insert(0, configuracion_dict['Vehiculo carga liviana (3500 kg < vehiculo < 8000 kg)'])
        tarifa3_entry.insert(0, configuracion_dict['Vehiculo carga pesada >= 8000 kg'])
        tarifa4_entry.insert(0, configuracion_dict['Taxis'])
        tarifa5_entry.insert(0, configuracion_dict['Autobuses, buses, microbuses'])
        tarifa6_entry.insert(0, configuracion_dict['Motocicletas'])
        tarifa7_entry.insert(0, configuracion_dict['Equipo especial de obras'])
        tarifa8_entry.insert(0, configuracion_dict['Equipo especial agricola'])
        return
    
    window = Toplevel()
    sv_ttk.set_theme("dark")
    window.title("Configuración")

    configuracion_label = Label(window, text="Configuración", font=("Arial", 20), fg='white', bg='#0A6AA6')
    cantidad_lineas_label = Label(window, text="Cantidad de líneas de revisión:", fg='white', font=("Arial", 12))
    cantidad_lineas_combobox = ttk.Combobox(window, values= [i for i in range(1, 26)])
    horario_label = Label(window, text="Horario de atención:", fg='white', font=("Arial", 12))
    hora_inicio_label = Label(window, text="Hora inicio", fg='white', font=("Arial", 12))
    hora_inicio_combobox = ttk.Combobox(window, values=[i for i in range(0, 24)])
    hora_final_label = Label(window, text="Hora final", fg="white", font=("Arial", 12))
    hora_final_combobox = ttk.Combobox(window, values=[i for i in range(0, 24)])
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
    
    iva_combobox = ttk.Combobox(window, values=[i / 10 for i in range(201)])
    configurar_boton = Button(window, text="Configurar", width=10, height=2, bg='#0A6AA6', fg='white', font=("Arial", 12), command=guardar_configuracion)
    
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
    
    tarifa_label = Label(window, text="Tarifas", font=("Arial", 14), fg='white', bg='#0A6AA6')
    tarifa_label.grid(row=11, column=0, columnspan=2, padx=10, pady=10)
    
    tarifa1_label = Label(window, text="Vehiculo carga liviana <= 3500 kg:", fg='white', font=("Arial", 10))
    tarifa1_label.grid(row=12, column=0, padx=10, pady=10)
    tarifa1_entry = Entry(window, width=20, font=("Arial", 10))
    tarifa1_entry.grid(row=12, column=1, padx=10, pady=10)
    
    tarifa2_label = Label(window, text="Vehiculo carga liviana (3500 kg < vehiculo < 8000 kg):", fg='white', font=("Arial", 10))
    tarifa2_label.grid(row=13, column=0, padx=10, pady=10)
    tarifa2_entry = Entry(window, width=20, font=("Arial", 10))
    tarifa2_entry.grid(row=13, column=1, padx=10, pady=10)
    
    tarifa3_label = Label(window, text="Vehiculo carga pesada >= 8000 kg:", fg='white', font=("Arial", 10))
    tarifa3_label.grid(row=14, column=0, padx=10, pady=10)
    tarifa3_entry = Entry(window, width=20, font=("Arial", 10))
    tarifa3_entry.grid(row=14, column=1, padx=10, pady=10)
    
    tarifa4_label = Label(window, text="Taxis:", fg='white', font=("Arial", 10))
    tarifa4_label.grid(row=15, column=0, padx=10, pady=10)
    tarifa4_entry = Entry(window, width=20, font=("Arial", 10))
    tarifa4_entry.grid(row=15, column=1, padx=10, pady=10)
    
    tarifa5_label = Label(window, text="Autobuses, buses, microbuses:", fg='white', font=("Arial", 10))
    tarifa5_label.grid(row=16, column=0, padx=10, pady=10)
    tarifa5_entry = Entry(window, width=20, font=("Arial", 10))
    tarifa5_entry.grid(row=16, column=1, padx=10, pady=10)
    
    tarifa6_label = Label(window, text="Motocicletas:", fg='white', font=("Arial", 10))
    tarifa6_label.grid(row=17, column=0, padx=10, pady=10)
    tarifa6_entry = Entry(window, width=20, font=("Arial", 10))
    tarifa6_entry.grid(row=17, column=1, padx=10, pady=10)

    tarifa7_label = Label(window, text="Equipo especial de obras:", fg='white', font=("Arial", 10))
    tarifa7_label.grid(row=18, column=0, padx=10, pady=10)
    tarifa7_entry = Entry(window, width=20, font=("Arial", 10))
    tarifa7_entry.grid(row=18, column=1, padx=10, pady=10)
    
    tarifa8_label = Label(window, text="Equipo especial agricola:", fg='white', font=("Arial", 10))
    tarifa8_label.grid(row=19, column=0, padx=10, pady=10)
    tarifa8_entry = Entry(window, width=20, font=("Arial", 10))
    tarifa8_entry.grid(row=19, column=1, padx=10, pady=10)
    
    configurar_boton.grid(row=20, column=0, columnspan=2, padx=10, pady=10)
    
    cargar_configuracion()