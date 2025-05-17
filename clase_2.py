lista = [ "hola", 30, True ]

print(lista[0])
print(lista[1])
print(lista[2])

lista1 = [ "pablo", "antunez", "akbal" ]

print(f"id lista1: {id(lista1)}")
lista2= lista1
print(f"id lista2: {id(lista2)}")

lista1 = ["romi", "jorge", "manuel"]
print(f"id lista1 v2 : {id(lista1)}")
print(f"id lista1 v2 : {id(lista2)}")