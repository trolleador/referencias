

# los nombres de las clases deben de empezar con mayúscula.
class Player:

    #variables compartidas:
    
    jugando = True
    arreglo_compartido = []

    #función iniciadora de la clase:
    def __init__(self, position_x, position_y):
        self.x = position_x
        self.y = position_y
        self.arreglo_individual = []


    #función para agregar cosas al arreglo:
    def agregar_compartido(self, elemento):
        self.arreglo_compartido.append(elemento)

    def agregar_individual(self, elemento):
        self.arreglo_individual.append(elemento)

pepe = Player(1,1)
maria = Player(0,0)

pepe.agregar_compartido("compartido desde yo")
maria.agregar_compartido("compartido desde tu")

pepe.agregar_individual("invividual de yo")
maria.agregar_individual("individual de tu")

print(pepe.arreglo_compartido)
print(maria.arreglo_compartido)
print(pepe.arreglo_individual)
print(maria.arreglo_individual)

