#Crear archivo inicial con productos: 
#Crear un archivo de texto llamado productos.txt con tres productos. 
#Cada línea debe tener: nombre,precio,cantidad

with open("productos.txt", "w") as archivo:
    archivo.write("Celular,560,8\n")
    archivo.write("Tablet,490,12\n")
    archivo.write("Notebook,742,16\n")

#Leer y mostrar productos: 
#Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), 
#y muestre los productos en el siguiente formato: Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        print(partes)


#Agregar productos desde teclado: 
#Modificar el programa para que luego de mostrar los productos, 
#le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) 
#y lo agregue al archivo sin borrar el contenido existente.

#Mostrar los productos existentes
with open("productos.txt", "r") as archivo:
    print("\nProductos existentes:")
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        print(partes)

#Pedir nuevo producto
nuevo_producto = input("\nIngresa un nuevo producto (nombre, precio, cantidad): ")

#Agregar el nuevo producto al archivo (sin borrar lo anterior)
with open("productos.txt", "a") as archivo:
    archivo.write(nuevo_producto+"\n")

print("\nProducto agregado correctamente.")

#Volver a mostrar los productos actualizados
with open("productos.txt", "r") as archivo:
    print("\nProductos actualizados: ")
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        print(partes)


#Cargar productos en una lista de diccionarios: 
#Al leer el archivo, cargar los datos en una lista llamada productos, 
#donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.


#abrir el archivo y leer los productos

productos = []  #lista vacía donde se van a guardar los diccionarios 

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",") #separar por coma los datos de cada producto 
        if len(partes) == 3:  #asegurar que tenga las claves 'nombre, precio y cantidad'
            nombre = partes[0]
            precio = float(partes[1])
            cantidad = int(partes[2])
            producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
            productos.append(producto)  #agregar el diccionario con claves a la lista

#mostrar la lista 
print("\nLista de productos:")
for i in productos:
    print(i)

#Buscar producto por nombre: 
#Pedir al usuario que ingrese el nombre de un producto. 
#Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error.

#Leer los productos del archivo
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")
        if len(partes) == 3: 
            nombre = partes[0]
            precio = float(partes[1])
            cantidad = int(partes[2])
            producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
            productos.append(producto)

#Pedir producto a buscar
producto_ingresado = input("\nIngresá el nombre del producto que querés buscar: ")

#Buscarlo en la lista
encontrado = False
for i in productos:
    if i["nombre"].lower() == producto_ingresado.lower():
        print("Producto encontrado:")
        print("Nombre:", i["nombre"])
        print("Precio:", i["precio"])
        print("Cantidad:", i["cantidad"])
        encontrado = True
        break

#Si no se encontró, mostrar mensaje de error
if not encontrado:
    print("El producto no está en la lista.")
    


