import streamlit as st
from funciones import sumar, restar, multiplicar, dividir

st.title("🧮 Calculadora Básica")

# Entradas
a = st.number_input("Número 1", value=0)
b = st.number_input("Número 2", value=0)

# Selección de operación
operacion = st.selectbox("Selecciona una operación", ["Sumar", "Restar", "Multiplicar", "Dividir"])

# Botón calcular
if st.button("Calcular"):
    if operacion == "Sumar":
        st.success(f"Resultado: {sumar(a, b)}")
    elif operacion == "Restar":
        st.success(f"Resultado: {restar(a, b)}")
    elif operacion == "Multiplicar":
        st.success(f"Resultado: {multiplicar(a, b)}")
    elif operacion == "Dividir":
        st.success(f"Resultado: {dividir(a, b)}")
