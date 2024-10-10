#!/usr/bin/env python3

v1 = (1,2,3)
v2 = (-1,0,2)

lista_escalar = []

if len(v1) != len(v2):
    print("Los productos escalares no son compatibles.")
else:
    for n in range(len(v1)):
        lista_escalar.append(v1[n] * v2[n])

    producto_escalar = 0
    for n in lista_escalar:
        producto_escalar += n
    
    print(f"El producto escalar de los vectores {v1} y {v2} = {producto_escalar}")