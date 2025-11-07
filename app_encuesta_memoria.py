import streamlit as st
import matplotlib.pyplot as plt
from funciones import inicializar_votos, registrar_voto_memoria

st.title("📊 Encuesta con Memoria")

# Opciones
opciones = ["Python 🐍", "JavaScript ⚡", "Java ☕", "C++ 💻"]

# Inicializar votos en memoria
votos = inicializar_votos(opciones, st)

# Selección del usuario
eleccion = st.radio("¿Cuál es tu lenguaje favorito?", opciones)

if st.button("Votar"):
    votos = registrar_voto_memoria(eleccion, st)
    st.success(f"¡Gracias por votar por {eleccion}!")

# Mostrar gráfico actualizado
fig, ax = plt.subplots()
ax.bar(votos.keys(), votos.values(), color="orange")
ax.set_ylabel("Votos")
ax.set_title("Resultados de la Encuesta")
st.pyplot(fig)
