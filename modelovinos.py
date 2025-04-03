import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

#Datos
df=pd.read_csv("C:/Users/sebas/Inteligencia Artificial/WineQT.csv")

#Tamaño del df
df.shape

#Dar la descripcion estadistica 
df.describe()

#Eliminar la ultima columna 
df=df.iloc[:,:-1]

#Mostrar los resultados
print(df)
#Hacer nuevamente la descripcion estadistica 
df.describe()
#Dar informacion de las variables
df.info()
#=================Visualizar la relacion de las variables=============#
#Visualizar la informacion de la variable fixed acidity vs volatile acidity 
plt.figure(figsize=(8,6))
sns.scatterplot(x='fixed acidity',y='volatile acidity',data=df,color='blue')
plt.xlabel('Fixed Acidity')
plt.ylabel('Volatile Acidity')
plt.show()

#Scatter plot for citric acid vs residual sugar 
plt.figure(figsize=(8,6))
sns.scatterplot(x='citric acid', y='residual sugar',data=df, color='green')
plt.title('Scatter Plot of chloride and free sulphure dioxide')
plt.xlabel('Chlorides')
plt.ylabel('free sulfur dioxide')
plt.show()

#Scatter plot for fixed acidity vs volatile acidity 
plt.figure(figsize=(8,6))
sns.scatterplot(x='chlorides', y='free sulfur dioxide', data=df, color='red')
plt.title('Scatter plot of chloride and free sulfure dioxide')
plt.xlabel('chlorides')
plt.ylabel('free sulfur dioxide')
plt.show()

#Scatter plot for fixed total sulfur dioxide vs density 
plt.figure(figsize=(8,6))
sns.scatterplot(x='total sulfur dioxide',y='density',data=df, color='purple')
plt.title('Scatter Plot of total surface dioxide and density')
plt.xlabel('total sulfur dioxide')
plt.ylabel('density')
plt.show()

#Scatter plot for fixed acidity vs volatile acidity 
plt.figure(figsize=(8,6))
sns.scatterplot(x='pH',y='sulphates', data=df, color='orange')
plt.title('Scatter Plot of pH and sulphate')
plt.xlabel('pH')
plt.ylabel('sulpahte')
plt.show()

#Haz un heatmap para ver la correlacion entre las variables 
correlation_matrix = df.corr()

#plt.figure(figsize=(10,8)) #Ajusta el tamaño la figura como se necesite 
sns.heatmap(correlation_matrix)
plt.title('Correlation Matrix')
plt.show()

#===========================crea el modelo de regresion===========#
X=df.drop('quality', axis=1)
y=df.quality

#Separar los datos en engrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("X_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

#Seleccionar modelo
modelo=LinearRegression()

#Entrenar el modelo 
modelo.fit(X_train,y_train)

#Coeficiente de determinacion
modelo.score(X_test, y_test)

#Coeficientes
coef=modelo.coef_
coef

#Intercepto
intercep=modelo.intercept_
intercep

print("Ecuacion de la recta: y=",(coef),"xi+",intercep)

#Realizar predicciones
predicciones=modelo.predict(X_test)
print(predicciones[0:3,])

#Revisar el error
rmse=mean_squared_error(
    y_true=y_test,
    y_pred=predicciones,
    squared=False
    )
rmse