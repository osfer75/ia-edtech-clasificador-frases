import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar dataset
df = pd.read_csv("notas.csv")

st.title("📊 Análisis de Notas de Estudiantes")

# Mostrar tabla
st.subheader("Datos de estudiantes")
st.dataframe(df)

# Calcular promedio por estudiante
df["promedio"] = df[["matemáticas","ciencias","idiomas"]].mean(axis=1)

# Gráfico interactivo
st.subheader("Promedio por estudiante")
fig = px.bar(df, x="estudiante", y="promedio", color="promedio", title="Promedio de notas")
st.plotly_chart(fig)
