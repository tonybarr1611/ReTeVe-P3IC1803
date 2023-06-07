from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox

class Nodo:
    def __init__(self, cita, tipo, placa, vehiculo, marca, modelo, propietario, telefono, correo, direccion, fecha):
        self.cita = cita
        self.tipo = tipo
        self.placa = placa
        self.vehiculo = vehiculo
        self.marca = marca
        self.modelo = modelo
        self.propietario = propietario
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.fecha = fecha
        self.izquierda = None
        self.derecha = None

class ProgramarCitas:
    def __init__(self):
        self.root = None
        self.contador_citas = 1
        
    def insertar_cita(self, numero_cita, tipo_cita, placa, vehiculo, marca, modelo, propietario, telefono, correo, direccion, fecha):
        nuevo_nodo = Nodo(numero_cita, tipo_cita, placa, vehiculo, marca, modelo, propietario, telefono, correo, direccion, fecha)
    
        if self.root is None:
            self.root = nuevo_nodo
        else:
            self._insertar_recursivo(self.root, nuevo_nodo)

    def _insertar_recursivo(self, nodo_actual, nuevo_nodo):
        if nuevo_nodo.fecha < nodo_actual.fecha:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.izquierda, nuevo_nodo)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.derecha, nuevo_nodo)
    
    def get_cuenta_cita(self):
        return self.contador_citas
    
    def aumentar_contador_cita(self):
        self.contador_citas += 1
    
    def buscar_cita_disponible(self, nodo_actual, lista_citas, fecha_actual):
        if nodo_actual is None:
            return
        
        if nodo_actual.fecha > fecha_actual:
            lista_citas.append(nodo_actual.fecha)
        
        self.buscar_cita_disponible(nodo_actual.izquierda, lista_citas, fecha_actual)
        self.buscar_cita_disponible(nodo_actual.derecha, lista_citas, fecha_actual)

def crear_cita_window():
    programador = ProgramarCitas()
    
    window = Tk()
    window.title("Programar cita")
    
    def enviar_cita():
        numero_cita = programador.get_cuenta_cita()
        tipo_cita = tipo_cita_checkbutton.get()
        placa = placa_entry.get()
        vehiculo = tipo_vehiculo_listbox.get()
        marca = marca_entry.get()
        modelo = modelo_entry.get()
        propietario = propietario_entry.get()
        telefono = telefono_entry.get()
        correo = correo_entry.get()
        direccion = direccion_entry.get()
        fecha = fecha_entry.get()
        
        programador.insertar_cita(numero_cita, tipo_cita, placa, vehiculo, marca, modelo, propietario, telefono, correo, direccion, fecha)
        programador.aumentar_contador_cita()
        
        # Validar correo
        
        
        # Validar cita fecha y tiempo

        
        MessageBox.showinfo("Cita programada", "La cita ha sido programada exitosamente")
        window.destroy()
    
    # Elementos del formulario
    tipo_cita_checkbutton = StringVar()
    tipo_cita_label = Label(window, text="Tipo de cita")
    primera_cita = Radiobutton(window, text="Primera cita", variable=tipo_cita_checkbutton, value="Primera cita")
    reinspeccion_cita = Radiobutton(window, text="Reinspección", variable=tipo_cita_checkbutton, value="Reinspeccion")
    
    placa_label = Label(window, text="Placa")
    placa_entry = Entry(window)
    
    tipo_vehiculo_label = Label(window, text="Tipo de vehiculo")
    tipo_vehiculo_listbox = Listbox(window, height=4)
    tipos_vehiculo = ["Automovil", "Camioneta", "Campero", "Motocicleta"]
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
    fecha_entry = Entry(window)
    
    tiempo_label = Label(window, text="Tiempo")
    tiempo_entry = Entry(window)
    
    enviar_boton = Button(window, text="Enviar", command=enviar_cita)
    
    # Posicionamiento de los elementos
    tipo_cita_label.grid(row=0, column=0, padx=10, pady=10)
    primera_cita.grid(row=0, column=1, padx=10, pady=10)
    reinspeccion_cita.grid(row=0, column=2, padx=10, pady=10)
    placa_label.grid(row=1, column=0, padx=10, pady=10)
    placa_entry.grid(row=1, column=1, padx=10, pady=10)
    tipo_vehiculo_label.grid(row=2, column=0, padx=10, pady=10)
    tipo_vehiculo_listbox.grid(row=2, column=1, padx=10, pady=10)
    marca_label.grid(row=3, column=0, padx=10, pady=10)
    marca_entry.grid(row=3, column=1, padx=10, pady=10)
    modelo_label.grid(row=4, column=0, padx=10, pady=10)
    modelo_entry.grid(row=4, column=1, padx=10, pady=10)
    propietario_label.grid(row=5, column=0, padx=10, pady=10)
    propietario_entry.grid(row=5, column=1, padx=10, pady=10)
    telefono_label.grid(row=6, column=0, padx=10, pady=10)
    telefono_entry.grid(row=6, column=1, padx=10, pady=10)
    correo_label.grid(row=7, column=0, padx=10, pady=10)
    correo_entry.grid(row=7, column=1, padx=10, pady=10)
    direccion_label.grid(row=8, column=0, padx=10, pady=10)
    direccion_entry.grid(row=8, column=1, padx=10, pady=10)
    tipo_horario_label.grid(row=9, column=0, padx=10, pady=10)
    tipo_horario_manual.grid(row=9, column=1, padx=10, pady=10)
    tipo_horario_automatica.grid(row=9, column=2, padx=10, pady=10)
    fecha_label.grid(row=10, column=0, padx=10, pady=10)
    fecha_entry.grid(row=10, column=1, padx=10, pady=10)
    tiempo_label.grid(row=11, column=0, padx=10, pady=10)
    tiempo_entry.grid(row=11, column=1, padx=10, pady=10)
    enviar_boton.grid(row=12, column=1, padx=10, pady=10)
        
    window.mainloop()

crear_cita_window()
