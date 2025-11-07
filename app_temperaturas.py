import streamlit as st
from funciones import celsius_a_fahrenheit, fahrenheit_a_celsius

st.title("🌡️ Conversor de Temperaturas")

# Selección de conversión
opcion = st.radio("Elige el tipo de conversión:", ("Celsius → Fahrenheit", "Fahrenheit → Celsius"))

# Entrada
valor = st.number_input("Introduce el valor de la temperatura:", value=0.0)

# Botón convertir
if st.button("Convertir"):
    if opcion == "Celsius → Fahrenheit":
        st.success(f"{valor} °C = {celsius_a_fahrenheit(valor):.2f} °F")
    else:
        st.success(f"{valor} °F = {fahrenheit_a_celsius(valor):.2f} °C")
