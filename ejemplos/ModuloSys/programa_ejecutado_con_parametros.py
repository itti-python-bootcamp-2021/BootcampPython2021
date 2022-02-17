import sys

print("Número de parámetros:",len(sys.argv))
print("1er parámetro:",sys.argv[0])
email = sys.argv[1]
print("Enviando un correo electrónico a",email)