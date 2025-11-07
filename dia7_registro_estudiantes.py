# dia7_registro_estudiantes.py

# Lista de diccionarios: cada estudiante tiene nombre y sus notas
estudiantes = [ { "nombre": "Ana", "notas": [4.0, 4.5, 5.0]},
               {"nombre": "Luis", "notas": [3.0, 3.5, 4.0]},
               {"nombre": "Maria", "notas": [2.8, 3.2, 3.5]},
               {"nombre": "Carlos", "notas": [4.8, 4.9, 5.0]}]

# Funcion para calcular promedio
def promedio(lista):
    return sum(lista) / len(lista)

# mostrar resultados
print("Registro de estudiantes:\n")
for est in estudiantes:
    prom = promedio(est["notas"])
    print(f"{est['nombre']} → Notas: {est['notas']} | Promedio: {round(prom, 2)}")
    # Promedio general del grupo
todos_los_promedios = [promedio(est["notas"]) for est in estudiantes]
promedio_grupo = promedio(todos_los_promedios)
print(f"\nPromedio general del grupo: {round(promedio_grupo, 2)}")

# Agregar un nuevo estudiante
nombre_nuevo = input("\nIngresa el nombre del nuevo estudiante (o deja vacío para saltar): ")

if nombre_nuevo:
    notas_nuevas = []
    for i in range(1, 4):
        nota = float(input(f"Ingresa la nota {i} de {nombre_nuevo}: "))
        notas_nuevas.append(nota)
    
    estudiantes.append({"nombre": nombre_nuevo, "notas": notas_nuevas})
    print(f"\n¡Estudiante {nombre_nuevo} agregado correctamente!")

    # Agregar un nuevo estudiante
nombre_nuevo = input("\nIngresa el nombre del nuevo estudiante (o deja vacío para saltar): ")

if nombre_nuevo:
    notas_nuevas = []
    for i in range(1, 4):
        nota = float(input(f"Ingresa la nota {i} de {nombre_nuevo}: "))
        notas_nuevas.append(nota)
    
    estudiantes.append({"nombre": nombre_nuevo, "notas": notas_nuevas})
    print(f"\n¡Estudiante {nombre_nuevo} agregado correctamente!")
# Mostrar resultados actualizados
print("\nRegistro actualizado de estudiantes:")
for est in estudiantes:
    prom = promedio(est["notas"])
    print(f"{est['nombre']} → Notas: {est['notas']} | Promedio: {round(prom, 2)}")

# Promedio general actualizado
todos_los_promedios = [promedio(est["notas"]) for est in estudiantes]
promedio_grupo = promedio(todos_los_promedios)
print(f"\nPromedio general del grupo: {round(promedio_grupo, 2)}")

