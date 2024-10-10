#!/usr/bin/env python3

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

# Asignación de notas a cada asignatura.
for asignatura in asignaturas:
    nota = input(f"¿Qué nota has sacado en {asignatura}? ")

    notas.append((asignatura, int(nota)))

print()
for nota in notas:
    if nota[1] < 5:
        print(f"- Tienes que repetir la asignatura de {nota[0]}, porque has sacado un {nota[1]}")
