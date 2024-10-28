#!/usr/bin/env python3

def get_set_frutas(frutas1, frutas2):
    set_frutas1 = set(frutas1)
    set_frutas2 = set(frutas2)

def main():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    set_frutas1 = set(frutas1)
    set_frutas2 = set(frutas2)

    frutas1_list = list(set_frutas1)
    frutas2_list = list(set_frutas2)

    frutas_comunes_list = []
    for f1 in frutas1_list:
        if f1 in frutas2_list:
            frutas1.append(f1)

    frutas_comunes = set(frutas_comunes_list)



    print(frutas1)

if __name__ == '__main__':
    main()