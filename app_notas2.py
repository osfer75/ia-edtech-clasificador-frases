import streamlit as st
from funciones import evaluar_nota

st.title("🎓 Evaluador de Notas")

# Entrada de la nota
nota = st.number_input("Introduce la nota del 0 al 100:", min_value=0, max_value=100, value=70)

# Botón evaluar
if st.button("Evaluar"):
    resultado = evaluar_nota(nota)
    st.success(f"Resultado: {resultado}")
