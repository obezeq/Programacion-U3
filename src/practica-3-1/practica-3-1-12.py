#!/usr/bin/env python3

A = (1, 2, 3, 4, 5, 6)
B = (-1, 0, 0, 1, 1, 1)

AB = (0, 0, 0, 0, 0, 0)
for i in A:
    for j in B:
        print(f"{i} * {j}")

print(AB)