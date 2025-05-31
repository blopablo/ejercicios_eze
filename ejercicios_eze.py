#nombre de usuario
""" usuario = input('ingreses un nombre de usuario: ')
print("el nombre de usuario es: ", usuario) """
  
""" nombre = input("Ingrese un nombre de usuario: ")
print("Nombre de usuario es:", nombre) """

#suma de dos numero
#shift + alt + flecha abajo (copia linea), Ctrl + l (señala linea)

""" num1 = int(input('ingrese un numero entero: '))
num2 = int(input('ingrese un numero entero: '))
suma = num1 + num2
print(f'la suma es: ' suma )
print(f"La suma de los numero es {num1 + num2}") """

#mayor o menor de edad

""" edad = int(input('ingrese su edad: '))
if edad >= 18:
    print('ústed es mayor de edad')
else:
    print('Usted es menor de edad') """

#Calcular indice de masa corporal

""" estatura = float(input('ingrese su altura mts: '))
peso = float(input('ingrese su peso en kg: '))
IMC = peso / estatura ** 2

print(f"su imc es de {IMC: .2f}") """

#q imprima si el numero es multiplo de 2 y 3 a la vez

#Pida al usuario que ingrese un caracter, que pueda ser letra minuscula, mayuscula, numero o caracter especial
""" caracter = input('ingrese un caracter: ')

if caracter.islower ():
    print('minuscula')
elif caracter.isupper ():
    print('mayuscula')
elif caracter.isdigit ():
        print('numero')
else:
    print('caracter epescial') """

#CADENA DE CARACTERES
""" caracter = input('ingrese una cadena de caracteres: ')

if "a" in caracter.lower():
    print('contiene la letra A')
else:
    print('la cadena no contiene') """
""" 
cadena = input('ingrese una cadena de caracteres: ')
contiene_a = False """

for caracter in cadena:
    if caracter.lower() == 'a':
        contiene_a = True
        break
if contiene_a:
    print('contiene a')
else:
    print('no contiene a')

#crear un programa q pida al usuario contraseña y de ser incorrecta q vuelva a pedir

""" USUARIO_VALIDO = 'Info'
CONTRASENA_VALIDA = '1234'

while True:
    usuario = input('ingreses su nombre de usuario: ')
    contrasena = input('ingrese su contraseña: ')

    if usuario == USUARIO_VALIDO and contrasena == CONTRASENA_VALIDA:
        print('acceso concedido!!')
        break
    else:
        print('usuario o contra') """
    
# 10 - Ingrese 3 numeros y determine el o los mayores

""" numero1 = int(input('Ingrese un numero: '))
numero2 = int(input('Ingrese otro numero: '))
numero3 = int(input('Ingrese un numero mas: '))

if numero1 > numero2 and numero1 > numero3:
    print('el primer numero ingresado es mayor')
elif numero2 > numero1 and numero2 > numero3:
    print('El segundo numero ingresado es mayor')
elif numero3 > numero1 and numero3 > numero2:
    print('El tercer numero ingresado es mayor')
elif numero1 == numero2 and numero1 >= numero3:
    print(f'El primer numero ingresado: {numero1} y el segundo numero ingresado {numero2} son iguales y mayores')
elif numero1 == numero3 and numero1 >= numero2:
    print(f'El primer numero ingresado: {numero1} y el tercer numero ingresado {numero3} son iguales y mayores')
elif numero3 == numero2 and numero3 >= numero1:
    print(f'El tercer numero ingresado: {numero3} y el segundo numero ingresado {numero2} son iguales y mayores')
else:
    print('los tres numeros son iguales') """

# 11 - suma de dos numeros si son pares

""" print('Jugaremos un juego, si usted ingresa dos numeros pares el programa dira la suma de ellos, en caso contrario dira que los numero no se corresponde')
num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))

if num1 % 2 == 0 and num2 % 2 == 0:
    print(f'La suma de {num1} + {num2} = {num1 + num2}')
elif num1 % 2 == 0 and num2 % 2 != 0:
    print(f'El segundo numero ingresado es un {num2}, por ende no es par')
else:
    print(f'El primer numero ingresado es un {num1}, por ende no es par') """

# 12 - Pedir una palabra al usuario y hacer que el programa lo imprima linea por linea

""" palabra = input('ingrese una palabra: ') 
for letra in palabra:
    print(letra) """

# 13 - 

""" n = int(input('ingrese un numero entero: '))
suma = n * (n + 1) // 2
print('la suma es: ', suma) """

# 14 - tabla de multiplicar

""" print('Bienvenido! aqui obtendras la tabla del 1 al 10 del numero que ingreses!')
numero = int(input('ingrese un numero entero: '))
print(f'{numero * 1}, {numero * 2}, {numero * 3}, {numero * 4}, {numero * 5}, {numero * 6}, {numero * 7}, {numero * 8}, {numero * 9}, {numero * 10}') """





