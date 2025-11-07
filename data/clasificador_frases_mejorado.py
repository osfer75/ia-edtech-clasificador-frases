import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np

# 1) Cargar datos
df = pd.read_csv("frases.csv")  # asegúrate que la columna se llama 'texto' y 'dificultad'
print("Total ejemplos:", len(df))
print(df['dificultad'].value_counts(), "\n")

# 2) Vectorizar con TF-IDF (mejor que Count para muchos casos)
vectorizer = TfidfVectorizer(ngram_range=(1,2), min_df=1)  # unigramas + bigramas
X = vectorizer.fit_transform(df["texto"])
y = df["dificultad"]

# 3) Modelo recomendado inicial: MultinomialNB
model_nb = MultinomialNB()

# 4) Validación cruzada (k-fold stratificado)
cv = StratifiedKFold(n_splits=4, shuffle=True, random_state=42)
scores = cross_val_score(model_nb, X, y, cv=cv, scoring='accuracy')
print(f"Cross-val accuracy (MultinomialNB): {np.mean(scores):.3f} ± {np.std(scores):.3f}")

# 5) Entrenar y evaluar en una partición guardada (para inspección)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

model_nb.fit(X_train, y_train)
y_pred = model_nb.predict(X_test)
print("\nEvaluación en partición test:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 6) Prueba con frase nueva(s)
nuevas = [
    "El estudiante realiza un experimento de química",
    "La niña corre en el parque",
    "Resolví la ecuación de segundo grado"
]
X_new = vectorizer.transform(nuevas)
preds = model_nb.predict(X_new)
for txt, p in zip(nuevas, preds):
    print(f"'{txt}' -> {p}")

# 7) Alternativa: probar LogisticRegression con TF-IDF (por si quieres comparar)
model_lr = LogisticRegression(max_iter=200, solver='liblinear')
scores_lr = cross_val_score(model_lr, X, y, cv=cv, scoring='accuracy')
print(f"\nCross-val accuracy (LogisticRegression): {np.mean(scores_lr):.3f} ± {np.std(scores_lr):.3f}")
