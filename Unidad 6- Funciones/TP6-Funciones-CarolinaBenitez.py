#CREAR FUNCION LLAMADA IMPRIMIR_HOLA_MUNDO QUE MUESTRE: "HOLA MUNDO!". LLAMAR A ESTA FUNCION DESDE EL PROGRAMA PRINCIPAL.

def imprimir_hola_mundo():
    print("Hola Mundo!")  

#Programa principal
imprimir_hola_mundo()  #Llamamos a la función para que se ejecute


#Crear función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
#Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    saludo = "Hola " + nombre + "!"
    return saludo

nombre_ingresado = input("Ingrese su nombre: ")
print(saludar_usuario(nombre_ingresado))


#Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) 
#que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
#Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    informacion = f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}"
    return informacion

#Pedimos los datos uno por uno al usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

#Llamamos a la función con los valores ingresados
print(informacion_personal(nombre, apellido, edad, residencia))


#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
#calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
#Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

#Función para calcular el área del círculo
def calcular_area_circulo(radio):
    area= 3.14*radio**2
    return area 

#Función para calcular el perímetro del círculo
def calcular_perimetro_circulo(radio):
    perimetro= 2*3.14*radio
    return perimetro

#Programa principal
radio_ingresado = float(input("Ingrese el radio del círculo: "))

print("El área del círculo es:",(calcular_area_circulo(radio_ingresado)))
print("El perímetro del círculo es:",(calcular_perimetro_circulo(radio_ingresado)))


#Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
#Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas= segundos // 3600
    return horas

segundos_ingresados = int(input("Ingrese una cantidad de segundos: "))

print("Los segundos ingresados equivalen a las siguentes horas: ")
print(segundos_a_horas(segundos_ingresados)) 


#Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro e imprima la tabla de multiplicar de ese número del 1 al 10. 
#Pedir al usuario el número y llamar a la funcion.

def tabla_multiplicar(numero):
    for i in range(1, 11):
       print(numero, "x", i, "=", numero * i)  #muestra cada línea de la tabla

#Pedimos el número al usuario
numero_ingresado = int(input("Ingrese un número entero: "))

#Llamamos a la función
tabla_multiplicar(numero_ingresado)


#Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros 
#y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)  #devolvemos una tupla que guarda varios resultados a la vez

resultados = operaciones_basicas(8, 2) #guardamos la tupla, todos los resultados juntos

print(operaciones_basicas(8, 2))


#Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
#y devuelva el índice de  masa corporal (IMC). 
#Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso // (altura)**2

peso_kilogramos= float(input("Ingrese su peso en kilogramos: "))
altura_metros= float(input("Ingrese su altura en metros: "))

print("Su indice de masa corporal es: ") 
print(round(calcular_imc(peso_kilogramos, altura_metros), 2))


#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius 
#y devuelva su equivalente en Fahrenheit. 
#Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return (celsius*9/5)+32

temperatura_en_celsius = float(input("Ingrese la tempertura en grados Celsius: "))

print("La temperatura en grados Fahrenheit es: ")
print(celsius_a_fahrenheit(temperatura_en_celsius))


#Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros 
#y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    return a + b + c / 3

num_1= float(input("Ingrese el primer numero: "))
num_2= float(input("Ingrese el sengundo numero: "))
num_3= float(input("Ingrese el tercer numero: "))

print("El promedio entre los numeros ingresados es: ")
print(calcular_promedio(num_1, num_2, num_3))
