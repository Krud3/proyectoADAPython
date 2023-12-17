from estructuras.arbolbinario import BinaryTree
from estructuras.linkedlist import LinkedList
from estructuras.rojinegro import RBTree

class Escena:

    def __init__(self, estructura_datos):

        self.estructura_datos = estructura_datos

    def agregar_animal(self, animal):
        self.estructura_datos.append(animal)

    def get_value(self):
        return self.estructura_datos.get_value()


    
    def get_grandeza(self):
        if isinstance(self.estructura_datos, BinaryTree):
            return self.estructura_datos.get_grandeza()
        
        elif isinstance(self.estructura_datos, LinkedList):
            total_grandeza = 0
            for animal in self.estructura_datos:
                #depronto el .data no va
                total_grandeza += animal.get_grandeza()
            return total_grandeza
        
        else :
            return self.estructura_datos.get_grandeza()
    
    def __lt__(self, other):
        if not isinstance(other, Escena):
            return NotImplemented
        return self.get_grandeza() < other.get_grandeza()

