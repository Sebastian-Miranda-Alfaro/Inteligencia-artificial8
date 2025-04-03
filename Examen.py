'''Dado un diccionario con los nombres de estudiantes y sus calificaciones, 
realiza lo siguiente
A)Agrega un nuevo estudiante 
B)Actualizar la calificacion de un estudiante existente 
C)Obtener la calificacion de un estudiante en especifico 
D)Mostrar el promedio de calificaciones
E)Mostrar el estudiante con la calificacion mas alta y el de la calificacion mas baja'''

estudiantes={"Maria":9.5,"Sebastian":8.5,"Emiliano":7.5}
#A)
estudiantes["Eduardo"] = 10
#B)
estudiantes["Emiliano"] = 8
#C)
calificacionMaria = estudiantes.get("Maria")
print(f"La calificación de Maria es: {calificacionMaria}")
#D)
promedio = sum(estudiantes.values()) / len(estudiantes)
print(f"El promedio de calificaciones es: {promedio: }")
#E)
CalifMax = max(estudiantes, key=estudiantes.get)
CalifMin = min(estudiantes, key=estudiantes.get)

print(f"El estudiante con mayor calificación es: {CalifMax}")
print(f"El estudiante con menor calificación es: {CalifMin}")

'''Dada una lista de numeros enteros, realizar las siguientes operaciones
A)Agregar un nuevo numero a la lista 
B)Eliminar un numero especifico
C)Ordenar la lista en orden ascendente
D)Calcular el promedio de los numeros 
E)Encontrar el numero mayor y menor '''

listNum = [1,2,3,4,5]
#A) 
listNum.append(6)
#B)
listNum.remove(2)
#C)
listNum.sort()
#D)
promediolist = sum(listNum) / len(listNum)
#E)
mayor = max(listNum)
menor = min(listNum)
'''Se tiene un conjunto de datos de temperaturas (En grados celsius) 
de 7 ciudades durante 7 dias almacenado en una matriz 7x7 generada 
aleatoriamente entre -5°C Y 40°C. Se deben realizar las siguientes 
operaciones utilizando numpy 
A)Muestra la matriz original 
B)Calcula la temperatura promedio de cada ciudad (filas)
C)Obtener la temperatura mas alta por cada siudad
D)Convierte todas las temperaturas a grados farenheit'''
import numpy as np
#A)
temperatura = np.random.randint(-5, 41, (7, 7)) 
print(temperatura)
#B)
promediosTemp = [sum(fila) / len(fila) for fila in temperatura]
#C)
tempMax= [max(fila) for fila in promediosTemp]
#D)
farenheit = temperatura * (9/5) + 32

'''Se tiene un conjunto de datos que representa el numero de 
estudiantes que aprobaron un curso de matematicas en 6 semestres 
consecutivos. 
Se deben realizar las siguientes tareas utilizando Matplotlib
semestres =["2020-1","2020-2","2021-1","2021-1","2022-1","2022-2"]
aprobados =[120,150,180,160,200,220]
A)Crear un grafico de barras que muestre la cantidad de estudiantes 
aprobados por semestre 
B) Superponer un grafico de lineas en el mismo grafico para visualizar 
la tendencia de aprobacion 
C)Agregar titulos y etiquetas adecuadas
D)Mostrar la grafica con una cuadricula de fondo '''

import matplotlib.pyplot as plt
semestres = ["2020-1", "2020-2", "2021-1", "2021-2", "2022-1", "2022-2"]
aprobados = [120, 150, 180, 160, 200, 220]
#A)
plt.bar(semestres, aprobados)
#B)
plt.plot(semestres, aprobados)
#C)
plt.xlabel("Semestres")
plt.ylabel("Estudiantes Aprobados")
plt.title("Aprobados por Semestre")
#D)
plt.grid(True)
plt.show()
