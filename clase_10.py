# POO

class Coche:

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
coche_1 = Coche("Toyota", "Corolla", "Gris")
coche_2 = Coche("Nisan", "Tucson", "Azul")

print(coche_1)