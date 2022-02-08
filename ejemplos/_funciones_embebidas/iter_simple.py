baraja = iter([1,3,7,"Sota",6,5,"Caballo","Rey",2,3,5,8])
while (True):
    try:
        input("Pulsa <Enter> para sacar carta:")
        carta_actual = next(baraja)
        print("Carta actual",carta_actual)
    except StopIteration:
        break
print("FIN DE LA EJECUCIÓN")


