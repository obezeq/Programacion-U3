#!/usr/bin/env python3

import random

ERRORES = (
    "El producto escalar no es compatible."
)

def mostrar_error(e):
    print(ERRORES[e])

def generar_num_aleatorio(min_valor: int, max_valor: int) -> int:
    """Generar número aleatorio

    Args:
        min_valor (int): Mínimo valor del rango del número
        max_valor (int): Máximo valor del rango del número

    Returns:
        int: Número random entre (min_valor y max_valor)
    """

    num_aleatorio = random.randint(min_valor, max_valor)
                                   
    return num_aleatorio

def generar_vector(total_elementos: int, min_valor: int, max_valor: int) -> tuple:
    """Generar vector

    Args:
        total_elementos (int): Número de elementos total en el vector
        min_valor (int): Mínimo valor del rango para generar el número random para cada valor de la tupla
        max_valor (int): Máximo valor del rango para generar el número random para cada valor de la tupla

    Returns:
        tuple: Vector con número total de elementos y rango de números aleatorios dados
    """
    vector = []

    for _ in range(total_elementos):
        num_aleatorio = generar_num_aleatorio(min_valor, max_valor)
        vector.append(num_aleatorio)

    vector = tuple(vector)

    return vector

def producto_especial(v1: tuple, v2: tuple) -> tuple:
    if len(v1) != len(v2):
        return False
    else:
        especial = []
        for n1 in v1:
            suma = 0
            for n2 in v2:
                suma += (n1 * n2)
            especial.append(suma)

        especial = tuple(especial)
        return especial

def producto_escalar(v1: tuple, v2: tuple) -> int:

    lista_escalar = []

    if len(v1) != len(v2):
        return False
    else:
        for n in range(len(v1)):
            lista_escalar.append(v1[n] * v2[n])

        producto_escalar = 0
        for n in lista_escalar:
            producto_escalar += n
        
        return producto_escalar

def producto_matriz(A: tuple, B: tuple) -> tuple:
    len_A = len(A)
    len_B = len(B)

    len_list_A = len(A[0])
    len_list_B = len(B[0])

    if len_list_A == len_B:
        
        B_formatted = []
        for i in range(len_list_B):

            B_temp = []

            for j in range(len_B):
                B_temp.append(B[j][i])

            B_temp = tuple(B_temp)

            B_formatted.append(B_temp)

        B_formatted = tuple(B_formatted)

    else:
        return False


def mostrar_resultado(v1: tuple, v2: tuple, producto: int, especial: bool):

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    if especial:
        print(f"prod_especial = {producto}")
    else:
        print(f"prod = {producto}")

def main():

    especial = False
    v1 = generar_vector(4, -5, 5)
    v2 = generar_vector(4, -5, 5)

    #producto = producto_escalar(v1, v2)
    producto = producto_especial(v1, v2)
    especial = True

    if producto:
        mostrar_resultado(v1, v2, producto, especial)
    else:
        mostrar_error(0)

    print("--------------------------------------")

    A = (
        (1, 2, 3),
        (4, 5, 6)
    )

    B = (
        (-1, 1),
        (0, 2),
        (2, 3)
    )

    producto = producto_matriz(A, B)

    if producto:
        print()
    else:
        print("No se pueden multiplicar ambas matrices")

if __name__ == '__main__':
    main()