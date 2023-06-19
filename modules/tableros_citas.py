from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox
from datetime import datetime
from modules.abb import *
import json

def tablero_citas():
    programador = iniciar_arbol()
    with open("modules/configuracion.dat", "r") as file:
        configuracion = json.load(file)
        
    ventana_tablero = Toplevel()
    ventana_tablero.title("Tablero de citas")
    ventana_tablero.maxsize(800, 250 + ((int(configuracion['cantidad_lineas']) - 5) * 35))
    ventana_tablero.minsize(800, 250 + ((int(configuracion['cantidad_lineas']) - 5) * 35))
    
    fecha_actual = datetime.now()
    fecha_label = Label(ventana_tablero, text = "Fecha: " + fecha_actual.strftime("%d/%m/%Y"), font = ("Arial", 15))
    fecha_label.grid(row = 0, column = 1, pady = 3, padx = 20)
    
    linea_label = Label(ventana_tablero, text = "Linea", font = ("Arial", 15))
    linea_label.grid(row = 1, column = 0, pady = 3, padx = 20)
    puesto1_label = Label(ventana_tablero, text = "Puesto 1", font = ("Arial", 15))
    puesto1_label.grid(row = 1, column = 1, pady = 3, padx = 20)
    puesto2_label = Label(ventana_tablero, text = "Puesto 2", font = ("Arial", 15))
    puesto2_label.grid(row = 1, column = 2, pady = 3, padx = 20)
    puesto3_label = Label(ventana_tablero, text = "Puesto 3", font = ("Arial", 15))
    puesto3_label.grid(row = 1, column = 3, pady = 3, padx = 20)
    puesto4_label = Label(ventana_tablero, text = "Puesto 4", font = ("Arial", 15))
    puesto4_label.grid(row = 1, column = 4, pady = 3, padx = 20)
    puesto5_label = Label(ventana_tablero, text = "Puesto 5", font = ("Arial", 15))
    puesto5_label.grid(row = 1, column = 5, pady = 3, padx = 20)
    
    lineas = []
    for n in range(1, int(configuracion['cantidad_lineas']) + 1):
        linea = Label(ventana_tablero, text = str(n), font = ("Arial", 15))
        linea.grid(row = n + 1, column = 0, pady = 3, padx = 20)
        lineas.append(linea)
        