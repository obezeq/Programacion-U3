#!/usr/bin/env python3

def get_numeros_pares(numeros: dict) -> dict:
    numeros_pares = set()
    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares.add(numero)
    
    return numeros_pares
        
def get_multiplos_tres(numeros: dict) -> dict:
    multiplos_tres = set()
    for numero in numeros:
        if numero % 3 == 0:
            multiplos_tres.add(numero)
    
    return multiplos_tres

def get_intersection(numeros1: dict, numeros2: dict) -> dict:
    intersection = numeros1 & numeros2
    return intersection

def print_numeros(numeros: dict):
    for n in numeros:
        print(f"► {n}") 

def main():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    
    numeros_pares = get_numeros_pares(numeros)
    multiplos_tres = get_multiplos_tres(numeros)
    pares_y_multiplos_de_tres = get_intersection(numeros_pares, multiplos_tres)
    print("─────────────────────────────────")
    print("Numeros pares:")
    print_numeros(numeros_pares)
    print("─────────────────────────────────")
    print("Multiplos de tres:")
    print_numeros(multiplos_tres)
    print("─────────────────────────────────")
    print("Intersección de numeros pares y multiplos de tres")
    print_numeros(pares_y_multiplos_de_tres)
    print("─────────────────────────────────")

if __name__ == '__main__':
    main()