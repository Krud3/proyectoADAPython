from objetos.animales import Animal
from estructuras.arbolbinario import BinaryTree
from objetos.escena import Escena
from estructuras.linkedlist import LinkedList
from objetos.parte import Parte
from estructuras.rojinegro import RBTree
import random
import time

def main():

    
    #prueba_get_value_ll()
    #prueba_get_value_RB()
    #prueba_get_value_BT()
    prueba_escena_menor_mayor()
    '''
    n = 9
    m = 4
    k = 3
    print("n: ", n, "m: ", m, "k: ", k)
    estructura = LinkedList()
    evento = crearEvento(n,m,k,estructura)
    ls = evento.get_value()
    iterator = 0
    for parte in ls:
        if iterator == 0:
            print("Apertura: ", parte)
        else:

            print("Parte: ",iterator, parte)
        iterator = iterator + 1

    print("n: ", n, "m: ", m, "k: ", k)
    estructura = RBTree()
    evento = crearEvento(n,m,k,estructura)
    ls = evento.get_value()
    iterator = 0
    for parte in ls:
        if iterator == 0:
            print("Apertura: ", parte)
        else:

            print("Parte: ",iterator, parte)
        iterator = iterator + 1

    print("n: ", n, "m: ", m, "k: ", k)
    estructura = BinaryTree()
    evento = crearEvento(n,m,k,estructura)
    ls = evento.get_value()
    ls.reverse()
    iterator = 0
    for parte in ls:
        if iterator == 0:
            print("Apertura: ", parte)
            print("Escena de menor grandeza es:", parte[0])
            print("Escena de mayor grandeza es:", parte[-1])
        else:
            print("Parte: ",iterator, parte)
        iterator = iterator + 1

    #evento.get_value_counts()

    #print("Evento: ", evento.get_value())
    '''


def crearEvento(n,m,k,estructura):
    la_estructura = None
    if isinstance(estructura, LinkedList):
        la_estructura = LinkedList()
    elif isinstance(estructura, RBTree):
        la_estructura = RBTree()
    elif isinstance(estructura, BinaryTree):
        la_estructura = BinaryTree()

    estructura1 = la_estructura
    estructura2 = la_estructura
    lista_animales = LinkedList()
    crearAnimales(n,lista_animales)
    nombres = []

    for animal in lista_animales:
        nombres.append(animal.get_value())
        nombres.append(animal.get_grandeza())
        #print(animal.get_value(), animal.get_grandeza())
    
    lista_animales.shuffle()

    las_escenas = crearEscenas(m,k,lista_animales,estructura1)
    escenas_estructura = las_escenas[0]
    prom = escenas_estructura.get_grandeza()/((m-1)*k)
    #print("promedio grandeza de las escenas: ", prom)
    escenas_to_shufle = las_escenas[1]
    #print("Escenas to shuffle: ", escenas_to_shufle.get_value() )

    la_apertura = crearApertura(escenas_estructura)
    partes = crearPartes(m,k,escenas_to_shufle,estructura2,la_apertura)
    return partes



def crearAnimales(n, estructura_partes):
    estructura = estructura_partes

    for i in range(1,n+1):
        animal = Animal(i)
        estructura.append(animal)
    return estructura

def crearEscenas(m,k,linked_list_animales, tipo_estructura):
    
    escenas_totales = (m-1)*k
    todas_las_escenas = tipo_estructura
    escenas_to_shufle = LinkedList()
    for i in range(escenas_totales):
        
        animales_a_usar = LinkedList()
        nAgregados = 0
        while(nAgregados < 3):
            linked_list_animales.shuffle()
            animal = linked_list_animales.head.data

            if not (animales_a_usar.find(animal)):
                animales_a_usar.append(animal)
                nAgregados = nAgregados+ 1

        nueva_escena = Escena(animales_a_usar)
        escenas_to_shufle.append(nueva_escena)
        todas_las_escenas.append(nueva_escena)
    
    return (todas_las_escenas, escenas_to_shufle)

def crearApertura(estructura_escenas):
    apertura = Parte(estructura_escenas)
    return apertura

def crearPartes(m,k,escenas_to_shufle,estructura,apertura):
    partes_a_retornar = None
    if isinstance(estructura, LinkedList):
        partes_a_retornar = LinkedList()
    elif isinstance(estructura, RBTree):
        partes_a_retornar = RBTree()
    elif isinstance(estructura, BinaryTree):
        partes_a_retornar = BinaryTree()    

    la_apertura = apertura
    partes_a_retornar.append(la_apertura)
    escenas_to_shufle.shuffle()
    #print("cabeza escenas to shuffle: ", escenas_to_shufle.head.data.get_value())  
    for _ in range(m-1):
        if isinstance(estructura, LinkedList):
            escenas = LinkedList()
        elif isinstance(estructura, RBTree):
            escenas = RBTree()
        elif isinstance(estructura, BinaryTree):
            escenas = BinaryTree()
        nueva_parte = Parte(escenas)

        for j in range(k):
            escenita = escenas_to_shufle.head.data
            escenas.append(escenita)
            escenas_to_shufle.pop_head()
    
        partes_a_retornar.append(nueva_parte)

    return partes_a_retornar
    
def prueba_get_value_ll():
    n = 6
    m = 3
    k = 2
    for i in range(0,20):

        estructura = LinkedList()
        evento = crearEvento(n,m,k,estructura)
        inicio = time.time_ns()
        ls = evento.get_value()
        fin = time.time_ns()
        tiempo_milisegundos = (fin-inicio)/10**6
        print("i", i, "n: ",n, "m:", m, "k",k,"Tiempo: ", tiempo_milisegundos)
        n = n+2
        m = int(n/2)
        k = int(m-1)

def prueba_get_value_RB():
    n = 6
    m = 3
    k = 2
    for i in range(0,20):

        estructura = RBTree()
        evento = crearEvento(n,m,k,estructura)
        inicio = time.time_ns()
        ls = evento.get_value()
        fin = time.time_ns()
        tiempo_milisegundos = (fin-inicio)/10**6
        print("i", i, "n: ",n, "m:", m, "k",k,"Tiempo: ", tiempo_milisegundos)
        n = n+2
        m = int(n/2)
        k = int(m-1)

def prueba_get_value_BT():
    n = 6
    m = 3
    k = 2
    for i in range(0,20):

        estructura = BinaryTree()
        evento = crearEvento(n,m,k,estructura)
        inicio = time.time_ns()
        ls = evento.get_value()
        fin = time.time_ns()
        tiempo_milisegundos = (fin-inicio)/10**6
        print("i", i, "n: ",n, "m:", m, "k",k,"Tiempo: ", tiempo_milisegundos)
        n = n+2
        m = int(n/2)
        k = int(m-1)

def prueba_escena_menor_mayor():
    n = 6
    m = 3
    k = 2
    for i in range(0,40):

        estructura = BinaryTree()
        evento = crearEvento(n,m,k,estructura)
        
        ls = evento.get_value()
        ls.reverse()
        inicio = time.time_ns()
        iterator = 0
        for parte in ls:
            if iterator == 0:
                #print("Apertura: ", parte)
                parte[0]
                parte[-1]
            else:
                break
            iterator = iterator + 1
        fin = time.time_ns()
        tiempo_milisegundos = (fin-inicio)/10**6
        print("i", i, "n: ",n, "m:", m, "k",k,"Tiempo: ", tiempo_milisegundos)
        n = n+2
        m = int(n/2)
        k = int(m-1)

if __name__ == "__main__":
    main()
