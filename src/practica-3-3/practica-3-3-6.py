#!/usr/bin/env python3

import string

def main():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    alphabet = set(string.ascii_lowercase)
    
    consonantes = alphabet - vocales
    letras_comunes = alphabet & vocales
    
    print("─────────────────────────────────")
    print("Consonantes:")
    print(f"► {', '.join(map(str, consonantes))}.")
    print("─────────────────────────────────")
    print("Letras comunes:")
    print(f"► {', '.join(map(str, letras_comunes))}.")
    print("─────────────────────────────────")

if __name__ == '__main__':
    main()