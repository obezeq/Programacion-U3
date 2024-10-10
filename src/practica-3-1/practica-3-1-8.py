#!/usr/bin/env python3

palabra = input("Introduce una palabra: ")

if palabra.lower() == palabra.lower()[::-1]:
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' NO es un palíndromo.")