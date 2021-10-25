expresion = "(5+2*(8/2)+1)*5"
resultado_esperado = int((5+2*(8/2)+1)*5)
resultado = int(input("Introduce el resultado (entero) de la expresion "+expresion+":"))
if resultado==resultado_esperado:
    print("CORRECTO")
else:
    print("ERROR. El resultado esperado era:"+str(resultado_esperado))