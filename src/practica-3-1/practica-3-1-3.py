#!/usr/bin/env python3

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

# Asignación de notas a cada asignatura.
for asignatura in asignaturas:
    nota = input(f"¿Qué nota has sacado en {asignatura}? ")

    notas.append((asignatura, int(nota)))

print()
for nota in notas:
    print(f"- En {nota[0]} has sacado {nota[1]}")