# Considerando los avances realizados en nuestro proyecto, se solicita crear y agregar sentencias que nos 
# permitan manipular un stock de productos. Para ello debemos aplicar lo siguiente:

# - Definir el stock de un producto en una variable.
#Se almacena 100 unidades en una variable llamada manzana

manzana = 100

# - Definir una forma de solicitar el stock disponible del producto por consola.
#Aquí se almacena en una variable "producto" el nombre de este y con print se imprime el stock correspondiente. Si el 
# producto no existe, arroja otro mensaje que indica que el producto no existe.

producto = input("Ingrese el nombre del producto: ")
if producto =='manzana':
    print('Hay ', manzana)
else:
    print('El producto no existe')

# # - Definir una forma de solicitar unidades del producto por consola. Este número de productos se almacenarán en una 
# # nueva variable llamada ‘Productos seleccionados’.
# # - Los productos reubicados serán descontados del stock inicial.
# # - El programa debe verificar que existan unidades disponibles.
# #Con una condición en la cual se indica que si producto seleccionado es mayor a la variable manzana, se entrgue un mensaje
# #que indique que no hay stock. De lo contrario, se restará la cantidad solicitada al stock original. 

productosSeleccionados = int(input('¿Cuántas unidades de manzana desea llevar?: '))
if productosSeleccionados > manzana:
    print('No hay Stock')
else:  
    manzana -= productosSeleccionados
    print('Stock disponible', manzana)


# - Al verificar las unidades disponibles, el programa entregará una unidad extra cuando se seleccionen más de 12 
# unidades. Verificar que el stock posibilite entregar una unidad extra. Sino se entregan las unidades justas. Cada
#  una de las posibles acciones debe imprimir un mensaje explicando lo realizado.
# - No se pueden solicitar más de 20 unidades en un mismo pedido.
# - Si el valor ingresado es superior al stock disponible, este debe entregar un mensaje indicando que no es posible 
# realizar esta acción debido a que no hay stock suficiente.


productosSeleccionados = int(input('¿Cuántas unidades de manzana desea llevar?: '))
if productosSeleccionados > 0: #Condición que indica que no deben ingresarse números negativos.
    if manzana > productosSeleccionados: #Condición que permite verificar que hay stock.
        if productosSeleccionados > 12 and productosSeleccionados <=20: #En esta condición se crea un rango de compra.
            productosSeleccionados += 1 #Si es mayor a 12, pero menor a 20, se sumará una unidad adicional. 
            print('Stock de manzanas es de: ', manzana - productosSeleccionados) #Indica el stock total después de ingresar una cantidad
        elif productosSeleccionados > 20 : # Condición que evita la compra de más de 20 unidades
            print('No es posible comprar más de 20 unidades')
        else:
           print('Stock de manzana es de:', manzana- productosSeleccionados) #Indica el stock total después de ingresar una cantidad   
    else:
         print('No tenemos stock suficiente')
else:
    print('No puede comprar unidades menor a 0')#Condición que indica que no deben ingresarse números negativos.


