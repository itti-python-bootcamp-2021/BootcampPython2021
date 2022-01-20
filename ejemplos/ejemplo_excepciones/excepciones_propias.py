def validar_credenciales(usuario, password):
    if (len(usuario)<10):
        raise Exception("La longitud del usuario es menor de 10 caracteres")
    if (password.startswith("A")):
        raise Exception("La contraseña empieza por A")

try:
    validar_credenciales("PEPEPEPEPE","b38478$")
    print("Credenciales válidas")
except Exception as e:
    print(e)
    