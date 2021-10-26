edad=12
mensaje="" #Si no se declara 'mensaje' se produce un error al no estar definido en la línea 7
if edad>=18:
    mensaje="Es mayor de edad"
elif edad>=14:
    mensaje="Es adolescente"
print(mensaje)