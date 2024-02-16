 
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
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

# Ejemplo de uso:
if __name__ == "__main__":
    arbol = ArbolBinario(10)
    arbol.agregar(5)
    arbol.agregar(15)
    arbol.agregar(3)
    arbol.agregar(7)
    arbol.agregar(12)
    arbol.agregar(18)

    print("Recorrido del arbol:\n")
    print("Recorrido preorden:")
    arbol.preorden(arbol.raiz)
    print("\nRecorrido inorden:")
    arbol.inorden(arbol.raiz)
    print("\nRecorrido postorden:")
    arbol.postorden(arbol.raiz)
