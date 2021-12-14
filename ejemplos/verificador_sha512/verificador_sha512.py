import hashlib
import sys

nombre_programa = sys.argv[0]
fichero_a_validar = sys.argv[1]
fichero_hash = sys.argv[2]

algoritmo = hashlib.sha512()
with open(fichero_a_validar, "rb") as fichero:
    bytes = fichero.read()
    algoritmo.update(bytes)
    resumen = algoritmo.digest().hex()

with open(fichero_hash,"r") as fichero_hash:
    resumen_original = fichero_hash.read()

if (resumen==resumen_original):
    print("El fichero no ha sido manipulado ni modificado")
else:
    print("¡OJO! El fichero ha sido manipulado")