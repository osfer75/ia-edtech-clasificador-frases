import streamlit as st
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Función para calcular predicción
def predecir_aprobacion(promedio, ausencias):
    modelo = DecisionTreeClassifier()
    # Datos de ejemplo (X = [promedio, ausencias], y = etiqueta 1=aprueba,0=reprueba)
    X = [[4.5,2],[3.0,5],[2.5,8],[4.8,10],[3.8,3],[2.0,10]]
    y = [1,1,0,0,1,0]
    modelo.fit(X, y)
    return modelo.predict([[promedio, ausencias]])[0]

# Título
st.title("🎓 Clasificador de Rendimiento Académico")

# Formulario de ingreso de estudiante
st.subheader("Ingresa los datos del estudiante")
nombre = st.text_input("Nombre del estudiante")
promedio = st.number_input("Promedio de notas", min_value=0.0, max_value=5.0, step=0.1)
ausencias = st.number_input("Número de ausencias", min_value=0, step=1)

if st.button("Predecir"):
    if nombre:
        resultado = predecir_aprobacion(promedio, ausencias)
        if resultado == 1:
            st.success(f"✅ {nombre} probablemente APROBARÁ.")
        else:
            st.error(f"❌ {nombre} probablemente REPROBARÁ.")
    else:
        st.warning("Por favor ingresa el nombre del estudiante.")
