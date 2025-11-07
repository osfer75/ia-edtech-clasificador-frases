import pandas as pd

# === Datos simulados de desempeño en español ===
data = {
    "Nombre": ["Anna", "Lucas", "Maya", "Carlos", "Elena"],
    "Lectura": [4.3, 3.7, 4.8, 3.9, 4.5],
    "Escritura": [4.0, 3.5, 4.6, 3.6, 4.4],
    "Escucha": [4.5, 3.8, 4.9, 3.7, 4.6],
    "Conversación": [4.2, 3.6, 4.7, 3.8, 4.3]
}

df = pd.DataFrame(data)
print("=== Desempeño de los estudiantes ===")
print(df)
# === Promedios por habilidad ===
print("\n=== Promedio por habilidad lingüística ===")
print(df.mean(numeric_only=True))

# === Promedio individual ===
df["Promedio"] = df[["Lectura", "Escritura", "Escucha", "Conversación"]].mean(axis=1)

# === Mejor y peor habilidad ===
promedios_habilidad = df.mean(numeric_only=True)
mejor = promedios_habilidad.idxmax()
peor = promedios_habilidad.idxmin()

print(f"\n🌟 Mejor habilidad promedio del grupo: {mejor}")
print(f"⚠️  Habilidad con menor desempeño: {peor}")

import matplotlib.pyplot as plt

# === Gráfico comparativo por habilidad ===
promedios_habilidad = df[["Lectura", "Escritura", "Escucha", "Conversación"]].mean()

plt.figure(figsize=(8,5))
promedios_habilidad.plot(kind='bar')

plt.title("Desempeño promedio por habilidad lingüística", fontsize=14)
plt.ylabel("Puntaje promedio (0-5)")
plt.ylim(3, 5)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()
import matplotlib.pyplot as plt

# === Gráfico comparativo por habilidad ===
promedios_habilidad = df[["Lectura", "Escritura", "Escucha", "Conversación"]].mean()

plt.figure(figsize=(8,5))
promedios_habilidad.plot(kind='bar')

plt.title("Desempeño promedio por habilidad lingüística", fontsize=14)
plt.ylabel("Puntaje promedio (0-5)")
plt.ylim(3, 5)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()
