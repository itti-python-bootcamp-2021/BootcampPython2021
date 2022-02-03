from re import S


def duplicar(numero):
    return numero*2

lista = (1,2,4,5)

mapa = map(duplicar, lista)
tupla = tuple(mapa)
print(tupla)

