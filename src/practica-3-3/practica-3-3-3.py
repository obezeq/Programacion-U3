#!/usr/bin/env python3

def conjunto_potencia(s):
    subsets = [[]]
    sets = list(s)

    for set in sets:
        subsets += [s + [set] for s in subsets]

    print(subsets)


# Main Function
def main():
     s = {1, 2, 3}
     subsets = conjunto_potencia(s)
     print(subsets)


# Program Starts
if __name__ == '__main__':
    main()

