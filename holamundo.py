""" frutas = ["banana", "pera", "manzana"]

frutas[2] = "uvas"

# print (frutas)

nombre = "info"
apellido = "matorio"
edad = 12

print(f"mi nombre es {nombre}, mi apellido es {apellido}, y tengo {edad} años de edad ") """

# 1 - sumar los elementos de una lista
""" numeros = [1, 3, 5, 7, 9]
suma = 0



for numero in numeros: 
    suma += numero

print(f"el valor de la suma de todos los numeros es {suma}") """

caracter = input("ingrese un caracter: ")
if caracter.isupper():
    print("el caracter es una letra mayuscula")
elif caracter.islower():
    print("El caracter es una letra minuscula")
elif caracter.isdigit():
    print("el caracter es un numero")
else: 
    print("el caracter es un caracter especial")