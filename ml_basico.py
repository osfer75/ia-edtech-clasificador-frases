from sklearn.tree import DecisionTreeClassifier

# Datos de entrenamiento
# X son las características (nota promedio y número de ausencias)
# y es la etiqueta (1 = aprueba, 0 = reprueba)
X = [
    [4.5, 2],
    [3.0, 5],
    [2.5, 8],
    [4.8, 1],
    [3.8, 3],
    [2.0, 10],
]
y = [1, 1, 0, 1, 1, 0]

# Crear y entrenar el modelo
modelo = DecisionTreeClassifier()
modelo.fit(X, y)

# Nueva predicción
# Un estudiante con promedio 3.2 y 4 ausencias
nuevo_estudiante = [[3.2, 4]]
resultado = modelo.predict(nuevo_estudiante)

if resultado[0] == 1:
    print("✅ El modelo predice que el estudiante APROBARÁ.")
else:
    print("❌ El modelo predice que el estudiante REPROBARÁ.")
