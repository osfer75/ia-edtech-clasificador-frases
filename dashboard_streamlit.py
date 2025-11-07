import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos iniciales
data = {
    "nombre": ["Ana", "Luis", "Carla", "Pedro", "Sofia"],
    "nota1": [4.0, 3.5, 4.2, 3.0, 4.5],
    "nota2": [3.5, 4.0, 4.5, 2.8, 4.0],
    "nota3": [4.2, 3.8, 4.0, 3.5, 4.8]
}

df = pd.DataFrame(data)

# Funciones
def color_por_promedio(valor):
    if valor >= 4.0:
        return 'green'
    elif valor >= 3.0:
        return 'yellow'
    else:
        return 'red'

def mensaje_pedagogico(valor):
    if valor >= 4.0:
        return "¡Excelente desempeño! Sigue así 💪"
    elif valor >= 3.0:
        return "Buen desempeño, pero hay espacio para mejorar 🙂"
    else:
        return "Necesita reforzar conocimientos 🔴"

# Título
st.title("Mini Dashboard Educativo Interactivo")

# Sliders para cada estudiante
for nombre in df['nombre']:
    df.loc[df['nombre'] == nombre, 'promedio'] = st.slider(
        nombre,
        min_value=0.0,
        max_value=5.0,
        value=df.loc[df['nombre'] == nombre, ['nota1','nota2','nota3']].mean(axis=1).values[0],

        step=0.1
    )

# Promedio general
promedio_grupo = df['promedio'].mean()
st.write(f"**Promedio general del grupo:** {round(promedio_grupo,2)}")

# Gráfico de barras
colores = [color_por_promedio(x) for x in df['promedio']]
fig, ax = plt.subplots(figsize=(8,4))
ax.bar(df['nombre'], df['promedio'], color=colores)
ax.axhline(promedio_grupo, color='red', linestyle='--', label='Promedio grupo')
ax.set_ylabel("Promedio")
ax.set_title("Promedio por estudiante")
ax.legend()
st.pyplot(fig)

# Mensajes pedagógicos
st.write("📚 **Mensajes pedagógicos por estudiante:**")
for nombre, valor in zip(df['nombre'], df['promedio']):
    st.write(f"{nombre}: {mensaje_pedagogico(valor)}")
