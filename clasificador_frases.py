import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1️⃣ Cargar los datos
df = pd.read_csv("data/frases.csv")

# 2️⃣ Convertir texto en vectores numéricos
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(df["texto"])
y = df["dificultad"]

# 3️⃣ Dividir en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Crear y entrenar el modelo
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# 5️⃣ Evaluar precisión
y_pred = modelo.predict(X_test)
precision = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {round(precision*100, 2)}%")

# 6️⃣ Probar con una frase nueva
nueva_frase = ["El estudiante realiza un experimento de química"]
nueva_vector = vectorizador.transform(nueva_frase)
prediccion = modelo.predict(nueva_vector)
print(f"La frase '{nueva_frase[0]}' se clasifica como: {prediccion[0]}")
