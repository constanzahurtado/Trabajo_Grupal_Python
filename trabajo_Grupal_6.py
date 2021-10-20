# DESARROLLO
# ● Guarde en una variable la siguiente información:

# ● Información de clientes: nombre, edad, identificador único.
# ● Información de productos: nombre, precio, identificador único y color.
# ● Información de la compra de cada cliente.
# Debe crear 10 clientes y 5 productos.
# La forma en que se organiza la información es a criterio del equipo. Es decir, ustedes definen 
# el número de variables y tipo de datos.

import random 
import time

#Creamos un diccionario para almacenar 10 clientes. Clave rut, lista incluye nombre y edad. 

diccionarioClientes = {'15.222.333-6':['Ana', 18],
                       '18.025.369-6':['Esteban', 30],
                       '13.111.345-9':['Pablo', 43],
                       '19.456.879-3':['Emanuel', 32],
                        '20.369.852-9':['Constanza', 32],
                        '8.523-963-5':['Alejandro', 32],
                        '11.258.369-8':['Sara', 31],
                        '14.258.741-2':['Juan',20],
                        '6.002.963-6':['Sebastián',60],
                        '20.321.548-9':['Luciano',65]}                     

#Creamos un diccionario para almacenar 5 productos. Clave identificador único, en la lista valor nombre del producto, precio y color.   
                   
diccionarioProductos = {100:['polera',5000,'azul'],
                        200:['conjunto',20000,'verde'],
                        300:['zapatilla',35000,'rojo'],
                        400:['gorro',6000,'amarillo'],
                        500:['bufanda',3500,'blanco']}

#Se crea Diccionario de compras con 5 compras. Clave id compra, tupla con id cliente,unidades, total compra y otra tupla con id productos.

diccionarioCompras = {1:('15.222.333-6',1,20000,(200)),
                      2:('18.025.369-6',1,6000, (400)),
                      3:('13.111.345-9',2,9500,(400, 500)),
                      4:('8.523-963-5',2,25000,(100,200)),
                      5:('14.258.741-2',1,35000,(300))}

# Sin definir funciones, utilice métodos necesarios para:

#Agregar Cliente.
diccionarioClientes ['21.001.369-8'] = ['Raúl',20] #Se agrega item al diccionario, asignando un valor lista a una clave.
print(diccionarioClientes)
print('---------------------------------------------------------------')

#Agregar Producto.  
diccionarioNuevoProducto = {600: ['polerón',13500,'negro']} #Se crea una nueva variable con el producto a agregar. 
diccionarioProductos.update(diccionarioNuevoProducto)#Aplicamos el método update a la variable creada. 
print(diccionarioProductos)
print('---------------------------------------------------------------')

#Mostrar Clientes: Muestra el listado de clientes.

for clave, valor in diccionarioClientes.items(): #Se utliza ciclo for para imprimir los valores de clave y valor del diccionario cliente.
    print(clave, ':', valor)
print('---------------------------------------------------------------')


# ● Mostrar Producto: Muestra el listado de productos.

for clave, valor in diccionarioProductos.items(): #Se utliza ciclo for para imprimir los valores de clave y valor del diccionario productos.
    print(clave, ':', valor)
print('---------------------------------------------------------------')

# ● Elimine clientes. ¿Qué información requiere para eliminar un cliente al azar?

claveDiccionario = random.choices(list(diccionarioClientes.keys()))#Se requiere de random para seleccionar un elemento al azar.
print(claveDiccionario)

del diccionarioClientes[claveDiccionario[0]] #Con el método del, eliminamos el elemento seleccionado al azar, que fue alamacenada en una variable.
print(diccionarioClientes)
print('---------------------------------------------------------------')

# ● Elimine productos. ¿Qué información requiere para eliminar el último producto agregado?

print(diccionarioProductos.popitem())#Se utiliza la función popitem, que elimina el último elemento de un diccionario. 
print(diccionarioProductos)
print('---------------------------------------------------------------')

# En el caso que la información se esté guardando en un diccionario.

# - Imprima todas las claves con un delay de 2 segundos.
#Con un ciclo for imprimimos las claves del diccionario clientes. Se utiliza time.sleep para generar el delay indicado. 
for clave in diccionarioClientes.keys():
    time.sleep(2) 
    print(clave)

print('---------------------------------------------------------------')

#Con un ciclo for imprimimos las claves del diccionario productos. Se utiliza time.sleep para generar el delay indicado.
for clave in diccionarioProductos.keys():
    time.sleep(2) 
    print(clave)
print('---------------------------------------------------------------')

# - Luego imprima los valores con un delay de 3 segundos.

#Con un ciclo for imprimimos los valores del diccionario clientes. Se utiliza time.sleep para generar el delay indicado.

for valor in diccionarioClientes.values():
    time.sleep(3) 
    print(valor)

print('---------------------------------------------------------------')

#Con un ciclo for imprimimos los valores del diccionario productos. Se utiliza time.sleep para generar el delay indicado.

for valor in diccionarioProductos.values():
    time.sleep(3) 
    print(valor)
print('---------------------------------------------------------------')

# Imprima en pantalla un listado que contenga los ID de los usuarios.
#Con un ciclo for imprimimos las claves del diccionario clientes. Se utiliza time.sleep para generar el delay indicado. 

for clave in diccionarioClientes.keys():
    time.sleep(1) 
    print(clave)
print('---------------------------------------------------------------')

# Modifique todos los ID. Agregue la siguiente cadena de caracteres: “_piloto” al final de cada ID.
# Imprima en pantalla los nuevos ID.
#Con un ciclo for se agrega a cada una de las claves de clientes '_piloto', concatenando esta cadena. Luego se imprime. 

for i in diccionarioClientes.keys():
    i += str('_piloto')
    print(i)
print('---------------------------------------------------------------')

# Elimine los últimos cuatro ID_clientes en el listado.
#En el ciclo for se delimita un rango de clientes a borrar, y con el método popitem nos aseguramos que sean los 4 
#últimos elementos. 

print(diccionarioClientes)

for i in range(4):
    diccionarioClientes.popitem()

print(diccionarioClientes)