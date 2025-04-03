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

#fUNCION PREDECIR PRECIOS 
def predecir_precios():
    # Obtener los valores ingresados por el usuario
    CRIM= float(txt1.get())
    ZN= float(txt2.get())
    INDUS = float(txt3.get())
    CHAS = float(txt4.get())
    NOX = float(txt5.get())
    RM=float(txt6.get())
    AGE=float(txt7.get())
    DIS=float(txt8.get())
    RAD=float(txt9.get())
    TAX = float(txt10.get())
    PTRATIO=float(txt11.get())
    B=float(txt12.get())
    LSTAT=float(txt13.get())
    
    #crear arreglo
    arreglo = [[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]]

    # Usar el modelo entrenado para predecir
    prediccion = modelo.predict(arreglo).flatten()[0]
# Mostrar el resultado en la interfaz
    resultado_label.config(text=f"Predicción: ${prediccion:.2f}")
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
#sns.heatmap(df_corr, annot=True, cmap="coolwarm")
plt.title("Matriz de Correlación")
#plt.show()

# c) Pairplot de las principales variables
#sns.pairplot(df, diag_kind='kde')
#plt.show()

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

# e) Predicción con una muestra específica (fila 4 del dataset original)
muestra = X.iloc[[4]]
prediccion = modelo.predict(muestra)

# f) Evaluar métricas del modelo
y_pred = modelo.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

#Diseño de la interfaz
root=tk.Tk()
root.title("Predicción de precios de casas")
#Dimensiones de la ventana
root.geometry('650x500')
#Color de fondo
root.config(bg="#FE4567")
#Etiquetas de entrada
lbl1=tk.Label(root,text="CRIM",bg='#FC9E9B')
lbl1.place(x=100,y=10,width=150,height=30)

lbl2=tk.Label(root,text="ZN",bg='#FC9E9B')
lbl2.place(x=100,y=50,width=150,height=30)

lbl3=tk.Label(root,text="INDUS",bg='#FC9E9B')
lbl3.place(x=100,y=90,width=150,height=30)

lbl4=tk.Label(root,text="CHAS",bg='#FC9E9B')
lbl4.place(x=100,y=130,width=150,height=30)

lbl5=tk.Label(root,text="NOX",bg='#FC9E9B')
lbl5.place(x=100,y=170,width=150,height=30)

lbl6=tk.Label(root,text="RM",bg='#FC9E9B')
lbl6.place(x=100,y=210,width=150,height=30)

lbl7=tk.Label(root,text="AGE",bg='#FC9E9B')
lbl7.place(x=100,y=250,width=150,height=30)

lbl8=tk.Label(root,text="DIS",bg='#FC9E9B')
lbl8.place(x=100,y=290,width=150,height=30)

lbl9=tk.Label(root,text="RAD",bg='#FC9E9B')
lbl9.place(x=100,y=330,width=150,height=30)

lbl10=tk.Label(root,text="TAX",bg='#FC9E9B')
lbl10.place(x=100,y=370,width=150,height=30)

lbl11=tk.Label(root,text="PTRATIO",bg='#FC9E9B')
lbl11.place(x=100,y=410,width=150,height=30)

lbl12=tk.Label(root,text="B",bg='#FC9E9B')
lbl12.place(x=100,y=450,width=150,height=30)

lbl13=tk.Label(root,text="LSTAT",bg='#FC9E9B')
lbl13.place(x=100,y=490,width=150,height=30)

#Caja de texto
txt1=tk.Entry(root)
txt1.place(x=280,y=10,width=150,height=30)

txt2=tk.Entry(root)
txt2.place(x=280,y=50,width=150,height=30)

txt3=tk.Entry(root)
txt3.place(x=280,y=90,width=150,height=30)

txt4=tk.Entry(root)
txt4.place(x=280,y=130,width=150,height=30)

txt5=tk.Entry(root)
txt5.place(x=280,y=170,width=150,height=30)

txt6=tk.Entry(root)
txt6.place(x=280,y=210,width=150,height=30)

txt7=tk.Entry(root)
txt7.place(x=280,y=250,width=150,height=30)

txt8=tk.Entry(root)
txt8.place(x=280,y=290,width=150,height=30)

txt9=tk.Entry(root)
txt9.place(x=280,y=330,width=150,height=30)

txt10=tk.Entry(root)
txt10.place(x=280,y=370,width=150,height=30)

txt11=tk.Entry(root)
txt11.place(x=280,y=410,width=150,height=30)

txt12=tk.Entry(root)
txt12.place(x=280,y=450,width=150,height=30)

txt13=tk.Entry(root)
txt13.place(x=280,y=490,width=150,height=30)

resultado_label = tk.Label(root, text="Predicción: $0.00", bg='#FC9E9B', font=("Arial", 12))
resultado_label.place(x=150, y=620, width=300, height=30)

# Botón para realizar la predicción
button = tk.Button(root, text="Predecir", command=predecir_precios)
button.place(x=150, y=570, width=150, height=30)

#Ejecutar el bucle principal de la aplicación
root.mainloop()