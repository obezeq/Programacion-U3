#!/usr/bin/env python3

lista = []

# Almacenar en la lista números del 1-10
for i in range(10):
    lista.append(i+1)

for n in lista:
    if lista[-1] == n:
        print(n, end=".")
    else:
        print(n, end=", ")