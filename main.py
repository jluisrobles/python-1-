
# RETO 1
print ("----------RETO 1-----------")
"""• Crea una variable denominada cadena que almacene una cadena de texto.

• Crea una variable denominada entero que almacene un número entero.

• Crea una variable float que almacene un numero en decimal

• Crea una variable booleana que almacene un valor verdadero"""

cadena = "Grupo de trabajo:"
entero = 5
promedio = 2.5
activo = True

print(cadena, "/", entero, "/", promedio,"/", activo)

# RETO 2
print ("----------RETO 2-----------")
# 1. Hacer tres listas de 5 elementos de tipo str
nombre = ["Jose", "Maria", "Pedro", "Luis", "Ana"]
ciudad = ["Madrid", "Londres", "Tokio", "Pekin", "Paris"]
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

#2. Hacer una lista de lass tres listtas y llamarle matriz

matriz = [nombre, ciudad, dias]
print(matriz)

#3. Mostrar matriz [2]

print (matriz [2])

#4. Mostrar matriz [2,4]

print (matriz [2] [4])

#5. Mostrar el segundo carácter del elemento matriz [2,4]

print (matriz [2][4][2])

#6. Sustituir el elemento matriz [2] por otra lista de números

matriz [2] = [1, 2, 3, 4, 5]

#7. Mostrar ese elemento

print (matriz [2])

#8. Modificar el elemento matriz [1,3] por un booleano

matriz [1][3] = "True"
#9. Mostrar ese elemento

print (matriz [1:])

#10. Insertar al final de la primera lista un nuevo string

nombre.append("Carlos")
print (nombre)

#11. Eliminar el primer elemento de la primera lista

del nombre[0]
print (nombre)

#12. Eliminar el ultimo elemento de una lista

del ciudad[-1]
print (ciudad)
#13. Ordenar alfabéticamente la segunda lista

ciudad.sort ()
print (ciudad)

#RETO 3
print ("----------RETO 3-----------")
#1. Crear un tupla que almacene el nombre, apellido1, apellido2, numero de dni, fecha de nacimiento

mi_tupla = ("Pedro", "Gil", "Lopez", 47889654 , "12/01/1988")

#2. Empaquetar cada dato en una variable diferente.

nombre, apellido1, apellido2, dni, nacimiento = mi_tupla

#3. Mostrar el valor de todas las variables generadas en el punto anterior
print(nombre)
print(apellido1)
print(apellido2)
print(dni)
print(nacimiento)

#RETO4
print ("----------RETO 4-----------")
"""1. Crear un diccionario que almacene el nombre, apellido1, apellido2, numero 
de dni, fecha de nacimiento y aficiones de una persona. Las aficiones
deben ser una lista de str."""

usuario = {"nombre": "Pedro", "apellido1" : "Gil", "apellido2" : "Lopez", "dni": 47889654,
           "nacimiento": "12/01/1988", "aficiones": ["leer", "correr", "video juegos"] }

#2. Mostrar cada valor del diccionario de manera individual.

print(usuario["nombre"])
print(usuario["apellido1"])
print(usuario["apellido2"])
print(usuario["dni"])
print(usuario["nacimiento"])
print(usuario["aficiones"])

#3. Mostrar todas las claves

print (usuario.keys())

#4. Mostrar todos los vavlores

print (usuario.values())