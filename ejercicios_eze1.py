# crear Lista con numeros de uno al 5

#numeros = [1, 2, 3, 4, 5]
#print(numeros[3])

#Crear una Lista vacía. Agrega nombres "ana", "luis" y "carlos" usando metodo append

""" nombres = []
nombres.append("Ana")
nombres.append("Luis")
nombres.append("Carlos")

for nombre in nombres:
    print(nombre) """

#3 - da una Lista (o iterables) de frutas y modificala

""" frutas = ["manzana", "banana", "naranja"]
print(frutas)
frutas[1] = "pera"
print(frutas)
frutas[2] = "uva"
print(frutas) """

#4 - crea una tupla con tres colores, muestra el segundo color

""" colores = ("rojo", "amarillo", "azul")
print(colores[1])
 """
#5 - dada la pupla de datos = (10, 20, 30), convierte en una lista, agrega el numero 40 y vuelve a convertir en tupla

""" datos = (10, 20, 30)
lista_datos = list(datos)
lista_datos.append(40)
datos = tuple(lista_datos)
print(datos) """

#6 - tupla cuantas veces aparece el numero 2

""" numeros = (1, 2, 2, 4, 5, 2)
contador = 0

for numero in numeros:
    if numero == 2:
       contador += 1

print(f"El numero dos se encontró {contador} veces") """

#numeros = (1, 2, 2, 3, 4, 2)
#print ("el numero ->2<- se repite",numeros.count(2), "veces.")

#7 - crea un conjunto a aprtir de la lista nombre (ana luis carlos aca) y muestra el resultado

""" nombres = ["ana", "luis", "carlos", "ana"]
conjunto_nombres = set(nombres)
print(conjunto_nombres) """

# 8 - Crea un conjunto con los nbumeros del 1 al 5

""" numeros = {1, 2, 3, 4, 5}
print(0 in numeros) """

# 9 - Dado A = {1 2 3} y B = {3 4 5} interseccion de ambos conjuntos
""" a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b)) """
# o print(set.intersection(a, b)

# 10 - Crea un diccionario con nombre, clave y ciudad

""" datos = {
    "nombre": "Pablo",
    "edad": 35,
    "ciudad": "Resistencia"
}
print(datos) """

# 11- dado el diccionario alumno = {nombre: pablo, nota: 7} y cambia a 9 la nota y agrega la clave aprobado con valor true
""" alumno = {
    "nombre": "Pablo", 
     "nota": 7
     }

alumno["nota"] = 9
alumno["aprobado"] = True

print(alumno) """

# 12 - Diccionario de colores, muestra todo

""" colores = {
    "rojo": "red",
    "azul": "blue",
    "verde": "green"
 }

for clave, valor in colores.items():
    print(f"{clave}: {valor}") """

# 1 lista de verduras y precios y mostrar diccionario completo

""" frutas = {
    "manzana" : 3500,
    "naranja" : 2500,
    "banana" : 3500,
    
}
for fruta, precio in frutas.items():
    print(f"Fruta: {fruta}, precio ${precio}") """




# 5 crear un set/conjunto


""" numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
impares = set()

for numero in numeros:
    if numero % 2 != 0:
        impares.add(numero)

print(impares)  """

#print(min(numeros))

# 6 mostrar elementos impares del conjunto

#impares = {1, 3, 5, 7, 9}
#print(len(impares))

# 9 crear una lista con 3 paises y ordenarlo por orden alfabetico

""" paises = ['Argentina', 'Francia', 'Brasil', 'Belgica', 'Angola', 'China']
paises.sort()
print(paises) """

""" numeros = [1, 2, 3, 4, 5, 6]
numeros.sort(reverse=True)
print(numeros) """

numeros = [12, 21, 23, 14, 5, 6]
ordenados = sorted(numeros)
print(ordenados)
print(numeros)