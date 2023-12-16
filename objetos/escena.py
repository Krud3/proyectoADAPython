class Escena:

    def __init__(self, estructura_datos):
        self.estructura_datos = estructura_datos

    def agregar_animal(self, animal):
        self.estructura_datos.append(animal)

    def concatenar_animales_linkedlist(self):
        nombres = []
        for animal in self.estructura_datos:
            nombres.append(animal.obtener_nombre())
        nombres

    def concatenar_animales_binary_tree(self):
        self.estructura_datos.print_tree()