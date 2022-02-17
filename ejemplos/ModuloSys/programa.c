#include "stdio.h"
int main(int argc, char const *argv[])
{
    printf("Número de parámetros: %d\n",argc);
    printf("1er parámetro: %s\n",argv[0]);
    printf("Enviando un correo electrónico a %s",argv[1]);
    return 0;
}
