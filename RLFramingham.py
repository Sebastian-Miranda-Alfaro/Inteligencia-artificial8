import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import MinMaxScaler

df=pd.read_csv('framingham.csv')
#Revisión de los primeras 5 filas
df.head()
#Revision delos valores de presión arterial BPMeds, para comprobar que tienen valores nulos
bpMeds=df['BPMeds']
print(bpMeds)
#Revisión de las columnas
df.describe()
#Revisión de los datos nulos
df.isnull().sum()
#Saca el valor medio de cada columna y rellena los valores nulos con esa información
df=df.fillna(df.mean())
#Comprobación de que ya no hay datos nulos
df.isnull().sum()
#Guardar el nombre de las columnas en una lista
columnasN=df.columns
'''columasN=['male','age','education','currentSmoker','cigsPerDay','BPMeds','prevalentStroke','prevalentHyp','diabetes','totChol',
          'sysBP','diaBP','BMI','heartRate','glucose','TenYearCHD']'''
print(columnasN)
#8.	Transforma los valores de los datos de todas las columnas en el intervalo 0 y 1
scaler = MinMaxScaler()
df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

#9.	Separa las variables X y Y, donde Y es TenYearCHD y el resto son las X
X= df.drop(columns="TenYearCHD")
Y= df["TenYearCHD"]

#10.	Divide el set de datos en entrenamiento y prueba
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

#11.	Crea el modelo de regresión logística
modelo=LogisticRegression()

#12.	Entrena el modelo
modelo.fit(X_train,Y_train)

#13.	Saca el score del modelo
score=modelo.score(X_test,Y_test)
print(score)
#14.	Realiza la predicción de los 10 primeros valores de la variable X_test
pre=modelo.predict(X_test[:10])
print(f"Predicción: {pre}")
#15.	Realiza el reporte del modelo
reporte = classification_report(Y_test, modelo.predict(X_test))

#16.	Saca la matriz de confusión
conf_matrix = confusion_matrix(Y_test, modelo.predict(X_test))
