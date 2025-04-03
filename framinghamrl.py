'''De acuerdo con el archivo de Framingham, realiza un modelo de regresión 
logística que permita predecir si un paciente tiene riesgo a 10 años de 
sufrir enfermedad coronaria en el futuro. El conjunto de datos proporciona 
la información de pacientes que incluye más de 4000 registros y 15 atributos.
Realiza lo siguiente:'''

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
df=pd.read_csv("C:/Users/sebas/Inteligencia Artificial/framingham.csv")
#1.Revisa los primeros 5 valores
print(df.head())
#2.Revisa los valores de presión arterial BPMeds, para comprobar que tienen valores nulos
valNul= df['BPMeds'].isnull()
#3.Revisa las columnas
print(df.columns)
#4.Revisa todos los datos nulos
nulos = df.isnull().sum()
#5.Saca el valor medio de cada columna y rellena los valores nulos con esa información (investiga como hacerlo).
df.fillna(df.mean(), inplace=True)
#6.Comprueba que ya no hay datos nulos
df.isnull().sum()
print(df.isnull().sum())
#7.Guarda en una lista los nombres de las columnas
columnas_nombre = df.columns.tolist()
print(columnas_nombre)
#8.Transforma los valores de los datos de todas las columnas en el intervalo 0 y 1
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
#9.Separa las variables X y Y, donde Y es TenYearCHD y el resto son las X
X= df.drop(columns="TenYearCHD")
Y= df["TenYearCHD"]
#10.Divide el set de datos en entrenamiento y prueba
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
#11.Crea el modelo de regresión logística
modelo = LogisticRegression(solver='saga', max_iter=500)
#12.Entrena el modelo
modelo.fit(X_train,Y_train)

#13.Saca el score del modelo
score=modelo.score(X_test,Y_test)
print(score)
#14.Realiza la predicción de los 10 primeros valores de la variable X_test
predict=modelo.predict(X_test[:10])
print(f"Predicción: {predict}")
#15.Realiza el reporte del modelo
reporte = classification_report(Y_test, modelo.predict(X_test))
#16.Saca la matriz de confusión
matrix_conf = confusion_matrix(Y_test, modelo.predict(X_test))