from objetos.animales import Animal
from estructuras.arbolbinario import BinaryTree
from objetos.escena import Escena
from estructuras.linkedlist import LinkedList
from objetos.parte import Parte
from estructuras.rojinegro import RBTree

def main():

    print("hola mundo")

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
