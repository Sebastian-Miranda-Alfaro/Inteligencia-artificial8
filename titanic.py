import pandas as pd

# Cargar los datos
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# Ver las primeras filas
train.head()

# Información general
train.info()

# Estadísticas generales
train.describe()

# Ver valores nulos
train.isnull().sum()

import seaborn as sns
import matplotlib.pyplot as plt

# Relación entre sobrevivientes y sexo
sns.countplot(x="Survived", hue="Sex", data=train)
plt.show()

# Relación entre sobrevivientes y clase del ticket
sns.countplot(x="Survived", hue="Pclass", data=train)
plt.show()

# Llenar valores nulos en "Age" con la media
train["Age"].fillna(train["Age"].median(), inplace=True)
test["Age"].fillna(test["Age"].median(), inplace=True)

# Llenar valores nulos en "Embarked" con el valor más frecuente
train["Embarked"].fillna(train["Embarked"].mode()[0], inplace=True)

# Convertir "Sex" y "Embarked" a variables numéricas
train["Sex"] = train["Sex"].map({"male": 0, "female": 1})
test["Sex"] = test["Sex"].map({"male": 0, "female": 1})

train["Embarked"] = train["Embarked"].map({"S": 0, "C": 1, "Q": 2})
test["Embarked"] = test["Embarked"].map({"S": 0, "C": 1, "Q": 2})

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Seleccionar características
features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
X = train[features]
y = train["Survived"]

# Dividir en datos de entrenamiento y prueba
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
model = DecisionTreeClassifier(max_depth=3)
model.fit(X_train, y_train)

# Evaluar el modelo
y_pred = model.predict(X_val)
accuracy = accuracy_score(y_val, y_pred)
print(f"Precisión del modelo: {accuracy:.2f}")

# Predecir en el dataset de prueba
predictions = model.predict(test[features])

# Crear el archivo para Kaggle
output = pd.DataFrame({"PassengerId": test["PassengerId"], "Survived": predictions})
output.to_csv("submission.csv", index=False)

print("Archivo submission.csv guardado. ¡Listo para subir a Kaggle! 🎉")
