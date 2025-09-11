#MOSTRAR TODOS LOS NUMEROS ENTEROS DESDE 0 HASTA 100 (INCLUYENDOLOS), EN ORDEN CRECIENTE, MOSTRANDO UN NUMERO POR LINEA.

for x in range(101):
    print(x)

#PEDIR UN NUMERO ENTERO Y DETERMINAR LA CANTIDAD DE DIGITOS QUE CONTIENE. 

numero = int(input("Ingresa un numero entero: "))

#usa valor absoluto abs para ignorar el signo negativo si lo hay, y contar solo los digitos
numero_abs = abs(numero)

#convertir a cadena y contar los dígitos
cantidad_digitos = len(str(numero_abs))

print(f"El número tiene {cantidad_digitos} dígito(s).")

#SUMAR TODOS LOS NUMEROS ENTEROS COMPRENDIDOS ENTRE DOS VALORES INGRESADOS, EXCLUYENDO ESOS DOS VALORES.

suma = 0 

num1 = int(input("Ingresa un primer valor: "))
num2= int(input("Ingresa un segundo valor: "))

for x in range(num1+1,num2): #+1 PARA EXCLUIR EL NUM1 PASANDO AL SIGUIENTE
    suma= suma + x 

print(f"La suma consecutiva entre los dos valores es: {suma}")

#INGRESAR NUMEROS ENTEROS Y SUMARLOS EN SECUENCIA. DETENERSE Y MOSTRAR EL TOTAL ACUMULADO CUANDO SE INGRESE UN CERO.

NUMERO_INVALIDO= 0
cont = 1
SUMA = 0 

num = int(input(f"ingrese valor n° {cont} (0 para terminar): "))

while num != NUMERO_INVALIDO:
    SUMA = SUMA + num
    cont = cont + 1
    num= int(input(f"ingresa valor n° {cont} (0 para terminar): "))
    
print(f"La suma secuencial de los numeros ingresados es: {SUMA}")

#ADIVINAR UN NUMERO ALEATORIO ENTRE 0 Y 9. AL FINAL, MOSTRAR CUANTOS INTENTOS FUERON NECESARIOS PARA ACERTAR EL NUMERO. 

import random #genera numeros aleatorios

numero_secreto = random.randint(0, 9) #genera el numero secreto entre 0 y 9
intentos = 0 #para llevar la cuenta de cuantas veces se intenta adivinar el numero
adivinado = False #bandera que indica que todavia no se adivino

print("Adivina el número (entre 0 y 9):")

while adivinado == False:
    intento = int(input(f"Ingresa tu intento n° {intentos + 1}: "))
    intentos += 1


    if intento == numero_secreto:
        adivinado = True
    else:
        print("Incorrecto, intenta de nuevo.")

print(f"¡ADIVINASTE! El número es: {numero_secreto}. El número de intentos fue: {intentos}.")


#MOSTRAR TODOS LOS NUMEROS PARES COMPRENDIDOS ENTRE 0 Y 100, EN ORDEN DECRECIENTE.

for x in range(100,-1,-2):
    print(x)

#CALCULA LA SUMA DE TODOS LOS NUMEROS COMPRENDIDOS ENTRE 0 Y UN NUMERO ENTERO POSITIVO INGRESADO POR EL USUARIO.

Suma = 0 

Numero = int(input("Ingresa un numero entero positivo: "))

#verificar que sea positivo
if Numero >= 0:
    for x in range(Numero+1): #+1 para que incluya ese numero ingresado
        Suma = Suma + x
print(f"la suma consecutiva entre 0 y {Numero} es: {Suma}")

#INGRESAR 100 NUMEROS ENTEROS. LUEGO, INDICAR CUANTOS DE ESTOS SON PARES, IMPARES, NEGATIVOS Y POSITIVOS. 

pares = 0
impares = 0
negativos = 0
positivos = 0

# Se usa un bucle for para ingresar exactamente 100 números
for cont in range(1, 101): #cont para mostrar en que numero del rango esta el bucle (en que vuelta esta)
    # Se lee cada número dentro del bucle
    numero = float(input(f"Ingrese el número {cont} de 100: ")) #input dentro bucle para pedir un nuevo numero en las 100 vueltas

    # Clasificación del número
    # Primero se verifica su signo

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

    # Luego se verifica si es par o impar (solo si es un entero)
    # Se usa .is_integer() para verificar si es entero
    if numero.is_integer():
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

print(f"Total de números pares: {pares}")
print(f"Total de números impares: {impares}")
print(f"Total de números positivos: {positivos}")
print(f"Total de números negativos: {negativos}")

#INGRESAR 100 NUMEROS ENTEROS Y LUEGO CALCULAR LA MEDIA DE ESOS VALORES 

suma = 0

for cont in range(1,101):
    num = int(input(f"ingresa numero {cont} de 100: "))
    suma = suma + num

#calcular la media (promedio)

media = suma / 100

print(f"la media de los 100 numeros ingresados es: {media}")

#INVERTI EL ORDEN DE LOS DIGITOS DE UN NUMERO INGRESADO.

numero = input("ingresa un numero: ")

#verificar si es negativo
if numero.startswith('-'):
    #invertir a partir del segundo carácter (ignorando el signo)
    invertido = '-' + numero[1:][::-1] #mantener el signo al principio + [1:] empieza desde el segundo elemento (ignorando el -) y [::-1] lo invierte
else:
    invertido = numero[::-1]  #si no es negativo, invertir todo

print("Número invertido:", invertido)
