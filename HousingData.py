'''Del archivo de california housing, predice cual será el valor medio 
de una casa en California de acuerdo con: la latutid, la longitud, la edad 
media de la casa, total de cuartos, población y si está cerca del mar'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Importar los datos
df = pd.read_csv("C:/Users/sebas/Inteligencia Artificial/HousingData.csv")

# 2. Revisión de la data
print(df.head())  # a) Primeras 5 filas
print(df.columns)  # b) Nombres de las columnas
print(df.describe())  # c) Información estadística
print(df.dtypes)  # d) Tipo de datos
duplicados = df.duplicated().sum()
print(f"Valores duplicados: {duplicados}")  # e) Verificar duplicados
faltantes = df.isnull().sum()
print(f"Valores faltantes:\n{faltantes}")  # f) Verificar valores faltantes
df = df.dropna()

# 3. Preprocesamiento de datos
# b) Gráfico de correlación
df_corr = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(df_corr, annot=True, cmap="coolwarm")
plt.title("Matriz de Correlación")
plt.show()

# c) Pairplot de las principales variables
sns.pairplot(df, diag_kind='kde')
plt.show()

# 4. Revisar muestra después de la transformación
print(df.sample(5))

# 5. Crear el modelo de regresión
# a) Definir variables X (predictores) y Y (objetivo)
X = df.drop(columns=['MEDV'])
y = df['MEDV']

# b) Separar en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# c) Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# d) Evaluar el modelo
r2 = modelo.score(X_test, y_test)
print(f"R² del modelo: {r2:.4f}")

# e) Predicción con una muestra específica (fila 4 del dataset original)
muestra = X.iloc[[4]]
prediccion = modelo.predict(muestra)
print(f"Predicción para la fila 4: {prediccion[0]:.2f}")

# f) Evaluar métricas del modelo
y_pred = modelo.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
