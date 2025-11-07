def cuadrado(numero):
    return numero * numero

def presentacion(nombre, edad):
    return f"Hola {nombre}, tienes {edad} años"

def promedio_safe(lista):
    if not lista:
        return None
    return sum(lista) / len(lista)

def es_par(numero):
    return numero % 2 == 0
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b
def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9
def evaluar_nota(nota):
    if nota >= 90:
        return "Excelente 🎉"
    elif nota >= 75:
        return "Muy bien 👍"
    elif nota >= 60:
        return "Aprobado ✅"
    else:
        return "Reprobado ❌"
def registrar_voto(opcion, votos):
    if opcion in votos:
        votos[opcion] += 1
    else:
        votos[opcion] = 1
    return votos
def inicializar_votos(opciones, st):
    if "votos" not in st.session_state:
        st.session_state.votos = {op: 0 for op in opciones}
    return st.session_state.votos

def registrar_voto_memoria(opcion, st):
    if "votos" not in st.session_state:
        st.session_state.votos = {}
    if opcion in st.session_state.votos:
        st.session_state.votos[opcion] += 1
    else:
        st.session_state.votos[opcion] = 1
    return st.session_state.votos
