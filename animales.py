import random

class Animal:
    list_animals = {"Leon","Tigre","Elefante","Jirafa","Cebra","Oso","Canguro","Panda","Gorila","Chimpance","Hipopotamo","Rinoceronte","Cocodrilo","Caiman","Flamenco","Pinguino","Avestruz","PavoReal","Koala","Perezoso","Lobo","Zorro","Bisonte","Bufalo","Camello","Dromedario","Foca","Leopardo","Jaguar","Mono","Murcielago","Nutria","Puercoespin","Armadillo","Suricata","Okapi","Iguana","Tortuga","Serpiente","Cacatua","Tucan","Lince","Puma","Guacamayo","Orix","Antilope","Gacela","Mandril","Lemur","Carpincho"}

    def nombreRandom(self):
        return random.choice(list(self.list_animals))

    def __init__ (self, grandeza):
        self.nombre = self.nombreRandom()
        self.grandeza = grandeza

    def obtener_nombre(self):
        return self.nombre
    
    def obtener_grandeza(self):
        return self.grandeza
    
    