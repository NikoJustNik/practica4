from pasajero import Pasajero


class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaPasajeros:
    # arranca vacia
    def __init__(self):
        self.head = None
        self.cantidad = 0

    # mete al final
    def ingresar(self, pasajero):
        nuevo = Nodo(pasajero)

        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo

        self.cantidad = self.cantidad + 1
        return True

    # ver si no hay nadie
    def esta_vacia(self):
        return self.head is None

    # cuantos hay
    def longitud(self):
        return self.cantidad

    # sacar todos en orden
    def listar(self):
        resultado = []
        actual = self.head
        while actual is not None:
            resultado.append(actual.data)
            actual = actual.next
        return resultado

    # buscar por numero
    def buscar(self, numero):
        actual = self.head
        while actual is not None:
            if actual.data.numero == numero:
                return actual.data
            actual = actual.next
        return None

    # buscar por asiento
    def buscar_por_asiento(self, asiento):
        actual = self.head
        while actual is not None:
            if actual.data.asiento == asiento:
                return actual.data
            actual = actual.next
        return None

    # buscar por cedula
    def buscar_por_cedula(self, cedula):
        actual = self.head
        while actual is not None:
            if actual.data.cedula == cedula:
                return actual.data
            actual = actual.next
        return None

    # cambiar datos
    def modificar(self, numero, nuevo_nombre, nueva_edad, nuevo_asiento):
        pasajero = self.buscar(numero)
        if pasajero is None:
            return False
        pasajero.nombre = nuevo_nombre
        pasajero.edad = nueva_edad
        pasajero.asiento = nuevo_asiento
        return True

    # quitar una reserva
    def eliminar(self, numero):
        # lista vacia
        if self.head is None:
            return None
        # era la cabeza
        if self.head.data.numero == numero:
            quitado = self.head
            self.head = self.head.next
            self.cantidad = self.cantidad - 1
            return quitado.data
        # buscar con anterior
        anterior = self.head
        while anterior.next is not None and anterior.next.data.numero != numero:
            anterior = anterior.next
        # no existe
        if anterior.next is None:
            return None
        # saltarse el nodo
        quitado = anterior.next
        anterior.next = quitado.next
        self.cantidad = self.cantidad - 1
        return quitado.data

    # filtrar por clase
    def filtrar_por_clase(self, clase):
        resultado = []
        actual = self.head
        while actual is not None:
            if actual.data.clase() == clase:
                resultado.append(actual.data)
            actual = actual.next
        return resultado
