#include <stdio.h>

int main() {
    char nombre[50];
    printf("¿Cuál es tu nombre? ");
    scanf("%s", nombre);
    printf("Hola %s. Este programa está hecho en el lenguaje de programación: C.\n", nombre);
    return 0;
}

