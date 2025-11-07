import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# --------------------
# Función para calcular promedio
# --------------------
def promedio(lista):
    return sum(lista) / len(lista) if lista else 0

# --------------------
# Lista inicial de estudiantes
# --------------------
if "estudiantes" not in st.session_state:
    st.session_state.estudiantes = [
        {"nombre": "Ana", "notas": [4.0, 4.5, 5.0]},
        {"nombre": "Luis", "notas": [3.0, 3.5, 4.0]},
        {"nombre": "María", "notas": [2.8, 3.2, 3.5]},
        {"nombre": "Carlos", "notas": [4.8, 4.9, 5.0]}
    ]

st.title("🎓 Registro de Estudiantes")

# --------------------
# Agregar nuevo estudiante
# --------------------
st.subheader("Agregar nuevo estudiante")
nombre_nuevo = st.text_input("Nombre del estudiante:")
notas_nuevas = []
num_notas = st.number_input("Cantidad de notas a ingresar", min_value=1, step=1, value=3)

if nombre_nuevo:
    for i in range(1, num_notas + 1):
        nota = st.number_input(f"Nota {i} de {nombre_nuevo}", min_value=0.0, max_value=5.0, step=0.1)
        notas_nuevas.append(nota)
    
    if st.button("Agregar estudiante"):
        st.session_state.estudiantes.append({"nombre": nombre_nuevo, "notas": notas_nuevas})
        st.success(f"Estudiante {nombre_nuevo} agregado correctamente!")

# --------------------
# Agregar notas a estudiante existente
# --------------------
st.subheader("Agregar notas a estudiante existente")
if st.session_state.estudiantes:
    estudiante_seleccionado = st.selectbox(
        "Selecciona el estudiante:",
        [est["nombre"] for est in st.session_state.estudiantes]
    )

    if estudiante_seleccionado:
        num_notas_agregar = st.number_input(
            f"¿Cuántas notas deseas agregar a {estudiante_seleccionado}?",
            min_value=1, step=1, value=1
        )

        nuevas_notas = []
        for i in range(1, num_notas_agregar + 1):
            nota = st.number_input(f"Nota {i} para {estudiante_seleccionado}", min_value=0.0, max_value=5.0, step=0.1)
            nuevas_notas.append(nota)

        if st.button(f"Agregar notas a {estudiante_seleccionado}"):
            for est in st.session_state.estudiantes:
                if est["nombre"] == estudiante_seleccionado:
                    est["notas"].extend(nuevas_notas)
                    st.success(f"Se agregaron {len(nuevas_notas)} notas a {estudiante_seleccionado} correctamente!")
                    break

# --------------------
# Mostrar registro actualizado
# --------------------
st.subheader("Registro de estudiantes")
for est in st.session_state.estudiantes:
    prom = promedio(est["notas"])
    st.write(f"{est['nombre']} → Notas: {est['notas']} | Promedio: {round(prom,2)}")

# --------------------
# Promedio general del grupo
# --------------------
todos_los_promedios = [promedio(est["notas"]) for est in st.session_state.estudiantes]
promedio_grupo = promedio(todos_los_promedios)
st.write(f"**Promedio general del grupo:** {round(promedio_grupo,2)}")

# --------------------
# Gráfico de promedios con colores condicionales
# --------------------
nombres = [est["nombre"] for est in st.session_state.estudiantes]
promedios = [promedio(est["notas"]) for est in st.session_state.estudiantes]

colores = []
for prom in promedios:
    if prom >= 4.0:
        colores.append("green")
    elif prom >= 3.0:
        colores.append("yellow")
    else:
        colores.append("red")

fig, ax = plt.subplots()
ax.bar(nombres, promedios, color=colores)
ax.set_ylim(0, 5)
ax.set_ylabel("Promedio")
ax.set_title("Promedio de cada estudiante (colores según desempeño)")

st.pyplot(fig)
st.markdown("**Leyenda:** 🟢 ≥4.0 | 🟡 3.0–3.99 | 🔴 <3.0")

# --------------------
# Exportar a CSV
# --------------------
st.subheader("Exportar registro a CSV")

df = pd.DataFrame({
    "Nombre": [est["nombre"] for est in st.session_state.estudiantes],
    "Notas": [est["notas"] for est in st.session_state.estudiantes],
    "Promedio": [round(promedio(est["notas"]), 2) for est in st.session_state.estudiantes]
})

csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Descargar CSV",
    data=csv,
    file_name='registro_estudiantes.csv',
    mime='text/csv'
)
