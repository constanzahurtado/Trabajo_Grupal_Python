# DESARROLLO
# Como buen desarrollador, para comenzar a poder trabajar de manera óptima, es necesario que debamos 
# preparar las herramientas necesarias para inicializar nuestro proyecto, esto incluye tener ya nuestro editor de texto
# y la versión de Python disponible en nuestro equipo.

# Familiarizado ya con estos componentes debemos prepararnos para realizar las siguientes acciones, para simular el 
# funcionamiento de tu aplicación.

# Deben crear un inventario de 15 productos relativos al ámbito ropa deportiva. Cada producto tiene un stock y un valor 
# asociado.

# De forma conjunta deben imprimir en pantalla y de forma amigable, una primera sección de 5 productos al azar. Luego, 
# si un usuario indica por terminal que quiere ver más productos, se muestran los siguientes cinco productos al azar. 
# Por último, el usuario debe volver a indicar que quiere ver los últimos cinco productos con sus respectivos precios
# y stock.

# El producto de este trabajo deben publicarlo en sus repositorios github.
# Primer valor (posición 0) lista es Stock
# Segundo valor (posición 1) lista es Precio

#Primero 
import random

#Primero se construye un diccionario con los productos deportivos
diccionarioDeportivo = {'poleras':[100, 1999], 
                        'jogger':[60, 2000],
                        'short':[70, 3000],
                        'sudadera':[30, 1500],
                        'zapatillas':[28, 3999],
                        'bolso':[65,6000],
                        'guantes':[16,2000],
                        'tops':[40,2500],
                        'calcetines':[80,1500],
                        'gorros':[30,999],
                        'mochila':[60,1000],
                        'tank':[40,520],
                        'polerón':[50,4999],
                        'calza':[42,7000],
                        'conjunto':[30,5200],
                        }

primera_seleccion = random.sample(list(diccionarioDeportivo.items()), k = 5)#Variable que almacena 5 de los productos deportivos definidos en el diccionario
productos_por_mostrar = list(diccionarioDeportivo.keys())

print('Bienvenido, aquí te mostramos 5 de nuestros productos: ')
print(primera_seleccion) #Se muestran los 5 primeros productos

respuesta = input('¿Desea ver más productos? s/n: ')
#Para mostrar los siguientes 5 productos, se remueven los ya mostrados con un loop for. 
if respuesta == 's':
    for producto in primera_seleccion:
      productos_por_mostrar.remove(producto[0]) #Con la función remove se quitan los productos mostrados en "primera_seleccion"

segunda_seleccion = random.sample(productos_por_mostrar, k = 5)#Se crea la variable seleecion conformada por los productos que continúan en el diccionario 
print('Estos son los siguientes productos: ',segunda_seleccion)#después de haber sido removidos.

respuesta = input('¿Desea ver los siguientes productos? s/n: ')
#Para mostrar los productos que quedan, se realiza el mismo procedimiento, pero el recorrido se realiza en la variable "segunda_muestra"
if respuesta == 's':
    for producto in segunda_seleccion:
        productos_por_mostrar.remove(producto)

tercera_seleccion = random.sample(productos_por_mostrar, k = 5)#Se crea la variable seleecion conformada por los productos que continúan en el diccionario
print('Estos son los siguientes productos: ', tercera_seleccion)#después de haber sido removidos.
print('Hasta aquí nuestra aplicación. Espereamos que haya sido de su Agrado.')















#    list(diccionarioDeportivo.keys()).remove(i)

# if respuesta == 's': 
#     print('Aquí te mostramos otros productos: ')
#     print((random.sample(list(diccionarioDeportivo.items()), k = 5)))

# print(productos_por_mostrar)