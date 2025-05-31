#POO

#Un objeto es una instancia de clase
#Es esferica
#tiene parches
#peso
#textura
#rueda

""" class Pelota:
    def __init__(self, color, marca, tamanio, deporte):
        self.color = color
        self.marca = marca
        self.tamanio = tamanio
        self.deporte = deporte

    
    def rodar(self):
        print(f"La pelota de {self.deporte} esta rodando!!")

mi_pelota1 = Pelota("Blanca", "Nike", 5, "Futbol")
mi_pelota2 = Pelota("Roja", "Adidas", 3, "Futsal")

print(f"Mi pelota es {mi_pelota1.marca}, de color {mi_pelota1.color}, para {mi_pelota1.deporte}")
mi_pelota1.rodar() """

#----------------------------------------------------
#Calculadora con POO

class Calculadora:

    def __init__(self):
       pass

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self,a, b):
        if b != 0:
            return a / b
        else:
            return "error, division por 0."

mi_calculadora = Calculadora()
print(f"Suma: {mi_calculadora.sumar(7, 5)}")
print(f"Suma: {mi_calculadora.restar(7, 5)}")
print(f"Suma: {mi_calculadora.multiplicar(3, 5)}")
print(f"Suma: {mi_calculadora.dividir(12, 3)}")