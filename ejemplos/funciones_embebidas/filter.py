lista = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sábado","Domingo"]

def condicion_empeza_por_m(dia_semana : str):
    return dia_semana.startswith("M")

lista_filtrada = filter(condicion_empeza_por_m, lista)
for dia in lista_filtrada:
    print(dia)