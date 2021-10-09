# # A una variable se le asigne un mensaje motivador que incluya los nombres de todos los integrantes. 
# # Se le asigna a la variable 'mensajeMotivador' un valor de tipo String. Luego, se imprime con la función 'print'.
# mensajeMotivador = 'Te deseamos lo mejor en este curso de Python, Atte. Constanza, Pablo, Alejandro y Emanuel'
# print(mensajeMotivador)

# # ¿Qué tipo de dato puede ser?: Es un tipo String. 

# # Se asegure que todos su caracteres estén en mayúscula.
# # Se crea la variable 'mensajemayuscula', y se aplica la función 'upper()' en la veriable 'mensajeMotivador', para que aparezca en mayúscula.
# # Luego, se imprime con la función 'print'.

# mensajemayuscula = mensajeMotivador.upper()
# print(mensajemayuscula)

# # Elabore una lista con cada palabra del string.
# # Se crea la variable 'mensajeseparado', y se aplica la función 'split(espacio)' en la veriable 'mensajeMotivador', para separar los elemetos del mensaje principal.
# # Luego, se imprime con la función 'print'.

# mensajeseparado = mensajeMotivador.split(' ')
# print(mensajeseparado)

# # Cada integrante del grupo debe reconocer en qué índice está su nombre.
# # Se crea la variable 'indice' con el nombre de cada integrante, y se aplica la función 'find("Nombre")' en la veriable 'mensajeMotivador', para sencontrar el ídice de cada uno.
# # Luego, se imprime con la función 'print'.

# indiceConstanza = mensajeMotivador.find("Constanza")
# print('El índice de Constanza es: ',indiceConstanza)

# indicePablo = mensajeMotivador.find("Pablo")
# print('El índice de Pablo es: ',indicePablo)

# indiceAlejandro = mensajeMotivador.find("Alejandro")
# print('El índice de Alejandro es: ',indiceAlejandro)

# indiceEmanuel = mensajeMotivador.find("Emanuel")
# print('El índice de Emanuel es: ',indiceEmanuel)

# # Indique cuántas palabras tenía el string.
# # Se crea la variable 'numeroplabras' y se aplica la función 'len("Nombre")' en la veriable 'mesajeseparado', que permite conta el número de palabras en el mensaje.
# # Luego, se imprime con la función 'print'.
# numeroplabras = len(mensajeseparado)
# print(numeroplabras)

# # Imprima una tupla con todas las palabras del string.
# # Se crea la variable 'tupla' y se aplica la función 'tuple' en la veriable 'mensajeseparado', que permite generar una tupla.
# # Luego, se imprime con la función 'print'.

# tupla = tuple(mensajeseparado)
# print(tupla)

# # ¿Con qué función podrían obtener el mensaje por teclado al ejecutar el programa? Implementarlo!.
# # Se crea la variable 'mensajeNuevo' y se aplica la función 'input' para permitir a un usuario ingresar un mensaje.
# # Luego, se imprime con la función 'print'.

# mensajeNuevo = input('Escriba un mensaje motivador ')
# print(mensajeNuevo)

# usuario =input('Ingrese su nombre de usuario')
# mensaje = 'Bienvenido ', usuario
# print(mensaje)

# •	Esta aplicación debe entregar la posibilidad de iniciar sesión con un perfil individual.
# •	Generalmente, uno ingresa a su cuenta personal en una página, ésta te saluda y te reconoce


#Intentemos replicar esto. Crea un string con el nombre de al menos 7 usuarios de tu aplicación.

usuarios = 'Sofía,Luís,Antonio,Juan,Sandra,Estéban,Lucía'
print(usuarios)

# •	Ahora piensa en tres de ellos. Búscalos en la lista con el método adecuado.

print(usuarios.find('Antonio'))
print(usuarios.find('Luís'))
print(usuarios.find('Sofía'))

# •	Convierte tu string en una lista, en la cual cada elemento es un usuario.

listaUsuarios = usuarios.split(',')
print(listaUsuarios)

# •	Imprima en pantalla la cantidad usuarios que tiene tu aplicación.

print(len(listaUsuarios))

# •	Imprima en pantalla un mensaje de saludo a los diferentes usuarios. 
# ¿Qué técnica puedes utilizar para realizar esto?

mensaje1 = 'Bienvenido a nuestro sitio ', listaUsuarios[0]
mensaje2 = 'Bienvenido a nuestro sitio ', listaUsuarios[1]
mensaje3 = 'Bienvenido a nuestro sitio ', listaUsuarios[2]
mensaje4 = 'Bienvenido a nuestro sitio ', listaUsuarios[3]
mensaje5 = 'Bienvenido a nuestro sitio ', listaUsuarios[4]
mensaje6 = 'Bienvenido a nuestro sitio ', listaUsuarios[5]
mensaje7 = 'Bienvenido a nuestro sitio ', listaUsuarios[6]

print(mensaje1)
print(mensaje2)
print(mensaje3)
print(mensaje4)
print(mensaje5)
print(mensaje6)
print(mensaje7)








