"""
Buscar y mostrar los días que comienzan por determinada letra
Si no se encuentra ninguno, avisar
"""
dias = ["Lunes","Martes","miércoles","Jueves","Viernes","Sábado","Domingo"]
letra = input("Introduce la letra de búsqueda:")
letra_mayuscula = letra.upper()
encontrados = False #Bandera o flag
for dia in dias:
    if dia.upper().startswith(letra_mayuscula):
        print(dia)
        encontrado = True
if not encontrado:
    print("No existe ninguna palabra que empiece por la letra indicada")