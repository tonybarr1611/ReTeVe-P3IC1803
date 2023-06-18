class Nodo:
    def __init__(self, cita, tipo, placa, vehiculo, marca, modelo, propietario, telefono, correo, direccion, fecha, izquierda = None, derecha = None):
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
            'fecha': fecha
        }
        self.izquierda = izquierda
        self.derecha = derecha
# Se crea la clase Arbol que nos permitira crear el arbol binario
class Arbol:
    # Se inicializa como un arbol de 0 nodos
    def __init__(self):
        self.raiz = None
        self.cantidad_citas = 0
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
        
    def agregar_nodo(self, tipo, placa, vehiculo, marca, modelo, propietario, telefono, correo, direccion, fecha):
        nodo = Nodo(self.cantidad_citas, tipo, placa, vehiculo, marca, modelo, propietario, telefono, correo, direccion, fecha)
        # Si el arbol esta vacio, el nodo se vuelve la raiz
        if self.raiz == None:
            self.raiz = nodo
        else:
            self.agregar_nodo_aux(nodo, self.raiz)
        self.cantidad_citas = self.cantidad_citas + 1
    
    def consultar_nodo_aux(self, cita, nodo_actual):
        if nodo_actual != None:
            if cita == nodo_actual.cita:
                return nodo_actual
            elif cita < nodo_actual.cita:
                return self.consultar_nodo_aux(cita, nodo_actual.izquierda)
            else:
                return self.consultar_nodo_aux(cita, nodo_actual.derecha)
        else:
            return None
    
    def consultar_nodo(self, cita):
        return self.consultar_nodo_aux(cita, self.raiz)