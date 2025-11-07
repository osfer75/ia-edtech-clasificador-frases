import streamlit as st
from funciones import promedio_safe, es_par, cuadrado, presentacion

st.title("Mini App de Funciones en Python")

# Promedio
st.header("Calcular promedio")
nums = st.text_input("Introduce números separados por coma", "3,4,5")
if st.button("Calcular promedio"):
    lista = [int(n) for n in nums.split(",") if n.strip().isdigit()]
    st.write("Promedio:", promedio_safe(lista))

# Número par
st.header("¿Es par?")
num = st.number_input("Introduce un número", value=2)
if st.button("Verificar paridad"):
    st.write(es_par(num))

# Cuadrado
st.header("Cuadrado de un número")
num2 = st.number_input("Introduce un número para el cuadrado", value=3)
if st.button("Calcular cuadrado"):
    st.write(cuadrado(num2))

# Presentación
st.header("Presentación")
nombre = st.text_input("Tu nombre", "Ana")
edad = st.number_input("Tu edad", value=25)
if st.button("Generar presentación"):
    st.write(presentacion(nombre, edad))
