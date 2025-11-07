import streamlit as st
import pandas as pd
import random

# Cargar CSV
df = pd.read_csv("frases.csv")

st.title("Explorador de frases EdTech 🚀")

# Diccionario de colores y emojis por nivel
niveles_info = {
    "principiante": {"color": "green", "emoji": "🌱"},
    "básico": {"color": "blue", "emoji": "📘"},
    "intermedio": {"color": "orange", "emoji": "🔥"}
}

# Seleccionar nivel
nivel = st.selectbox("Selecciona el nivel de la frase:", df["nivel"].unique())

# Filtrar frases por nivel
frases_filtradas = df[df["nivel"] == nivel]["frase"].tolist()
# Mostrar todas las frases con color y emoji
st.subheader(f"{niveles_info[nivel]['emoji']} Frases nivel {nivel}:")
for frase in frases_filtradas:
    st.markdown(f"<span style='color:{niveles_info[nivel]['color']}'>{frase}</span>", unsafe_allow_html=True)

# Botón para mostrar frase al azar
if st.button("🎲 Mostrar frase al azar"):
    if frases_filtradas:
        frase_random = random.choice(frases_filtradas)
        st.success(f"{niveles_info[nivel]['emoji']} {frase_random}")
