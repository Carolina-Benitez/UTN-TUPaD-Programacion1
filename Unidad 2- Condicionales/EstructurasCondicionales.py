#Solicite edad. Si es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#Solicite nota. Si la nota es mayor o igual a 6, mostrar “Aprobado”; en caso contrario mostrar “Desaprobado”

nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Permita ingresar solo números pares. Si ingresa un número par: "Ha ingresado un número par"; sino: "Por favor, ingrese un número par"

numero = float(input("Ingrese un numero: "))

#verificar si es par
if numero %2==0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")


#Solicita edad y mostra a cuál de las categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/joven")
else:
    print("Adulto")

#Introducir contraseña entre 8 y 14 caracteres (incluyendo 8 y 14). 
#Si ingresa contraseña de longitud adecuada, "Ha ingresado contraseña correcta"; sino, "Ingrese contraseña entre 8 y 14 caracteres"

contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
longitud = len(contraseña) #cantidad de elementos que tiene el string

#verificar la longitud
if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#Tomar lista numeros_aleatorios, calcule moda, mediana y media y las compare para definir si hay sesgo positivo, negativo o no hay.

import random
import statistics

#definir la lista numeros_aleatorios
numeros_aleatorios = {random.randint(1, 100) for i in range(50)}

#calcular la media, mediana y moda
media= statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)

#intentamos obtener moda, puede haber un error si no existe una moda clara
try:
    moda = statistics.mode(numeros_aleatorios)
except statistics.StatisticsError:
    moda = "No hay una moda unica"

#imprimimos los resultados
print("Lista de numeros aleatorios:" , numeros_aleatorios)
print("Media:", media)
print("mediana:", mediana)
print("Moda:", moda)

#determinamos si hay sesgo
if isinstance(moda, int): #solo comparamos si hay una moda
    if media > mediana and media > moda:
        sesgo = "Sesgo positivo"
    elif media < mediana and media < moda: 
        sesgo = "Sesgo negativo"
    else:
        sesgo = "No hay sesgo"
else:
    sesgo = "No se puede determinar sesgo debido a que no hay una moda unica."

print("Sesgo:", sesgo)


#Solicite una frase o palabra. Si termina con vocal, añadir un signo de exclamación al final; sino, dejarlo tal cual lo ingresó

palabra = input("Ingresa una palabra o frase: ")

#obtener el ultimo caracter 
ultima_letra = palabra[-1]

#verificar si el ultimo caracter es una vocal
if ultima_letra == "a" or ultima_letra == "A" or ultima_letra == "e" or ultima_letra == "E" or ultima_letra == "i" or ultima_letra == "I" or ultima_letra == "o" or ultima_letra == "O" or ultima_letra == "u" or ultima_letra == "U":
    palabra= palabra + "!"

print(palabra)

#Solicita nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere nombre en mayúsculas. #2. Si quiere nombre en minúsculas. #3. Si quiere nombre con la primera letra mayúscula.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada

nombre = (input("Ingrese su nombre: "))

#mostrar opciones
print("¿De qué manera te gustaría ver tu nombre?")
print("1. En mayúsculas.")
print("2. En minúsculas.")
print("3. Con la primera letra en mayúscula.")

#solicitar la opción que desea
opcion = int(input("Selecciona la opción 1, 2 o 3: "))

#transformar el nombre según la opción elegida
if opcion == 1:
    resultado = nombre.upper()  # Convierte todo a mayúsculas
elif opcion == 2:
    resultado = nombre.lower()  # Convierte todo a minúsculas
elif opcion == 3:
    resultado = nombre.capitalize()  # Convierte la primera letra a mayúscula
else:
    resultado = "Opción no válida."

#imprimir el resultado
print("Resultado:", resultado)

#Pida la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías y mostrar el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremoto del 1 al 10: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")

#Preguntar en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
#El programa deberá utilizar esa información para mostrar si se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En que hemisferio se encuentra? N: norte, S: sur: ")
mes = int(input("Ingrese el mes en numero: "))
dia = int(input("Ingrese el dia en numero: ")) 

#validar que los valores ingresados sean correctos
if hemisferio not in ['N', 'S']:
    print("Hemisferio no válido. Ingresa 'N' para el hemisferio norte o 'S' para el hemisferio sur.")
elif mes < 1 or mes > 12:
    print("Mes no válido. Ingresa un número entre 1 y 12.")
elif dia < 1 or dia > 31:
    print("Día no válido. Ingresa un número entre 1 y 31.")
else:
    #determinar la estación según el hemisferio y la fecha

    #NORTE
    if hemisferio == 'N':
        if (mes == 12 and dia >=21) or (mes == 1) or (mes == 2) or (mes == 3 and dia < 21):
            print("Invierno")
        elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia < 21):
            print("Primavera")
        elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia < 21):
            print("Verano")
        else:
            print("Otoño")
    #SUR    
    elif hemisferio == 'S':
        if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia < 21):
            print("Verano")
        elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia < 21):
            print("Otoño")
        elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia < 21):
            print("Invierno")
        else:
            print("Primavera")









