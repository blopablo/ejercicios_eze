# 1 lista de frutas organizada
""" frutas = {
    "uva": 5000, 
    "manzana": 5000, 
    "pera": 5000}
for fruta, precio in frutas.items():

    print(f"fruta: {fruta}, precio: {precio}") """

# Listado de paises y sumo otro con append

""" Paises = ["Argentina", "China", "Grecia", "Colombia", "Chile", "Bolivia", "Ecuador", "Brasil", "Uruguay", "Paraguay"]
Paises.append("Zorro")
print(Paises)
Paises.sort(reverse=True)
print(Paises) """

# Listado de paises y muestro el segundo

""" Paises = ["Argentina", "China", "Grecia", "Colombia", "Chile", "Bolivia", "Ecuador", "Brasil", "Uruguay", "Paraguay"]

print(Paises[1])
 """
# Lista de 3 nombre y mostrar edad de la ultima  ////NO COMPLETADO

""" Nombres = {
    "Eze": 50, 
    "Manu": 50, 
    "Gera": 50
    }
for nombre, edad in Nombres.items():
     ultima_edad = edad
     print(f"La edad del ultimo en la lista es: {ultima_edad}") """

#5-Crear un set/conjunto con los números del 1 al 10 y mostrar el número más grande en el conjunto

Numeros = set(range(1, 11))
print(min(Numeros))
print(max(Numeros))

segundo_maximo = sorted(Numeros)[-2]
print(segundo_maximo)