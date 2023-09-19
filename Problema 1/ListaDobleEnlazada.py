class Nodo_DobleEnlazado:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio_lista = 0 

    def esta_vacia(self):
        return self.cabeza is None

    def tamanio(self):
        return self.tamanio_lista  
    
    def __len__(self):
        return max(0, self.tamanio_lista)

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise IndexError("La lista está vacía, no se puede extraer ningún elemento.")

        if posicion is None:
            # Si la posición es None, extraemos el último elemento de la lista
            elemento = self.cola.dato
            if self.cabeza == self.cola:
                self.cabeza = None
                self.cola = None
            else:
                self.cola = self.cola.anterior
                self.cola.siguiente = None
        elif posicion == 0:
            # Si la posición es 0, extraemos el primer elemento de la lista
            elemento = self.cabeza.dato
            if self.cabeza == self.cola:
                self.cabeza = None
                self.cola = None
            else:
                self.cabeza = self.cabeza.siguiente
                self.cabeza.anterior = None
        elif 0 < posicion < self.tamanio() - 1:
            actual = self.cabeza
            indice = 0
            while indice < posicion:
                
                actual = actual.siguiente
                indice += 1
            
            aux=actual
            elemento = actual.dato
            aux.anterior.siguiente = actual.siguiente
            
        elif  0 < posicion <= self.tamanio() - 1:
            aux.siguiente.anterior = actual.anterior
            
        else:
            raise IndexError("La posición no es válida")

            self.tamanio_lista -= 1

            return elemento


    def copiar(self):
        nueva_lista = ListaDobleEnlazada()
        actual = self.cabeza
        while actual is not None:
            nuevo_nodo = Nodo_DobleEnlazado(actual.dato)  
            nueva_lista.agregar_al_final(nuevo_nodo.dato)  

            actual = actual.siguiente

        return nueva_lista

    def insertar(self, dato, posicion=None):
        if posicion is None or posicion == self.tamanio():
            self.agregar_al_final(dato)
        elif posicion == 0:
            self.agregar_al_inicio(dato)
        else:
            nuevo_nodo = Nodo_DobleEnlazado(dato)
            actual = self.cabeza
            indice = 0

            while indice < posicion:
                actual = actual.siguiente
                indice += 1

            nuevo_nodo.anterior = actual.anterior
            nuevo_nodo.siguiente = actual

            if actual.anterior is not None:
                actual.anterior.siguiente = nuevo_nodo
            else:
                self.cabeza = nuevo_nodo

            actual.anterior = nuevo_nodo

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo_DobleEnlazado(dato)
        if self.esta_vacia():
            nuevo_nodo.anterior = None
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
            self.cabeza.anterior = None
        if self.cola is not None:
            self.cola.siguiente = None

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo_DobleEnlazado(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            nuevo_nodo.siguiente = None
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

        if self.cabeza is not None:
            self.cabeza.anterior = None
        
        self.tamanio_lista += 1 

            
    def invertir(self):
        actual = self.cabeza
        while actual is not None:
            actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
            actual = actual.anterior

    def ordenar(self):
        if self.esta_vacia():
            return

        actual = self.cabeza
        while actual is not None:
            siguiente = actual.siguiente
            while siguiente is not None:
                if actual.dato > siguiente.dato:
                    actual.dato, siguiente.dato = siguiente.dato, actual.dato
                siguiente = siguiente.siguiente
            actual = actual.siguiente

    def __iter__(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def concatenar(self, otra_lista):
        if self.esta_vacia():
            self.cabeza = otra_lista.cabeza
            self.cola = otra_lista.cola
            if self.cabeza is not None:
                self.cabeza.anterior = None
            if self.cola is not None:
                self.cola.siguiente = None
        elif not otra_lista.esta_vacia():
            self.cola.siguiente = otra_lista.cabeza
            otra_lista.cabeza.anterior = self.cola
            self.cola = otra_lista.cola
            self.cola.siguiente = None

        self.tamanio_lista += len(otra_lista)  

    def __add__(self, otra_lista):
        nueva_lista = ListaDobleEnlazada()
        nueva_lista.concatenar(self)
        nueva_lista.concatenar(otra_lista)
        return nueva_lista
