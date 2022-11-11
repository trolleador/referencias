

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

yo = Player(1,1)
tu = Player(0,0)

yo.agregar_compartido("compartido desde yo")
tu.agregar_compartido("compartido desde tu")

yo.agregar_individual("invividual de yo")
tu.agregar_individual("individual de tu")

print(yo.arreglo_compartido)
print(tu.arreglo_compartido)
print(yo.arreglo_individual)
print(tu.arreglo_individual)

