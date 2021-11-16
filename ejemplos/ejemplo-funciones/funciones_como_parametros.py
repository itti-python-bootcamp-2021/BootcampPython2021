def facturar():
    print("Facturando...")

def pasar_a_cobro():
    print("Pasar a cobro...")

def cobrar():
    print("Cobrando...")

def contabilizar():
    print("Contabilizando...")

def ejecutar_funcion(lista_funciones):
    for funcion in lista_funciones:
        funcion()

ejecutar_funcion([facturar, pasar_a_cobro, cobrar, contabilizar])