"""
Utilizamos:
os.chdir
os.listdir
os.path.isdir
"""
import os
def evaluar_path(ruta, extension, lista_ficheros):
    try:
        os.chdir(ruta)
    except PermissionError:
        print(f"Permiso denegado para acceder a {ruta}")
    ficheros = os.listdir()
    for fichero in ficheros:
        if os.path.isdir(fichero)==False:
            #Es un fichero
            if (fichero.endswith(extension)):
                lista_ficheros.append(fichero)
        else:
            #Es un directorio
            evaluar_path(fichero, extension, lista_ficheros)
            os.chdir("..")
    print("Salir de la función...")
ruta = input("Introduce el PATH (formato d:/loquesea/):")
extension = input("Introduce la extensión (incluyendo el .):")
lista_ficheros = []
evaluar_path(ruta, extension, lista_ficheros)
print(lista_ficheros)        