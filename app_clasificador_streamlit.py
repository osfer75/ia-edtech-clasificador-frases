import streamlit as st
import pickle

# Cargar modelo y vectorizador
modelo = pickle.load(open("modelos/modelo_frases.pkl", "rb"))
vectorizador = pickle.load(open("modelos/vectorizador_frases.pkl", "rb"))

# Función para predecir dificultad
def clasificar_frase(frase):
    X = vectorizador.transform([frase])
    pred = modelo.predict(X)[0]
    return pred

# Interfaz Streamlit
st.title("🎓 Clasificador de Frases Educativas")
st.write("Esta herramienta analiza una frase y predice si es de **nivel fácil o difícil** según su vocabulario y estructura.")

frase_usuario = st.text_area("Escribe una frase educativa:", height=100)

if st.button("Analizar"):
    if frase_usuario.strip():
        resultado = clasificar_frase(frase_usuario)
        if resultado == "facil":
            st.success("🟢 Frase clasificada como: **FÁCIL**. Ideal para niveles iniciales o primaria.")
        else:
            st.warning("🔴 Frase clasificada como: **DIFÍCIL**. Adecuada para niveles avanzados o secundaria.")
    else:
        st.info("Por favor, escribe una frase antes de analizar.")
