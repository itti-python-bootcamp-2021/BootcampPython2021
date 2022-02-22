def funcion_externa(valor):
    lista = list(range(0,valor))
    def funcion_interna():
        for item in lista:
            print(item)
    return funcion_interna

f = funcion_externa(10)
f()


def generar_funcion_tabla(lista_elementos):
    def show_ficha():
        salida = "<table>"
        for e in lista_elementos:
            salida = f"{salida}<tr><td>{e[0]}</td><td>{e[1]}</td></tr>"
        salida = f"{salida}</table>"
        print(salida)
    return show_ficha

entrada = [(1,10000),(2,5000),(3,8000)]
f = generar_funcion_tabla(entrada)
f()

def ejecutar_funcion_tabla(lista_elementos):
    def show_ficha():
        salida = "<table>"
        for e in lista_elementos:
            salida = f"{salida}<tr><td>{e[0]}</td><td>{e[1]}</td></tr>"
        salida = f"{salida}</table>"
        print(salida)
    show_ficha()

entrada = [(1,10000),(2,5000),(3,8000)]
ejecutar_funcion_tabla(entrada)

def calcula_salario(nombre, salario_bruto, numero_mensualidades, irpf):
    salario_mensual = salario_bruto / numero_mensualidades
    def calcular_salario_mensual_neto():
        return salario_mensual - (salario_mensual * irpf)
    return calcular_salario_mensual_neto

miirpf = calcula_salario("Fernando",12000,12,0.15)
print(miirpf())

def saludar_exterior3(nombre):
    mensaje = "Hola " + nombre
    def saludar_interior3():
        nonlocal mensaje #Sin esta declaración, el mensaje del ámbito externo no se modifica
        mensaje = "Mensaje modificado"
    saludar_interior3()
    print(mensaje)

saludar_exterior3("Fernando")

    






