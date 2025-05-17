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
contiene_a = False

for caracter in cadena:
    if caracter.lower() == 'a':
        contiene_a = True
        break
if contiene_a:
    print('contiene a')
else:
    print('no contiene a') """

#crear un programa q pida al usuario contraseña y de ser incorrecta q vuelva a pedir

USUARIO_VALIDO = 'Info'
CONTRASENA_VALIDA = '1234'

while True:
    usuario = input('ingreses su nombre de usuario: ')
    contrasena = input('ingrese su contraseña: ')

    if usuario == USUARIO_VALIDO and contrasena == CONTRASENA_VALIDA:
        print('acceso concedido!!')
        break
    else:
        print('usuario o contra')
    





