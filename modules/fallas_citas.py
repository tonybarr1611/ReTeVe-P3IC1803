from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox
from datetime import datetime
from modules.abb import *
import json

def fallas_citas():
    def cargar():
        llave_entry.delete(0, END)
        descripcion_entry.delete(0, END)
        tipo_string.set("Seleccione")
        with open("modules/fallas.dat", "r") as file:
            fallas = json.loads(file.read())
        if cargar_entry.get() == "":
            MessageBox.showerror("Error", "Ingrese una llave")
        else:
            llave = int(cargar_entry.get())
            for tipo in fallas:
                try:
                    llave_entry.insert(0, llave)
                    descripcion_entry.insert(0, fallas[tipo][str(llave)][0])
                    tipo_string.set(fallas[tipo][str(llave)][1])
                    return
                except:
                    llave_entry.delete(0, END)
                    descripcion_entry.delete(0, END)
                    tipo_string.set("Seleccione")
    
    def create():
        with open("modules/fallas.dat", "r") as file:
            fallas = json.loads(file.read())
        if llave_entry.get() == "" or descripcion_entry.get() == "" or tipo_string.get() == "Seleccione":
            return MessageBox.showerror("Error", "Ingrese todos los datos")
        if not llave_entry.get().isnumeric() or int(llave_entry.get()) < 1 or int(llave_entry.get()) > 9999:
            return MessageBox.showerror("Error", "La llave debe ser un entero positivo entre 1 y 9999")
        if len(descripcion_entry.get()) < 5 or len(descripcion_entry.get()) > 200:
            return MessageBox.showerror("Error", "La descripción debe tener entre 5 y 200 caracteres")
        falla_leve = ""
        falla_grave = ""
        try:
            falla_leve = fallas["leves"][llave_entry.get()]
            falla_grave = fallas["graves"][llave_entry.get()]
        except:
            pass
        if falla_leve == "" and falla_grave == "":
            fallas[tipo_string.get().lower() + "s"][llave_entry.get()] = (descripcion_entry.get(), tipo_string.get())
            with open("modules/fallas.dat", "w") as file:
                file.write(json.dumps(fallas))
            MessageBox.showinfo("Falla creada", "La falla ha sido creada")
        elif falla_leve != "":
            if tipo_string.get() == "Leve":
                fallas["leves"][llave_entry.get()] = (descripcion_entry.get(), tipo_string.get())
            else:
                fallas["graves"][llave_entry.get()] = (descripcion_entry.get(), tipo_string.get())
                fallas["leves"].pop(llave_entry.get())
            MessageBox.showinfo("Falla actualizada", "La falla ha sido actualizada")
            with open("modules/fallas.dat", "w") as file:
                file.write(json.dumps(fallas))
        elif falla_grave != "":
            if tipo_string.get() == "Grave":
                fallas["graves"][llave_entry.get()] = (descripcion_entry.get(), tipo_string.get())
            else:
                fallas["leves"][llave_entry.get()] = (descripcion_entry.get(), tipo_string.get())
                fallas["graves"].pop(llave_entry.get())
            MessageBox.showinfo("Falla actualizada", "La falla ha sido actualizada")
            with open("modules/fallas.dat", "w") as file:
                file.write(json.dumps(fallas))
                
    
    def delete():
        cargar()
        if MessageBox.askyesno("Eliminar", "¿Desea eliminar la falla?"):
            for n in range(programador.cantidad_citas):
                try:
                    if int(llave_entry.get()) in programador.consultar_nodo(n).datos['fallas']:
                        return MessageBox.showerror("Error", "La falla está siendo utilizada en una cita")
                except:
                    pass
            with open("modules/fallas.dat", "r") as file:
                fallas = json.loads(file.read())
            try:
                fallas["leves"].pop(llave_entry.get())
            except:
                fallas['graves'].pop(llave_entry.get())
            with open("modules/fallas.dat", "w") as file:
                file.write(json.dumps(fallas))
            return MessageBox.showinfo("Falla eliminada", "La falla ha sido eliminada")
        else:
            return
    
    programador = iniciar_arbol()
    
    ventana_fallas = Toplevel()
    ventana_fallas.title("Lista de Fallas")
    ventana_fallas.geometry("500x500")
    ventana_fallas.maxsize(500, 500)
    ventana_fallas.minsize(500, 500)
    
    title_label = Label(ventana_fallas, text = "Lista de Fallas", font = ("Arial", 20))
    title_label.grid(row = 0, column = 0, columnspan = 2, pady = 10)
    
    cargar_entry = Entry(ventana_fallas, font = ("Arial", 15))
    cargar_entry.grid(row = 1, column = 0, pady = 10)
    cargar_boton = Button(ventana_fallas, text = "Cargar", font = ("Arial", 10), command = cargar)
    cargar_boton.grid(row = 1, column = 1, pady = 10)
    borrar_boton = Button(ventana_fallas, text = "Borrar", font = ("Arial", 10), command = delete)
    borrar_boton.grid(row = 1, column = 2, pady = 10)
    
    datos_label = Label(ventana_fallas, text = "Datos", font = ("Arial", 15))
    datos_label.grid(row = 2, column = 0, pady = 10)
    
    llave_label = Label(ventana_fallas, text = "Llave (de 0001 a 9999)", font = ("Arial", 12))
    llave_label.grid(row = 3, column = 0, pady = 10)
    llave_entry = Entry(ventana_fallas, font = ("Arial", 15))
    llave_entry.grid(row = 3, column = 1, pady = 10)
    
    descripcion_label = Label(ventana_fallas, text = "Descripción", font = ("Arial", 12))
    descripcion_label.grid(row = 5, column = 0, pady = 10)
    descripcion_entry = Entry(ventana_fallas, font = ("Arial", 12))
    descripcion_entry.grid(row = 5, column = 1, pady = 10)
    
    tipo_string = StringVar()
    tipo_string.set("Seleccione")
    tipo_label = Label(ventana_fallas, text = "Tipo", font = ("Arial", 12))
    tipo_label.grid(row = 6, column = 0, pady = 10)
    tipo_combobox = ttk.Combobox(ventana_fallas, font = ("Arial", 12), state = "readonly", values=["Leve", "Grave"], textvariable=tipo_string)
    tipo_combobox.grid(row = 6, column = 1, pady = 10)
    
    guardar_boton = Button(ventana_fallas, text = "Guardar", font = ("Arial", 15), command = create)
    guardar_boton.grid(row = 7, column = 0, pady = 10)
    