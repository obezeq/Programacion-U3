#!/usr/bin/env python3

numeros_ganadores = []
numeros = input("Introduce los números ganadores de la lotería primitiva (separados por comas): ").strip().replace(' ', '').replace('.', '').split(',')

# Guardar lista de números en tipo int.
for n in numeros:
    try:
        numeros_ganadores.append(int(n))
    except ValueError:
        print(f"¡Uno de los números que has introducido no es un número! ('{n}')")

# Ordenar la lista de números de menor a mayor.
numeros_ganadores.sort()

# Imprimit cada número de forma ordenada.
print(f"Tus números de la lotería primitiva de forma ordenada son: ", end="")
for n in numeros_ganadores:
    if numeros_ganadores[-1] == n:
        print(n, end=".")
    else:
        print(n, end=", ")