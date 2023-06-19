import json

# Auxiliar de iniciar_arbol
# Entradas: arbol_lista (lista), arbol (Arbol)
# Salida: arbol (Arbol)
def iniciar_arbol_aux(arbol_lista, arbol):
    if len(arbol_lista) == 0:
        return arbol
    if arbol_lista[0]['cita'] != arbol.cantidad_citas:
        arbol.cantidad_citas = arbol.cantidad_citas + 1
        return iniciar_arbol_aux(arbol_lista, arbol)
    else:
        arbol.agregar_nodo(arbol_lista[0]['tipo'], arbol_lista[0]['placa'], arbol_lista[0]['vehiculo'], arbol_lista[0]['marca'], arbol_lista[0]['modelo'], arbol_lista[0]['propietario'], arbol_lista[0]['telefono'], arbol_lista[0]['correo'], arbol_lista[0]['direccion'], arbol_lista[0]['fecha'], arbol_lista[0]['estado'])
        return iniciar_arbol_aux(arbol_lista[1:], arbol)
# Carga los datos del arbol de citas
# Entradas: Ninguna
# Salidas: arbol (Arbol)
def iniciar_arbol():
    with open('modules/citas_abb.dat', 'r') as file:
        arbol_existente = json.load(file)

    if arbol_existente == {'cantidad_citas': 1, 'arbol': []}:
        return Arbol()
    else:
        arbol = Arbol()
        arbol = iniciar_arbol_aux(arbol_existente['arbol'], arbol)
        return arbol
# Auxiliar de guardar_arbol
# Entradas: arbol (Arbol), cita (int)
# Salidas: lista (list)
def guardar_arbol_aux(arbol, cita = 1):
    if cita > arbol.cantidad_citas - 1:
        return []
    else:
        try:
            datos = arbol.consultar_nodo(cita).datos
            datos["cita"] = cita
            return [datos] + guardar_arbol_aux(arbol, cita + 1)
        except:
            return guardar_arbol_aux(arbol, cita + 1)
        
# Guarda los datos del arbol de citas
# Entradas: arbol (Arbol)
# Salidas: Ninguna   
def guardar_arbol(arbol):
    if arbol.cantidad_citas == 1:
        arbol_existente = {'cantidad_citas': 1, 'arbol': []}
    else:
        arbol_existente = {'cantidad_citas': arbol.cantidad_citas, 'arbol': []}
        arbol_lista = guardar_arbol_aux(arbol)
        arbol_existente['arbol'] = arbol_lista
    with open('modules/citas_abb.dat', 'w') as file:
        file.write(json.dumps(arbol_existente))
# Clase Nodo que nos permite crear los nodos del arbol
class Nodo:
    def __init__(self, cita, tipo, placa, vehiculo, marca, modelo, propietario, telefono, correo, direccion, fecha, estado, izquierda = None, derecha = None):
        self.cita = cita
        self.datos = {
            'tipo': tipo,
            'placa': placa,
            'vehiculo': vehiculo,
            'marca': marca,
            'modelo': modelo,
            'propietario': propietario,
            'telefono': telefono,
            'correo': correo,
            'direccion': direccion,
            'fecha': fecha,
            'estado': estado
        }
        self.izquierda = izquierda
        self.derecha = derecha
# Se crea la clase Arbol que nos permitira crear el arbol binario
class Arbol:
    # Se inicializa como un arbol de 0 nodos
    def __init__(self, raiz = None, cantidad_citas = 1):
        self.raiz = raiz
        self.cantidad_citas = cantidad_citas
    # Funcion auxiliar recursiva usada para agegar un nodo al arbol
    def agregar_nodo_aux(self, nodo_insertado, nodo_actual):
        # Si la fecha es menor, se mueve a la izquiera
        if nodo_insertado.datos['fecha'] < nodo_actual.datos['fecha']:
            if nodo_actual.izquierda != None:
                self.agregar_nodo_aux(nodo_insertado, nodo_actual.izquierda)
            else:
                nodo_actual.izquierda = nodo_insertado
        # Si la fecha es mayor, se mueve a la derecha
        else:
            if nodo_actual.derecha != None:
                self.agregar_nodo_aux(nodo_insertado, nodo_actual.derecha)
            else:
                nodo_actual.derecha = nodo_insertado
    # Funcion que agrega un nodo al arbol   
    def agregar_nodo(self, tipo, placa, vehiculo, marca, modelo, propietario, telefono, correo, direccion, fecha, estado = 'PENDIENTE'):
        nodo = Nodo(self.cantidad_citas, tipo, placa, vehiculo, marca, modelo, propietario, telefono, correo, direccion, fecha, estado)
        # Si el arbol esta vacio, el nodo se vuelve la raiz
        if self.raiz == None:
            self.raiz = nodo
        else:
            self.agregar_nodo_aux(nodo, self.raiz)
        self.cantidad_citas = self.cantidad_citas + 1
    # Funcion auxiliar recursiva usada para consultar un nodo del arbol
    def consultar_nodo_aux(self, cita, nodo_actual):
        if nodo_actual != None:
            if cita == nodo_actual.cita:
                return nodo_actual
            if self.consultar_nodo_aux(cita, nodo_actual.izquierda) != None:
                return self.consultar_nodo_aux(cita, nodo_actual.izquierda)
            if self.consultar_nodo_aux(cita, nodo_actual.derecha) != None:
                return self.consultar_nodo_aux(cita, nodo_actual.derecha)
        else:
            return None
    # Consulta un nodo del arbol
    def consultar_nodo(self, cita):
        return self.consultar_nodo_aux(cita, self.raiz)
