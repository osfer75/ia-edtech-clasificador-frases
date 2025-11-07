import pandas as pd

# Datos de ejemplo: estudiantes y notas
data = {
    "Nombre": ["Ana", "Luis", "Sofía", "Carlos", "Marta"],
    "Español": [4.5, 3.8, 4.9, 3.5, 4.2],
    "Inglés": [4.0, 4.2, 4.8, 3.9, 4.3],
    "Ciencias": [3.9, 4.1, 4.7, 3.8, 4.5]
}

# Crear el DataFrame
df = pd.DataFrame(data)

print("=== DataFrame de Notas ===")
print(df)

print("\n=== Promedios por materia ===")
print(df.mean(numeric_only=True))

print("\n=== Nota máxima por materia ===")
print(df.max(numeric_only=True))

print("\n=== Nota mínima por materia ===")
print(df.min(numeric_only=True))

# === Calcular el promedio individual de cada estudiante ===
df["Promedio"] = df[["Español", "Inglés", "Ciencias"]].mean(axis=1)

print("\n=== DataFrame con Promedio ===")
print(df)

# === Exportar el DataFrame a un archivo CSV ===
df.to_csv("notas_estudiantes.csv", index=False, encoding="utf-8")

print("\n✅ Archivo 'notas_estudiantes.csv' creado con éxito.")

import matplotlib.pyplot as plt

# === Crear un gráfico de barras con los promedios ===
plt.figure(figsize=(8, 5))
plt.bar(df["Nombre"], df["Promedio"], color="skyblue")
plt.title("Promedio de Notas por Estudiante")
plt.xlabel("Estudiante")
plt.ylabel("Promedio")
plt.ylim(0, 5)

# Mostrar el gráfico
plt.show()

