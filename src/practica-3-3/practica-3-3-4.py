#!/usr/bin/env python3

def main():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    set_frutas1 = set(frutas1)
    set_frutas2 = set(frutas2)
    
    frutas_comunes = set_frutas1 & set_frutas2

    frutas_solo_en_frutas1 = set_frutas1 - set_frutas2
    frutas_solo_en_frutas2 = set_frutas2 - set_frutas1

    print("─────────────────────────────────")
    print("Frutas comunes:")
    print(f"► {frutas_comunes}")
    print("─────────────────────────────────")
    print("Frutas solo en frutas1:")
    print(f"► {frutas_solo_en_frutas1}")
    print("─────────────────────────────────")
    print("Frutas solo en frutas2:")
    print(f"► {frutas_solo_en_frutas2}")
    print("─────────────────────────────────")

if __name__ == '__main__':
    main()