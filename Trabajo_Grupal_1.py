print('Bienvenido')

# def cajero():
#     Fruta =input('Ingresar Fruta ') 
#     Cantidad = int(input('Ingresar cantidad '))
#     Precio = int(input('Ingresar precio '))

# cajero()
# cajero()
# cajero()
# cajero()
# cajero()

Fruta1=input('Ingresar Primera Fruta: ') 
Cantidad1 = int(input('Ingresar cantidad: '))
Precio1 = int(input('Ingresar precio: '))

Fruta2=input('Ingresar Segunda Fruta: ')
Cantidad2 = int(input('Ingresar cantidad: '))
Precio2 = int(input('Ingresar precio: '))

Fruta3=input('Ingresar Tercera Fruta: ')
Cantidad3 = int(input('Ingresar cantidad: '))
Precio3 = int(input('Ingresar precio: '))

Fruta4=input('Ingresar Cuarta Fruta: ')
Cantidad4 = int(input('Ingresar cantidad: '))
Precio4 = int(input('Ingresar precio: '))

Fruta5=input('Ingresar Quinta Fruta: ')
Cantidad5 = int(input('Ingresar cantidad: '))
Precio5 = int(input('Ingresar precio: '))

totalNeto = (Precio1*Cantidad1)+(Precio2*Cantidad2)+(Precio3*Cantidad3)+(Precio4*Cantidad4)+(Precio5*Cantidad5)
IVA = totalNeto * 0.19
totalIVA = IVA + totalNeto

print('-------------------------------------')
print('Resumen Compra')
print(Fruta1, Cantidad1, Precio1)
print(Fruta2, Cantidad2, Precio2)
print(Fruta3, Cantidad3, Precio3)
print(Fruta4, Cantidad4, Precio4)
print(Fruta5, Cantidad5, Precio5)
print('-----------------------------------')
print('Total Neto: ',totalNeto)
print('IVA: ',IVA)
print('Total IVA: ',totalIVA)