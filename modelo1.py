import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

#Cargar el set de datos 

df=pd.read_excel("datos_produccion.xlsx")
#Mostrar los primeros 5 valores
df.head() 
x=df["Horas Trabajadas"]
y=df["Productos Terminados"]

#Graficar los datos 
plt.scatter(x,y)
plt.title("datos")
plt.xlabel("Horas Trabajadas")
plt.show()

#===============gENERAR EL MODELO ===================
#Dividir el set en datos de entrenamiento y prueba
x_train, x_test, y_train, y_test=train_test_split(x.values.reshape(-1,1),
                                                  y.values.reshape(-1,1), train_size=0.2)
#Colocar el modelo 
modelo=LinearRegression()

modelo.fit(X=x_train.reshape(-1,1),y=y_train)

modelo.score(x_test,y_test)

#IMPRIMIR EL COEFICIENTE Y EL INTERCEPTO 
coeficiente=modelo.coef_
intercepto=modelo.intercept_

#imprimir la ecuacion de la recta 
print("ecuacion de la recta: y=",(coeficiente), "x+",intercepto)

#Coeficiente de determinacion 
print("coeficiente de determinacion: ",modelo.score(x_train,y_train))

#Hacer predicciones 
predicciones=modelo.predict(X=x_test)
print(predicciones[0:3,])

#Grafica del intervalo de confianza 
sns.regplot(data=df, x=df["Horas Trabajadas"],y=df["Productos Terminados"],scatter=True)
plt.title("Regresion lineal simple")
plt.show()

