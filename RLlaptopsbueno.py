import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import tkinter as tk
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Importar los datos 
df = pd.read_csv("C:/Users/sebas/Inteligencia artificial/laptop_pricing.csv")

#Mostrar los primeros 10 valores 
df.head(10)
df.info()

#Transformar los datos de la variable manufactura a numericos 
df = pd.get_dummies(df, drop_first=True)

#Descripcion estadistica 
df.describe()

#revisar si hay datos nulos 
df.isnull().sum()

#Revisar correlacion entre las variables con heatmap
plt.figure(figsize=(20,20))
sns.heatmap(df.corr(numeric_only=True),annot=True)

#Crear el modelo
X=df.drop('Price',axis="columns")
y=df['Price']

# Separar los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Seleccionar y entrenar el modelo
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Evaluar el modelo
pred = rf.predict(X_test)
r2 = r2_score(y_test, pred)

# Función corregida para predecir el precio
def predecir_precio():
    try:
        # Obtener los valores ingresados por el usuario
        IntelCorei = float(txt2.get())
        IntelCoreGen = float(txt3.get())
        processingspeedGHz = float(txt4.get())
        Ramgb = float(txt5.get())
        HDDgb = float(txt6.get())
        ScreenSizeinch = float(txt9.get())

        # Crear un DataFrame con todas las características esperadas
        arreglo = pd.DataFrame([[IntelCorei, IntelCoreGen, processingspeedGHz, Ramgb, HDDgb, ScreenSizeinch]],
                                       columns=['IntelCorei', 'IntelCoreGen', 'processingspeedGHz', 'Ramgb', 'HDDgb', 'ScreenSizeinch'])

        # Agregar columnas faltantes con 0
        for col in X_train.columns:
            if col not in arreglo.columns:
                arreglo[col] = 0

        # Asegurar que el orden de las columnas sea el mismo que en X_train
        arreglo = arreglo[X_train.columns]

        # Usar el modelo entrenado para predecir
        prediccion = rf.predict(arreglo)[0]

        # Mostrar el resultado en la interfaz
        resultado_label.config(text=f"Predicción: ${prediccion:.2f}")
    
    except ValueError:
        resultado_label.config(text="Error: Ingresa valores numéricos válidos")

# Diseño de la interfaz
root = tk.Tk()
root.title("Predicción de precios de laptop")
#Dimensiones de la ventana
root.geometry('650x500')
#Color de fondo
root.config(bg="#FE4567")
# Etiquetas de entrada
lbl2 = tk.Label(root, text="IntelCore(i-)", bg='#FC9E9B')
lbl2.place(x=100, y=50, width=150, height=30)

lbl3 = tk.Label(root, text="IntelCoreGen", bg='#FC9E9B')
lbl3.place(x=100, y=90, width=150, height=30)

lbl4 = tk.Label(root, text="Processing speed (GHz)", bg='#FC9E9B')
lbl4.place(x=100, y=130, width=150, height=30)

lbl5 = tk.Label(root, text="Ram (GB)", bg='#FC9E9B')
lbl5.place(x=100, y=170, width=150, height=30)

lbl6 = tk.Label(root, text="HDD (GB)", bg='#FC9E9B')
lbl6.place(x=100, y=210, width=150, height=30)

lbl9 = tk.Label(root, text="ScreenSize (inch)", bg='#FC9E9B')
lbl9.place(x=100, y=250, width=150, height=30)

# Cajas de texto
txt2 = tk.Entry(root)
txt2.place(x=280, y=50, width=150, height=30)

txt3 = tk.Entry(root)
txt3.place(x=280, y=90, width=150, height=30)

txt4 = tk.Entry(root)
txt4.place(x=280, y=130, width=150, height=30)

txt5 = tk.Entry(root)
txt5.place(x=280, y=170, width=150, height=30)

txt6 = tk.Entry(root)
txt6.place(x=280, y=210, width=150, height=30)

txt9 = tk.Entry(root)
txt9.place(x=280, y=250, width=150, height=30)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="Predicción: $0.00", bg='#FC9E9B', font=("Arial", 12))
resultado_label.place(x=150, y=290, width=300, height=30)

# Botón para realizar la predicción
button = tk.Button(root, text="Predecir", command=predecir_precio)
button.place(x=150, y=330, width=150, height=30)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
