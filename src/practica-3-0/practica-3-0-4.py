#!/usr/bin/env python3

def main():
    frutas = "La lista es: banana, pera, manzana, kiwi, banana, pera, banana."
    fruta = "banana"
    n_banana = frutas.count(fruta) # Imprime la cantidad de palabra 'manzana' en la cadena de texto.

    print(f"La cantidad de veces que la fruta '{fruta}' aparece en la lista es: {n_banana}")

if __name__  == '__main__':
    main()