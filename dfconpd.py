'''1.	crea una seria qu tenga como datos los números 1,2,3 y 4 y como 
índices los países:EU, Alemania, Colombia y Japon. Muestra el resultado y 
busca el valor que tiene el índice Japón.'''
import pandas as pd 
Paises = pd.Series([1,2,3,4],index=["EU","Alemania","Colombia","Japon"])
print(Paises["Japon"])

'''2.	Realiza una serie a partir de un diccionario, donde las claves 
sean los numero de playera y el valor sea el nombre del jugador, puedes 
inventarlos, luego inserta un nuevo jugador cuya camiseta es la 10 y se 
llama Cesar.'''

jugadores = {"Maria": 25, "Emiliano": 9, "Eduardo": 8, "Sebastian": 3, 
             "Sofia": 7}

serie = pd.Series(jugadores)
serie["Cesar"]=10
print(serie)

'''3.Escribir un programa que genere un dataframe llamado contabilidad, 
a partir de un diccionario con la siguiente información:
Llave Mes, que contiene una lista con los meses: enero, febrero, marzo 
y abril.
Llave ventas, que contiene una lista con las ventas de cada mes que son: 
30500, 35600, 28300, 33900.
Llave Gastos, que contiene un a lista con los gastos de cada mes: 22000,
 23400, 18100, 20700.
a)	Imprime el dataframe generado.
b)	Grafica gastos vs ventas en un diagraama de dispersión.'''
import matplotlib.pyplot as plt
Mes = ["enero","febrero","marzo","abril"]
Ventas=[30500,35600,28300,33900]
Gastos=[22000,23400,18100,20700]

Contabilidad = {'mes':Mes,'ventas':Ventas,'Gastos':Gastos}
df=pd.DataFrame(Contabilidad)
print(df)
fig, ax = plt.subplots()
ax.scatter(Gastos,Ventas)
plt.title("Grafica Gastos vs Ventas")
plt.xlabel("Gastos")
plt.ylabel("Ventas")
plt.grid(True)
plt.show()
