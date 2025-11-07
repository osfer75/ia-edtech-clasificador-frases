import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Cargar los datos ---
df = pd.read_csv("notas_estudiantes.csv")

# --- Título ---
st.title("📊 Seguimiento de Notas de Estudiantes")
st.write("Visualiza los promedios y resultados de cada estudiante de manera interactiva.")

# --- Mostrar tabla ---
st.subheader("📋 Datos de los estudiantes")
st.dataframe(df)

# --- Seleccionar estudiante ---
estudiante = st.selectbox("Selecciona un estudiante:", df["Nombre"])

# --- Mostrar datos individuales ---
st.subheader(f"🎓 Resultados de {estudiante}")
fila = df[df["Nombre"] == estudiante].iloc[0]
st.write(f"**Español:** {fila['Español']}")
st.write(f"**Inglés:** {fila['Inglés']}")
st.write(f"**Ciencias:** {fila['Ciencias']}")
st.write(f"**Promedio:** {round(fila['Promedio'], 2)}")

# --- Gráfico de promedios ---
st.subheader("📈 Promedios Generales del Grupo")
fig, ax = plt.subplots()
ax.bar(df["Nombre"], df["Promedio"], color="mediumseagreen")
ax.set_xlabel("Estudiante")
ax.set_ylabel("Promedio")
ax.set_ylim(0, 5)
ax.set_title("Promedio de Notas por Estudiante")

st.pyplot(fig)
