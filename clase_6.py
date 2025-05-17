""" color_1 = "rojo"
color_2 = "verde"
color_3 = "rojo" """

#if color_1 != color_2 and color_2 != color_3 and color_1 == color_3:
#    print("los colores 1 y 3 son iguales")

#if color_1 != color_2:
 #   if color_2 != color_3:
  #      print("los colores 1 y 3 son iguales")

#Mayor o menor de edad
""" edad = int(input("ingrese su edad en numero: "))
if edad >= 18:
    print("usted es mayor de edad")
else:
    print("usted no es mayor de edad") """

#Numero ingresado

""" num = int(input("ingrese un numero entero: "))

if num > 0:
   print(num, "es un numero es positivo")
elif num < 0:
 print(num,"es un numero es negativo")
else:
   print("el numero es cero") """

#Multiplos de 2 y 3

""" num = int(input("ingresa un numero entero: "))
if num % 2 == 0 and num % 3 == 0:
    print(num, "es multiplo de 2 y 3 a la vez")
elif num % 2 == 0 and num % 3 != 0:
    print(num, "es multiplo de 2")
elif num % 2 != 0 and num % 3 == 0:
    print(num, "el numero es multiplo de 3")
else:
    print(num, "no es multiplo de ninguno") """

#tipo de caracter

""" caracter = input("ingrese un caracter: ")
if caracter.isupper():
    print("El caracter es una letra Mayuscula")
elif caracter.islower():
    print("El caracter es una letra minuscula")
elif caracter.isdigit ():
    print("El caracter es un numero")
else:
    print("El caracter es de orden especial") """

#ejercicio

""" numero = int(input("ingrese un numero entero"))
if numero % 2 == 0:
    print(numero, ", el numero es par")
else:
    print(numero, ", el numero es impar") """

#ejercicio profe con f string

""" numero = int(input("Ingrese un numero entero: "))

if numero % 2 == 0:
    print(f"el numero {numero} es par.")
else:
    print(f"el numero {numero} es impar.") """

numero = int(input("ingrese un numero: "))
if numero % 2 == 0 and numero % 3 == 0 and numero != 0:
    print(f"El numero {numero} es multiplo de 2 y 3")
elif numero % 2 == 0 and numero % 3 != 0:
    print(f"el numero {numero} es multiplo de 2")
elif numero % 2 !=0 and numero % 3 == 0:
    print(f"el numero {numero} es multiplo de 3")
elif numero % 2 != 0 and numero % 3 != 0:
    print(f"el numero {numero} es un numero primo")
else:
    print(f"el numero {numero} es cero") 

#usuario y contraseña

""" suario = input('ingrese su nombre de usuario: ')
contraseña = input('ingrese su contraseña: ')

if usuario == 'Flor' and contraseña == 'Flor2025':
    print('Acceso correcto. Bienvenido')
else:
    print('ingresaste mal tu usuario o contraseña. Intenta nuevamente') """