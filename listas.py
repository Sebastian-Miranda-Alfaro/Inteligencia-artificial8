# Creación de una lista con diferentes tipos de datos
lista1 = [1, 2, 3, 4, "Sebastian", [True, False, True]]

# Imprime la lista completa
print(lista1)

# Acceder a elementos individuales de la lista usando índices
lista1[0]  # Primer elemento de la lista -> 1
lista1[5]  # Último elemento, que es otra lista -> [True, False, True]

# Slicing (rebanado de listas) para obtener subconjuntos
lista1[0:4]   # Desde el índice 0 hasta el 3 -> [1, 2, 3, 4]
lista1[3:]    # Desde el índice 3 hasta el final -> [4, 'Sebastian', [True, False, True]]
lista1[-1]    # Último elemento -> [True, False, True]
lista1[-3:]   # Últimos tres elementos -> [4, 'Sebastian', [True, False, True]]

# Doble referencia en listas anidadas
lista1[5][1]  # Accede al segundo elemento de la lista interna -> False

# Acceso a elementos de la lista anidada usando índices negativos
lista1[-1][-2]   # Segundo elemento de la lista interna -> False
lista1[-1][-2:]  # Desde el segundo elemento en adelante -> [False, True]

# Operaciones con listas
lista1.append([5, 2])  # Agrega una lista al final de lista1
lista1.append(3.45)    # Agrega un número flotante al final de lista1

# Extend: agrega los elementos de otra lista a la lista original
lista2 = [1, 2]
lista2.extend([3, 4, True])  # lista2 ahora es [1, 2, 3, 4, True]

# Insert: inserta un elemento en una posición específica
lista2.insert(0, "Y")  # Inserta "Y" en la posición 0 -> ['Y', 1, 2, 3, 4, True]

# Uso de 'del' para eliminar elementos por índice
x = [1, 2, 3]
del x[1]  # Elimina el segundo elemento -> [1, 3]

# Remove: elimina el primer elemento que coincida con el valor especificado
z = [1, 2, 3, 'h', 5, 'h']
z.remove('h')  # Elimina la primera aparición de 'h' -> [1, 2, 3, 5, 'h']
print(z)

# Reverse: invierte el orden de los elementos en la lista
r = [4, 6, 1, 3, 2]
r.reverse()  # Ahora r = [2, 3, 1, 6, 4]

# Sort: ordena la lista en orden ascendente
r.sort()  # r ahora es [1, 2, 3, 4, 6]
print(r)

# Ordenar en orden descendente
t = ['R', 'C', 'Python', 'Java', 'Raul']
t.sort(reverse=True)  # Ordena en orden alfabético inverso
print(t)

# Obtener el índice de un valor en una lista
x3 = [10, 30, 20]
print(x3.index(30))  # Devuelve 1, ya que 30 está en la posición 1

# Contar cuántas veces aparece un valor en la lista
nombre = ['Sebastian', 'Maria', 'Sebastian', 'Emiliano']
print(nombre.count('Sebastian'))  # Devuelve 2, ya que "Sebastian" aparece dos veces

'''Escribir un programa que almacene las asignaturas de un curso: matematicas 
IA IO, AMov, almacenamiento en una lista y preguntarle al usuario cual fue la calificacion'''
materias=['matematicas','IA','IO','AMov','almacenamiento']
notas=[]
for i in materias:
    nota=input("Introduce la calificacion de "+i+": ")
    notas.append(nota)
#Mostrar las materias y las calificaciones
for i in materias:
    print(str(i)+" "+str(notas[materias.index(i)]))
    