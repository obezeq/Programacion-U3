#!/usr/bin/env python3

def cuenta(palabra, letra):

    contador = 0
    for l in palabra:
        if l == letra:
            contador = contador + 1
    
    return contador

def main():
    palabara = input("Introduce una palabra: ")
    letra = input("Introduce una letra: ")
    n_letra = cuenta(palabara, letra)

    print(f"La cantidad de letras '{letra}' en la palabra '{palabara}' son: {n_letra}")

if __name__ == '__main__':
    main()