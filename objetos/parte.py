from ..estructuras.arbolbinario import BinaryTree
from ..estructuras.linkedlist import LinkedList
from ..estructuras.rojinegro import RBTree

class Parte:
    def __init__(self, estructura_datos):
        self.estructura_datos = estructura_datos

    def agregar_escena(self, escena):
        self.estructura_datos.append(escena)

    def get_value(self):
        if isinstance(self.estructura_datos, BinaryTree):
            return self.estructura_datos.get_value()
        
        elif isinstance(self.estructura_datos, LinkedList):
            nombres = []
            for escena in self.estructura_datos:
                nombres.append(escena.data.get_value())
            nombres

        else :
            return self.estructura_datos.get_value()
    
    def get_grandeza(self):
        if isinstance(self.estructura_datos, BinaryTree):
            return self.estructura_datos.get_grandeza()
        
        elif isinstance(self.estructura_datos, LinkedList):
            total_grandeza = 0
            for escena in self.estructura_datos:
                #depronto el .data no va
                total_grandeza += escena.get_grandeza()
            return total_grandeza
        
        else :
            return self.estructura_datos.get_grandeza()