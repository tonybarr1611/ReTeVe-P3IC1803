from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox
from modules.abb import *

def cancelar_citas():
    def cancelar():
        # Pendiente verificar que la cita no esté en cola de revision, si está en la cola de espera, se debe eliminar de ahí
        nodo_cita = programador.consultar_nodo(int(cita_entry.get()))
        if nodo_cita == None:
            MessageBox.showerror("Error", "La cita no existe")
        elif nodo_cita.datos['placa'] != placa_entry.get():
            MessageBox.showerror("Error", "La placa no coincide con la cita")
        elif nodo_cita.datos['estado'] != "PENDIENTE":
            MessageBox.showerror("Error", "La cita no está pendiente")
        else:
            if MessageBox.askyesno("Cancelar cita", "¿Está seguro que desea cancelar la cita?"):
                nodo_cita.datos['estado'] = "CANCELADA"
                guardar_arbol(programador)
                MessageBox.showinfo("Cita cancelada", "La cita ha sido cancelada")
            else:
                MessageBox.showinfo("Cita no cancelada", "La cita no ha sido cancelada")
                
    programador = iniciar_arbol()
    ventana_cancelar = Toplevel()
    ventana_cancelar.title("Cancelar citas")
    ventana_cancelar.geometry("300x225")
    ventana_cancelar.maxsize(300, 225)
    ventana_cancelar.minsize(300, 225)
    
    title_label = Label(ventana_cancelar, text = "Cancelar citas", font = ("Arial", 20))
    title_label.grid(row = 0, column = 0, columnspan = 2, pady = 10)
    
    cita_label = Label(ventana_cancelar, text = "Cita: ", font = ("Arial", 15))
    cita_label.grid(row = 1, column = 0, pady = 10)
    cita_entry = Entry(ventana_cancelar, font = ("Arial", 15))
    cita_entry.grid(row = 1, column = 1, pady = 10)
    
    placa_label = Label(ventana_cancelar, text = "Placa: ", font = ("Arial", 15))
    placa_label.grid(row = 2, column = 0, pady = 10)
    placa_entry = Entry(ventana_cancelar, font = ("Arial", 15))
    placa_entry.grid(row = 2, column = 1, pady = 10)
    
    cancelar_boton = Button(ventana_cancelar, text = "Cancelar cita", font = ("Arial", 15), command = cancelar)
    cancelar_boton.grid(row = 3, column = 0, columnspan = 2, pady = 10)