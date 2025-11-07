import streamlit as st
import matplotlib.pyplot as plt
from funciones import registrar_voto

st.title("📊 Encuesta Rápida")

# Opciones
opciones = ["Python 🐍", "JavaScript ⚡", "Java ☕", "C++ 💻"]
votos = {opcion: 0 for opcion in opciones}

# Selección del usuario
eleccion = st.radio("¿Cuál es tu lenguaje favorito?", opciones)

if st.button("Votar"):
    votos = registrar_voto(eleccion, votos)
    st.success(f"¡Gracias por votar por {eleccion}!")

    # Mostrar gráfico
    fig, ax = plt.subplots()
    ax.bar(votos.keys(), votos.values(), color="skyblue")
    ax.set_ylabel("Votos")
    ax.set_title("Resultados de la Encuesta")
    st.pyplot(fig)
