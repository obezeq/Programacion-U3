#!/usr/bin/env python3

def main():
    cadena = "cadena"

    counter = len(cadena) - 1
    while counter >= 0:
        print(cadena[counter])
        counter -= 1

if __name__ == '__main__':
    main()