'''Graficar la funcion de f(x)=x^2-4x+3 en el rango [-2,6]'''
import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
    return x**2 -4*x + 3

x=np.linspace(-2,6,100)
y=f(x)

plt.plot(x,y)
plt.title("Graficar la funcion de f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

'''Crea dos listas, una con el nombre de 5 estudiantes y la otra con las 
calificaciones, posteriormente crea un gráfico de barras con ambas listas, 
agregando en cada barra un color diferente (si es necesario investiga como 
hacerlo).'''
estudiantes = ["Maria","Emiliano","Eduardo","Sebastian","Sofia"]
calificaciones = [10,6,8,10,7]
colores = ['pink','orange','blue','red','purple']
plt.bar(estudiantes, calificaciones, color=colores)
plt.xlabel("Estudiantes")
plt.ylabel("Calificacion")
plt.show()

'''Grafica la función fx(x)=sen(x)+cos⁡(x)en el intervalo 
[-2π,2π], primero crea un vector consecutivo en el rango mencionado, 
con 100 muestras y luego grafica.'''

def fx(x):
    return np.sin(x) + np.cos(x)
x=np.linspace(-2 * np.pi, 2 * np.pi,100)
y=fx(x)
plt.plot(x,y)
plt.title("Grafica de f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()