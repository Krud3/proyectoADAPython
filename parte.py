class Parte:
    def __init__(self, estructura_datos):
        self.estructura_datos = estructura_datos

    def agregar_escena(self, escena):
        self.estructura_datos.append(escena)

    def mostrar_escenas_linkedlist(self):
        to_return = []
        for escena in self.estructura_datos:
            escena.mostrar_animales()