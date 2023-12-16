from objetos.animales import Animal
from estructuras.arbolbinario import BinaryTree
from objetos.escena import Escena
from estructuras.linkedlist import LinkedList
from objetos.parte import Parte
from estructuras.rojinegro import RBTree

def main():

    estructura_partes = LinkedList()  # O BinaryTree() o RBTree()

    leon = Animal("León", 10)
    tigre = Animal("Tigre", 9)
    elefante = Animal("Elefante", 8)
    

    escena_savanna = Escena()
    escena_savanna.agregar_animal(leon)
    escena_savanna.agregar_animal(tigre)
    escena_savanna.agregar_animal(elefante)

    parte_savanna = Parte(estructura_partes)
    parte_savanna.agregar_escena(escena_savanna)

def crearAnimales(n, estructura_partes):
    estructura = estructura_partes

    for i in range(1,n+1):
        animal = Animal(i)
        estructura.append(animal)
    return estructura

def crearEscenas(k,estructura_animales):
    estructura = estructura_animales
    nEscenas = k
    for i in range(1,nEscenas+1):
        escena = Escena(estructura)
        estructura.append(escena)
    return estructura

def crearApertura(m,k,estructura_escenas):
    estructura = estructura_escenas
    nEscenas = (m-1)*k
    for i in range(1,nEscenas+1):
        escena = Escena(estructura)
        estructura.append(escena)
    return estructura


    


if __name__ == "__main__":
    main()
