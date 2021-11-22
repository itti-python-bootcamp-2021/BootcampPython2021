import datetime
LIMITE = 10000
#Filtrado sin emplear list comprehension
def es_primo(numero):
    if numero==1:
        return False
    for i in range(numero-1,1,-1):
        if (numero%i==0):
            return False
    return True

ini = datetime.datetime.now()
lista = [x for x in range(1,LIMITE) if es_primo(x)]
end = datetime.datetime.now()
delta_time = (end-ini).microseconds
print(delta_time/1000,"milisegundos",lista)

#Filtrado empleando list comprehension
def es_primo_lc(numero):
    if numero==1:
        return False
    divisores = [i for i in range(numero-1,1,-1) if (numero%i==0)]
    return len(divisores)==0

ini = datetime.datetime.now()
lista = [x for x in range(1,LIMITE) if es_primo_lc(x)]
end = datetime.datetime.now()
delta_time = (end-ini).microseconds
print(delta_time/1000,"milisegundos",lista)