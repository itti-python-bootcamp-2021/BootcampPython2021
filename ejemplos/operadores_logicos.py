def es_de_noche():
    print("Evaluando si es de noche...")
    return True

def es_verano():
    print("Evaluando si es verano...")
    return True

if es_de_noche() ^ es_verano():
    print("Me voy al parque")


