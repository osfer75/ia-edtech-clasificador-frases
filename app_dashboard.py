# -----------------------------
# Predicción de desempeño académico con IA (Streamlit)
# -----------------------------
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# -----------------------------
# Configuración de la página
# -----------------------------
st.set_page_config(
    page_title="Mini Dashboard Educativo con IA",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Mini Dashboard Educativo con IA")
st.write("Explora cómo la **participación** y las **tareas entregadas** pueden influir en el **promedio final** de los estudiantes.")

# -----------------------------
# Datos simulados (grupo de ejemplo)
# -----------------------------
participacion = np.array([40, 55, 60, 70, 80, 85, 90, 95, 100])
tareas = np.array([3, 4, 5, 6, 7, 7, 8, 9, 10])
promedio = np.array([2.8, 3.2, 3.5, 3.8, 4.0, 4.1, 4.3, 4.5, 4.8])

# Entrenamos el modelo
X = np.column_stack((participacion, tareas))
modelo = LinearRegression()
modelo.fit(X, promedio)

# -----------------------------
# Controles interactivos
# -----------------------------
st.sidebar.header("Ajusta los valores:")
participacion_usuario = st.sidebar.slider("Participación (%)", 0, 100, 80, 5)
tareas_usuario = st.sidebar.slider("Tareas entregadas", 0, 10, 7, 1)

# -----------------------------
# Predicción
# -----------------------------
prediccion = modelo.predict([[participacion_usuario, tareas_usuario]])[0]
st.metric("🎯 Promedio estimado", f"{prediccion:.2f}")

# -----------------------------
# Gráfico
# -----------------------------
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(promedio, participacion, color="skyblue", label="Estudiantes reales")
ax.scatter(prediccion, participacion_usuario, color="red", s=100, label="Tu predicción")
ax.set_xlabel("Promedio final")
ax.set_ylabel("Participación (%)")
ax.legend()
st.pyplot(fig)

# -----------------------------
# Mensaje educativo
# -----------------------------
st.info(f"Con una participación del **{participacion_usuario}%** y **{tareas_usuario}** tareas, el modelo estima un promedio de **{prediccion:.2f}**.")
