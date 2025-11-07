import streamlit as st
import pandas as pd
import random
import plotly.express as px

# -------------------------------
# CONFIGURACIÓN DE LA APP
# -------------------------------
st.set_page_config(page_title="Portafolio EdTech - Oscar", page_icon="🚀", layout="wide")

st.title("🚀 Portafolio EdTech - Oscar")

# Menú lateral
menu = st.sidebar.radio(
    "Selecciona una sección:",
    ["📚 Explorador de frases", "📊 Análisis de notas"]
)

# -------------------------------
# SECCIÓN 1: EXPLORADOR DE FRASES
# -------------------------------
if menu == "📚 Explorador de frases":
    st.header("📚 Explorador de frases")

    # Cargar dataset frases
    df_frases = pd.read_csv("frases.csv")

    # Diccionario de colores y emojis
    niveles_info = {
        "principiante": {"color": "green", "emoji": "🌱"},
        "básico": {"color": "blue", "emoji": "📘"},
        "intermedio": {"color": "orange", "emoji": "🔥"}
    }

    # Seleccionar nivel
    nivel = st.selectbox("Selecciona el nivel de la frase:", df_frases["nivel"].unique())

    # Filtrar frases por nivel
    frases_filtradas = df_frases[df_frases["nivel"] == nivel]["frase"].tolist()

    # Mostrar todas las frases con color y emoji
    st.subheader(f"{niveles_info[nivel]['emoji']} Frases nivel {nivel}:")
    for frase in frases_filtradas:
        st.markdown(f"<span style='color:{niveles_info[nivel]['color']}'>{frase}</span>", unsafe_allow_html=True)

    # Botón para mostrar frase al azar
    if st.button("🎲 Mostrar frase al azar"):
        if frases_filtradas:
            frase_random = random.choice(frases_filtradas)
            st.success(f"{niveles_info[nivel]['emoji']} {frase_random}")

# -------------------------------
# SECCIÓN 2: ANÁLISIS DE NOTAS
# -------------------------------
elif menu == "📊 Análisis de notas":
    st.header("📊 Análisis de notas de estudiantes")

    # Cargar dataset notas
    df_notas = pd.read_csv("notas.csv")
    df_notas["promedio"] = df_notas[["matemáticas","ciencias","idiomas"]].mean(axis=1)

    # Mostrar tabla
    st.subheader("📋 Datos completos")
    st.dataframe(df_notas)

      # -------------------------------
    # Filtro por estudiante
    # -------------------------------
    st.subheader("🔎 Filtro por estudiante")
    estudiante_sel = st.selectbox("Selecciona un estudiante:", df_notas["estudiante"].unique())

    notas_estudiante = df_notas[df_notas["estudiante"] == estudiante_sel]
    st.write(notas_estudiante)

    fig1 = px.bar(notas_estudiante.melt(id_vars=["estudiante"], value_vars=["matemáticas","ciencias","idiomas"]),
                  x="variable", y="value", color="variable",
                  title=f"Notas de {estudiante_sel}")
    st.plotly_chart(fig1)

    # -------------------------------
    # Filtro por materia
    # -------------------------------
    st.subheader("📊 Filtro por materia")
    materia_sel = st.selectbox("Selecciona una materia:", ["matemáticas","ciencias","idiomas"])
    ranking = df_notas[["estudiante", materia_sel]].sort_values(by=materia_sel, ascending=False)

    st.write(f"Ranking de estudiantes en {materia_sel}:")
    st.dataframe(ranking)

    fig2 = px.bar(ranking, x="estudiante", y=materia_sel, color="estudiante",
                  title=f"Ranking de estudiantes en {materia_sel}")
    st.plotly_chart(fig2)