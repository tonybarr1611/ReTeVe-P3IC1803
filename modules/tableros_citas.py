from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox
from datetime import datetime
from modules.abb import *
import json

def tablero_citas():
    def rellenar_tablero(estaciones, tablero_labels):
        if tablero_labels != []:
            for n in tablero_labels:
                n.destroy()
        tablero_labels = []
        for i in range(1, int(configuracion['cantidad_lineas']) + 1):
            for puesto in estaciones[str(i)]['revision']:
                try:
                    nodo_cita = programador.consultar_nodo(int(estaciones[str(i)]['revision'][puesto][0]))
                    try:
                        if nodo_cita.datos['fallas'] != None:
                            label_placa = Label(ventana_tablero, text = estaciones[str(i)]['revision'][puesto][1], font = ("Arial", 12), fg="red")
                            label_placa.grid(row = i + 1, column = puesto, pady = 3, padx = 20)
                            tablero_labels.append(label_placa)
                    except:
                        label_placa = Label(ventana_tablero, text = estaciones[str(i)]['revision'][puesto][1], font = ("Arial", 12))
                        label_placa.grid(row = i + 1, column = puesto, pady = 3, padx = 20)
                        tablero_labels.append(label_placa)
                except:
                    label_placa = Label(ventana_tablero, text = "", font = ("Arial", 12))
                    label_placa.grid(row = i + 1, column = puesto, pady = 3, padx = 20)
                    tablero_labels.append(label_placa)
        return tablero_labels
    def guardar_estaciones(estaciones):
        with open("modules/estaciones.dat", "w") as file:
            file.write(json.dumps(estaciones))
            
    def ejecutar_comando():
        comando = comando_entry.get()
        placa_comando = comando[1:]
        if comando == "":
            return MessageBox.showerror("Error", "El comando no es válido")
        if comando[0] == "T":
            for linea in estaciones:
                if len(estaciones[linea]['espera']) != 0 and str(estaciones[linea]['espera']["1"][1]) == placa_comando:
                    for n in range(1, 6):
                        if estaciones[linea]['revision'][str(n)] == '':
                            for n in range(1, n + 1)[::-1]:
                                try:
                                    estaciones[linea]['revision'][str(n)] = estaciones[linea]['revision'][str(n - 1)]
                                except:
                                    estaciones[linea]['revision'][str(n)] = estaciones[linea]['espera']["1"]
                            estaciones[linea]['espera'].pop("1")
                            guardar_estaciones(estaciones)
                            tablero_labels = rellenar_tablero(estaciones, [])
                            return

                for puesto in estaciones[linea]['revision']:
                    if estaciones[linea]['revision'][puesto] != "" and str(estaciones[linea]['revision'][puesto][1]) == placa_comando:
                        if int(puesto) == 5:
                            return MessageBox.showerror("Error", "La placa ya se encuentra en la ultima posicion de la linea")
                        for n in range(int(puesto), 5):
                            if estaciones[linea]['revision'][str(n + 1)] == '':
                                for j in range(int(puesto), n + 2)[::-1]:
                                    try:
                                        estaciones[linea]['revision'][str(j)] = estaciones[linea]['revision'][str(j - 1)]
                                    except:
                                        if len(estaciones[linea]['espera']) != 0:
                                            estaciones[linea]['revision'][str(j)] = estaciones[linea]['espera']["1"]
                                            estaciones[linea]['espera'].pop("1")  
                                        else:
                                            estaciones[linea]['revision'][str(j)] = ""
                                guardar_estaciones(estaciones)
                                tablero_labels = rellenar_tablero(estaciones, [])
                                comando_entry.delete(0, END)
                                return MessageBox.showinfo("Exito", "La placa se ha desplazado correctamente")
                        return MessageBox.showerror('Error', 'No hay espacio suficiente para desplazar la placa')          
            return MessageBox.showerror("Error", "La placa no se puede desplazar")
        elif comando[0] == "U":
            for linea in estaciones:
                for puesto in estaciones[linea]['revision']:
                    if estaciones[linea]['revision'][puesto] != "" and str(estaciones[linea]['revision'][puesto][1]) == placa_comando:
                        if int(puesto) == 5:
                            return MessageBox.showerror("Error", "La placa ya se encuentra en la ultima posicion de la linea")
                        if estaciones[linea]['revision'][str(int(puesto) + 1)] == "":
                            estaciones[linea]['revision'][str(int(puesto) + 1)] = estaciones[linea]['revision'][puesto]
                            estaciones[linea]['revision'][puesto] = ""
                            guardar_estaciones(estaciones)
                            tablero_labels = rellenar_tablero(estaciones, [])
                            return MessageBox.showinfo("Exito", "La placa se ha desplazado correctamente")
                        else:
                            return MessageBox.showerror("Error", "No hay espacio suficiente para desplazar la placa")
            return MessageBox.showerror("Error", "La placa no existe en el tablero")
        elif comando[0] == "E":
            # Falta verificacion de que la falta exista
            falla = comando[-4:]
            placa_comando = placa_comando[:-4]
            for linea in estaciones:
                for puesto in estaciones[linea]['revision']:
                    print(estaciones[linea]['revision'][puesto])
                    if estaciones[linea]['revision'][puesto] != "" and str(estaciones[linea]['revision'][puesto][1]) == placa_comando:
                        num_cita = estaciones[linea]['revision'][puesto][0]
                        nodo_cita = programador.consultar_nodo(int(num_cita))
                        try:
                            nodo_cita.datos['fallas'].append(falla)
                        except:
                            nodo_cita.datos['fallas'] = []
                            nodo_cita.datos['fallas'].append(falla)
                        guardar_arbol(programador)
                        return MessageBox.showinfo("Exito", "Se ha registrado la falla")
        elif comando[0] == "F":
            pass
        elif comando[0] == "R":
            guardar_arbol(programador)
            guardar_estaciones(estaciones)
            ventana_tablero.destroy()
        else:
            return MessageBox.showerror("Error", "El comando no es válido")
    programador = iniciar_arbol()
    with open("modules/configuracion.dat", "r") as file:
        configuracion = json.load(file)
        
    ventana_tablero = Toplevel()
    ventana_tablero.title("Tablero de citas")
    ventana_tablero.maxsize(800, 290 + ((int(configuracion['cantidad_lineas']) - 5) * 35))
    ventana_tablero.minsize(800, 290 + ((int(configuracion['cantidad_lineas']) - 5) * 35))
    
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
    
    comando_label = Label(ventana_tablero, text = "Comando: ", font = ("Arial", 10))
    comando_label.grid(row = int(configuracion['cantidad_lineas']) + 2, column = 1, pady = 3)
    comando_entry = Entry(ventana_tablero, font = ("Arial", 10), width=10)
    comando_entry.grid(row = int(configuracion['cantidad_lineas']) + 2, column = 2, pady = 3)
    comando_boton = Button(ventana_tablero, text = "Ejecutar", font = ("Arial", 10), command = ejecutar_comando)
    comando_boton.grid(row = int(configuracion['cantidad_lineas']) + 2, column = 3, pady = 3)
    with open("modules/estaciones.dat", "r") as file:
        estaciones = json.load(file)
    tablero_labels = rellenar_tablero(estaciones, [])