from estructuras.arbolbinario import BinaryTree
from estructuras.linkedlist import LinkedList
from estructuras.rojinegro import RBTree

class Parte:
    def __init__(self, estructura_datos):
        self.estructura_datos = estructura_datos

    def agregar_escena(self, escena):
        self.estructura_datos.append(escena)

    def get_value(self):
        return self.estructura_datos.get_value()

    def get_animal_mas_menos_repetido(self):
        return self.estructura_datos.get_animal_mas_repetido()
    
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
        
    def __lt__(self, other):
        if not isinstance(other, Parte):
            return NotImplemented
        return self.get_grandeza() < other.get_grandeza()    