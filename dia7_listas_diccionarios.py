notas = [3.5, 4.0, 2.8, 5.0, 4.2]
print("nota1", notas[0])
print("nota2",notas[1])
print("nota3",notas[2])
print("nota4",notas[3])
print("nota5",notas[4])
def promedio(notas):
    return sum(notas) / len(notas)

print("El promedio genreal es:", promedio(notas))

contador = 0
for nota in notas:
    if nota > 4.0:
        contador += 1
print("Cantidad de notas mayores a 4.0:", contador)

