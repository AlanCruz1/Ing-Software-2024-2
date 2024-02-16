#CANTIDAD DE VALLES
def valles(recorrido):
    nivel = 0 
    valles = 0

    for letra in recorrido:
        if letra == 'U':
            nivel += 1
            """ SI PASÓ AL NIVEL DEL MAR TRAS UNA SUBIDA QUIERE DECIR QUE
                ESTABA POR DEBAJO DEL NIVEL DEL MAR POR LO QUE SE ENCONTRABA
                EN UN VALLE 
            """
            if nivel == 0:
                valles += 1
        else:
            nivel -= 1

    return valles

#ÁRBOL BINARIO ORDENADO
 #ME BASÉ EN EL TUTORIAL DE UN YOUTUBER HINDÚ JEJE
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioOrdenado:
    def __init__(self, valor_raiz):
        self.raiz = Nodo(valor_raiz)

    def agregar(self, valor, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self.agregar(valor, nodo.izquierda)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self.agregar(valor, nodo.derecha)

    def preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.inorden(nodo.derecha)

    def postorden(self, nodo):
        if nodo:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.valor, end=" ")

#FUNCIÓN  MAIN
if __name__ == "__main__":
    recorrido = "DDUUDDUUUDU" #MODIFICAR EL RECORRIDO DEL VIAJERO
    print("Número de valles en el recorrido:", valles(recorrido))
#ÁRBOL BINARIO DEFINIDDO DEFINIDO 
    arbol = ArbolBinarioOrdenado(10)
    arbol.agregar(7)
    arbol.agregar(3)
    arbol.agregar(12)
    arbol.agregar(2)
    arbol.agregar(5)
    arbol.agregar(10)
    arbol.agregar(14)
    arbol.agregar(1)
    arbol.agregar(4)
    arbol.agregar(6)
    arbol.agregar(9)
    arbol.agregar(11)
    arbol.agregar(13)

    print("Recorrido del arbol:\n")
    print("Recorrido preorden:")
    arbol.preorden(arbol.raiz)
    print("\nRecorrido inorden:")
    arbol.inorden(arbol.raiz)
    print("\nRecorrido postorden:")
    arbol.postorden(arbol.raiz)
