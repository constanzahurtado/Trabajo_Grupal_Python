import random
import time

# DESARROLLO

# Hoy simularemos que nuestra tienda virtual tiene muchos usuarios comprando desesperadamente. De igual forma, 
# simularemos un alto movimiento de proveedores que renuevan nuestro stock de productos a ofrecer.

# Primero, desarrollaremos una forma de almacenar nuestro stock de dos productos. El primer producto tendrá 
# 120 unidades y el segundo 150.

stock_prodcuto1 = 120
stock_producto2= 150

# Luego, simularemos cada 3 segundos una compra de “n” unidades de cualquiera de los dos productos. 
# n representa un número aleatorio entre 1 y 10.
# Cada compra, como es natural, afecta el stock inicial de productos. Es decir, si una compra simulada es de 3 
# unidades del producto 1, este se debe descontar del stock.
# Cada 10 compras, el programa debe imprimir en pantalla el número de unidades disponibles por producto. ¿Lo lograron?
# Por último, cuando un producto tenga un stock de menos de 100 unidades, los proveedores enviarán automáticamente 50 
# unidades más. Esto se debe reflejar en el stock de cada producto.
# Lamentablemente, los proveedores solo tienen stock suficiente para enviar 150 unidades en total de productos 1 y 2.



#Es esta sección inicializamos los contadores utilizados en el ciclo while
compra = 0
reposicion1 = 0
reposicion2 = 0

while compra <=80: # Este while nos permitirá reiterar las compras hasta 80 veces
        while reposicion1 < 3 and reposicion2 < 3: #Este ciclo permite reponer los productos de cada stock en 50 unidades, cada vez 
                                                   #que baje de 100 unidades, pero sólo tres veces, al asignar el contador hasta 3
               
                if stock_prodcuto1 < 100: #Condicón que indica stock menor a 100
                            stock_prodcuto1 += 50 #Intrucción para sumar 50 unidades cuando se cumpla la condición 
                            print('Sumamos 50 a producto 1','stock resultante',stock_prodcuto1)
                            reposicion1 = reposicion1 + 1 #Contador reposición 
                            print('reposicion', reposicion1 )

                if  stock_producto2 < 100: #Condicón que indica stock menor a 100
                           stock_producto2 += 50 #Intrucción para sumar 50 unidades cuando se cumpla la condición 
                           print('Sumamos 50 a producto 2','stock resultante', stock_producto2)
                           reposicion2 = reposicion2 + 1 #Contador reposición 
                           print('reposicion', reposicion2 )
                
                #Esta parte del código se imprimen las compras con las condiciones que se solicitan. 
                time.sleep(3) #demora de 3 segundos entre cada ejecución de la compra.
                n1 = random.randrange(1, 11) #Cantidad de stock 1 a sustraer estimada mediante una función random
                n2 = random.randrange(1, 11) #Cantidad de stock 2 a sustraer estimada mediante una función random
                stock_prodcuto1 -= n1 #Resta stock 1 inicial y valor random
                stock_producto2 -= n2 #Resta stock 2 inicial y valor random
    
                compra += 1 #contador de compra

                #Output de stock
                print('Stock producto 1: ',stock_prodcuto1)
                print('Stock producto 2: ', stock_producto2)
                print('-------------------------------------')

                #Condición que permite ver el stock total cada 10 compras
                if compra == 11:
                        compra = 0
                        print('10 compras realizadas. Stock producto 1: ',stock_prodcuto1) 
                        print('10 compras realizadas. Stock producto 2: ',stock_producto2) 

        #Repetimos el código que permite imprimir las compras condicionadas
        time.sleep(3)
        n1 = random.randrange(1, 11)
        n2 = random.randrange(1, 11)
        stock_prodcuto1 -= n1
        stock_producto2 -= n2
    
        compra += 1
        print('Stock producto 1: ',stock_prodcuto1)
        print('Stock producto 2: ', stock_producto2)
        print('-------------------------------------')

        if compra == 11:
            compra = 0
            print('10 compras realizadas. Stock producto 1: ',stock_prodcuto1) 
            print('10 compras realizadas. Stock producto 2: ',stock_producto2) 
        
        #Este bloque permite terminar el ciclo cuando uno de los productos es inferior o igual a 10, porque 
        #el número máximo en la función random es 10. Así no se arrojan números negativos 
        if stock_prodcuto1 <= 10 or stock_producto2 <= 10:
            break


