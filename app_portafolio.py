import streamlit as st
import pandas as pd
import random

st.title("Portafolio EdTech 🚀")

# Cargar datasets
df_frases = pd.read_csv("frases.csv")
df_vocab = pd.read_csv("vocabulario.csv")
df_ejercicios = pd.read_csv("ejercicios.csv")

# Diccionario de colores y emojis
niveles_info = {
    "principiante": {"color": "green", "emoji": "🌱"},
    "básico": {"color": "blue", "emoji": "📘"},
    "intermedio": {"color": "orange", "emoji": "🔥"}
}

# Selector de dataset
opcion = st.radio("Selecciona el contenido:", ["Frases", "Vocabulario", "Ejercicios"])

if opcion == "Frases":
    nivel = st.selectbox("Selecciona el nivel de la frase:", df_frases["nivel"].unique())
    frases_filtradas = df_frases[df_frases["nivel"] == nivel]["frase"].tolist()
    st.subheader(f"{niveles_info[nivel]['emoji']} Frases nivel {nivel}:")
    for frase in frases_filtradas:
        st.markdown(f"<span style='color:{niveles_info[nivel]['color']}'>{frase}</span>", unsafe_allow_html=True)
    if st.button("🎲 Frase al azar"):
        if frases_filtradas:
            st.success(f"{niveles_info[nivel]['emoji']} {random.choice(frases_filtradas)}")

elif opcion == "Vocabulario":
    nivel = st.selectbox("Selecciona el nivel del vocabulario:", df_vocab["nivel"].unique())
    vocab_filtrado = df_vocab[df_vocab["nivel"] == nivel]
    st.subheader(f"{niveles_info[nivel]['emoji']} Vocabulario nivel {nivel}:")
    for _, row in vocab_filtrado.iterrows():
        st.markdown(f"{row['palabra']} → {row['traduccion']}")

elif opcion == "Ejercicios":
    nivel = st.selectbox("Selecciona el nivel de ejercicios:", df_ejercicios["nivel"].unique())
    ejercicios_filtrados = df_ejercicios[df_ejercicios["nivel"] == nivel]
    st.subheader(f"{niveles_info[nivel]['emoji']} Ejercicios nivel {nivel}:")
    for _, row in ejercicios_filtrados.iterrows():
        st.markdown(f"❓ {row['pregunta']} → {row['respuesta']}")
