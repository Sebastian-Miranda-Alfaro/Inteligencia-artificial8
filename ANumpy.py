'''1.Crear dos matrices de 5x5 A y B, con valores al azar y verificar
 que sean del mismo tamaño, súmalas. Después crea un vector X con la 
 primera fila de A y otro vector Y con la segunda fila de B y realiza
 una gráfica de X vs Y.'''
import numpy as np
import matplotlib.pyplot as plt

A = np.random.randint(1, 51, (5, 5)) #(inicio, fin, tamaño)
B = np.random.randint(1, 51, (5, 5))

if A.shape == B.shape:
    print("Las matrices A y B son del mismo tamaño.")
    
    C = A + B  
    print("\nMatriz A:\n", A)
    print("\nMatriz B:\n", B)
    print("\nMatriz (A + B):\n", C)
    
    X = A[0, :]  # 0 primera fila de A
    Y = B[1, :]  #1 para iniciar en la segunda fila de B

    print("\nVector X:", X)
    print("Vector Y:", Y)

    plt.figure(figsize=(8, 6))
    plt.plot(X, Y, marker='o', linestyle='-', color='red', label="X vs Y")
    
    plt.title("Gráfica de X vs Y")
    plt.xlabel("Valores de X")
    plt.ylabel("Valores de Y")
    plt.legend()
    plt.grid(True)
    plt.show()

else:
    print("Error: Las matrices A y B no son del mismo tamaño.")
    
'''Crea una variable llamada suma y guarda la suma de la columna
2 de la matriz A del inciso 1 con la columna 3 de la matriz B del mismo 
inciso.'''
colA = A[:, 1]  # 2 columna de A
colB = B[:, 2]  # 3 columna de B

suma = np.sum(colA + colB)

print("\nSegunda columna de A:", colA)
print("Tercera columna de B:", colB)
print("\nSuma total:", suma)

'''Crea un vector x con linspace de -10 a 10 100 valores, 
crea a y con la función coseno de x y gráfica, colocando el nombre de 
los ejes, la rejilla, el título de la gráfica y en color magenta'''

Vx = np.linspace(-10, 10, 100) #100 valores equidistantes entre -10 y 10
print(Vx)

a = np.cos(Vx) # Función coseno de x
#Fontsize personaliza el tamaño pata titulos o etiquetas 
plt.plot(Vx, a, color='magenta')
plt.title("Gráfica de la función coseno", fontsize=14)
plt.xlabel("Valores de x", fontsize=12)
plt.ylabel("cos(x)", fontsize=12)
plt.grid(True) #rejilla
plt.show() #Muestra la grafica 
'''Crea una matriz de 5x6 con valores aleatorios enteros entre 0 y 10.'''

matriz= np.random.randint(0,11, (5,6))
print(matriz)