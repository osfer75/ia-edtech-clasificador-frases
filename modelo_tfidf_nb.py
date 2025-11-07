import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np

# 1️⃣ Cargar los datos
df = pd.read_csv("frases_ampliadas.csv")
print(f"Total de frases: {len(df)}")
print(df["dificultad"].value_counts(), "\n")

# 2️⃣ Vectorización con TF-IDF
vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1)
X = vectorizer.fit_transform(df["texto"])
y = df["dificultad"]

# 3️⃣ Modelo Naive Bayes
model = MultinomialNB()

# 4️⃣ Validación cruzada (k=5)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')
print(f"Precisión promedio (validación cruzada): {np.mean(scores):.2f} ± {np.std(scores):.2f}")

# 5️⃣ Entrenamiento final
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 6️⃣ Resultados
print("\nEvaluación en conjunto de prueba:")
print("Precisión:", accuracy_score(y_test, y_pred))
print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred))
print("Matriz de confusión:")
print(confusion_matrix(y_test, y_pred))

# 7️⃣ Pruebas con frases nuevas
nuevas = [
    "El alumno resuelve una ecuación de segundo grado",
    "Los niños juegan con sus amigos en el patio",
    "El maestro explica las leyes del movimiento",
    "Sofía canta una canción en clase"
]
X_new = vectorizer.transform(nuevas)
preds = model.predict(X_new)
print("\n--- Predicciones de prueba ---")
for frase, pred in zip(nuevas, preds):
    print(f"'{frase}' → {pred}")

import pickle

# Guardar modelo y vectorizador
with open("modelo_frases.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizador_frases.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("\n✅ Modelo y vectorizador guardados correctamente.")
