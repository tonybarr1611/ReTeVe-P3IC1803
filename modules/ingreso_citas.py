from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox
from datetime import datetime
from modules.abb import *
import json

def ingreso_citas():
    def ingresar():
        cita = cita_entry.get()
        placa = placa_entry.get()
        
        nodo_cita = programador.consultar_nodo(int(cita))
        if nodo_cita == None:
            return MessageBox.showerror("Error", "La cita no existe")
        if str(nodo_cita.datos['placa']) != placa:
            return MessageBox.showerror("Error", "La placa no coincide con la cita")
        if nodo_cita.datos['estado'] != "PENDIENTE":
            return MessageBox.showerror("Error", "La cita no está pendiente")
        
        fecha_actual = datetime.now()
        fecha_actual = int(str(fecha_actual.year).rjust(4, "0") + str(fecha_actual.month).rjust(2, "0") + str(fecha_actual.day).rjust(2, "0") + str(fecha_actual.hour).rjust(2, "0") + str(fecha_actual.minute).rjust(2, "0"))
        
        if fecha_actual > nodo_cita.datos['fecha']:
            return MessageBox.showerror("Error", "La cita ya ha pasado")
        print(nodo_cita.datos['fecha'] - fecha_actual)
        print(fecha_actual)
        if (nodo_cita.datos['fecha'] - fecha_actual) > 100:
            return MessageBox.showerror("Error", "Se debe realizar el ingreso como maximo 1 hora antes de la cita")
        
        marca_label = Label(ventana_ingreso, text = "Marca: " + str(nodo_cita.datos['marca']), font = ("Arial", 15))
        marca_label.grid(row = 4, column = 1, pady = 10)
        modelo_label = Label(ventana_ingreso, text = "Modelo: " + str(nodo_cita.datos['modelo']), font = ("Arial", 15))
        modelo_label.grid(row = 5, column = 1, pady = 10)
        propietario_label = Label(ventana_ingreso, text = "Propietario: " + str(nodo_cita.datos['propietario']), font = ("Arial", 15))
        propietario_label.grid(row = 6, column = 1, pady = 10)
        costo_label = Label(ventana_ingreso, text = "Costo: ", font = ("Arial", 15))
        costo_label.grid(row = 7, column = 1, pady = 10)
        
        with open("modules/estaciones.dat", "r") as file:
            estaciones = json.load(file)
        min_linea = [0, 0]
        for estacion in estaciones:
            for linea in estaciones[estacion]["espera"]:
                if estaciones[estacion]["espera"][linea][0] == cita:
                    return MessageBox.showerror("Error", "La cita ya se encuentra en la estacion " + estacion)
            for linea in estaciones[estacion]["revision"]:
                if estaciones[estacion]["revision"][linea][0] == cita:
                    return MessageBox.showerror("Error", "La cita ya se encuentra en la estacion " + estacion)

            if min_linea == [0, 0]:
                min_linea = [estacion, len(estaciones[estacion]["espera"])]
            elif len(estaciones[estacion]["espera"]) < min_linea[1]:
                min_linea = [estacion, len(estaciones[estacion]["espera"])]
        
        estacion_label = Label(ventana_ingreso, text = "Estacion: " + str(min_linea[0]), font = ("Arial", 15))
        estacion_label.grid(row = 8, column = 1, pady = 10)
        
        estaciones[min_linea[0]]["espera"][str(min_linea[1] + 1)] = [cita, placa]
        
        with open("modules/estaciones.dat", "w") as file:
            file.write(json.dumps(estaciones))
        
        return MessageBox.showinfo("Ingreso", "El vehiculo se encuentra en espera de la estacion " + str(min_linea[0]))

    programador = iniciar_arbol()
    ventana_ingreso = Toplevel()
    ventana_ingreso.title("Ingreso de citas")
    ventana_ingreso.geometry("400x400")
    ventana_ingreso.maxsize(400, 400)
    ventana_ingreso.minsize(400, 400)
    
    cita_label = Label(ventana_ingreso, text = "Cita: ", font = ("Arial", 15))
    cita_label.grid(row = 1, column = 0, pady = 10)
    cita_entry = Entry(ventana_ingreso, font = ("Arial", 15))
    cita_entry.grid(row = 1, column = 1, pady = 10)
    
    placa_label = Label(ventana_ingreso, text = "Placa: ", font = ("Arial", 15))
    placa_label.grid(row = 2, column = 0, pady = 10)
    placa_entry = Entry(ventana_ingreso, font = ("Arial", 15))
    placa_entry.grid(row = 2, column = 1, pady = 10)
    
    cancelar_boton = Button(ventana_ingreso, text = "Registrar ingreso", font = ("Arial", 15), command = ingresar)
    cancelar_boton.grid(row = 3, column = 0, columnspan = 2, pady = 10)