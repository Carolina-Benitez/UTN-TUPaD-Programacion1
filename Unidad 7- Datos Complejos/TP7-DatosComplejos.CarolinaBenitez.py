#Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

#Siguiendo con el diccionario precios_frutas, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

#Siguiendo con el diccionario precios_frutas, crear una lista que contenga únicamente las frutas sin los precios.

precios_frutas = {'Banana', 'Ananá', 'Melón', 'Uva'}
print(precios_frutas)

#Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

#diccionario vacío
contactos = {}

#cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto n°{i+1}: ")
    numero = input("Ingrese el número telefónico: ")
    contactos[nombre] = numero  #guardar nombre como key y número como value

#consultar un contacto
pedir_nombre = input("Ingrese un nombre para buscar su número: ")

if pedir_nombre in contactos:
    print(f"El número de {pedir_nombre} es: {contactos[pedir_nombre]}")
else:
    print("Ese contacto no existe.")

#Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra


#pedir una frase al usuario
frase = input("Ingresa una frase: ")

#separar la frase en palabras
palabras = frase.split()

#crear un conjunto (set) con las palabras únicas
palabras_unicas = set(palabras) #eliminar las repetidas 

#crear un diccionario para contar cuántas veces aparece cada palabra
conteo_palabras = {} #contador

for palabra in palabras: 
    if palabra in conteo_palabras: #si la palabra ya existe en el diccionario
        conteo_palabras[palabra] += 1 #sumo uno más a palabra ya existente
    else:
        conteo_palabras[palabra] = 1 # si no esta en el diccionario, la agrego con valor 1 

#mostrar resultados
print("Palabras únicas:")
print(palabras_unicas)

print("Cantidad de veces que aparece cada palabra:")
print(conteo_palabras)

#Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.


#crear un diccionario para guardar alumno y sus notas
alumnos_notas = {}

#pedir 3 alumnos
for i in range(3):
    nombre = input(f"Ingresa el nombre del alumno n°{i+1}: ")
    
    #pedir las 3 notas 
    n1 = float(input("Ingrese la primera nota: "))
    n2 = float(input("Ingrese la segunda nota: "))
    n3 = float(input("Ingrese la tercera nota: "))

    #guardar las notas como una tupla
    notas = (n1, n2, n3)
    
    #asociar el nombre con su tupla de notas
    alumnos_notas[nombre] = notas

#mostrar el promedio de cada alumno
print("Promedios de los alumnos:")
for nombre, notas in alumnos_notas.items(): #nombre (clave), notas (valor). 
    promedio = sum(notas) / len(notas) #sumar las notas, contar cuantas hay y dividir
    print(f"{nombre}: {promedio:.2f}") #promedio con dos decimales

#Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)

parcial_1 = {7, 5, 9, 6, 8}
parcial_2 = {4, 5, 8, 7, 6}

print("Estudiantes que aprobaron ambos parciales:", parcial_1)

#crear los conjuntos con los estudiantes que aprobaron cada parcial
parcial1 = {"Ana", "Juan", "Sofía", "Marcos"}
parcial2 = {"Juan", "Sofía", "Lucía", "Pedro"}

#estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

#estudiantes que aprobaron solo uno (diferencia simétrica)
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

#estudiantes que aprobaron al menos un parcial (unión)
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

#Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

productos = {"heladera": 6, "aire acondicionado": 4, "microondas": 8, "lavarropa": 5}

produc_ingresado_stock = input("Ingresa un electrodomestico para consultar stock: ")

if produc_ingresado_stock in productos:
    print(f"Stock actual de {produc_ingresado_stock}: {productos[produc_ingresado_stock]}") #muestra el stock del producto ingresado
    
    #agregar unidades al stock si el producto ya existe
    agregar_stock = input("¿Querés agregar unidades al stock de este producto? (si/no): ").lower()
    if agregar_stock == "si":
        cantidad_stock = int(input("¿Cuántas unidades querés agregar?: "))
        productos[produc_ingresado_stock] += cantidad_stock
        print(f"Nuevo stock de {produc_ingresado_stock}: {productos[produc_ingresado_stock]}")
    else:
        print("No se realizaron cambios en el stock.")

else: #si el producto no existe
    print("El producto no existe.")
    #opcion para agregar un nuevo producto
    nuevo_producto = input("¿Querés agregarlo al sistema? (si/no): ").lower()
    if nuevo_producto == "si":
        cantidad_stock = int(input("¿Cuántas unidades tiene?: "))
        productos[produc_ingresado_stock] = cantidad_stock
        print(f"Se agregó {produc_ingresado_stock} con stock {cantidad_stock}.")
    else:
        print("No se agregó ningún producto nuevo.")

#mostrar el diccionario actualizado
print("Stock actualizado de todos los productos:")
print(productos)

#Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

#diccionario donde las claves son tuplas (día, hora)
fechas_eventos = {
    ("viernes", "19:00hs"): "recital",
    ("sabado", "17:00hs"): "patinaje",
    ("domingo", "16:30hs"): "feria"
}

#consultar una actividad
consultar_actividad = input("¿Querés consultar qué actividad hay en cierto día y horario? (si/no): ").lower()

if consultar_actividad == "si":
    dia = input("Ingrese el día: ").lower()
    hora = input("Ingrese la hora (por ejemplo, 19:00hs): ").lower()

    #armar la tupla (día, hora) para buscarla en el diccionario
    dia_horario = (dia, hora)

    if dia_horario in fechas_eventos:
        print(f"Actividad del {dia} a las {hora}: {fechas_eventos[dia_horario]}")
    else:
        print("No hay actividades para ese día y hora.")

#Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

paises_capitales = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
print(f"Diccionario original: {paises_capitales}")

#invertir claves y valores 
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()} #recorre cada par (pais, capital) y los da vuelta

print(f"Invertido: {capitales_paises}")

