#FICHERO MODIFICADO EN EL ORDENADOR DE FERNANDO

texto1 = "En un lugar de La Mancha"
texto2 = "de cuyo nombre no quiero acordarme"
#Mostrar los dos textos separados por "---" con un único print
#En un lugar de La Mancha---de cuyo nombre no quiero acordarme
print(texto1,texto2,sep="---")
#Mostrar los dos textos en dos líneas distintas con un único print
"""
En un lugar de La Mancha
de cuyo nombre no quiero acordarme
"""
print(texto1,texto2,sep="\n")
#Mostrar los dos textos en una única línea con dos print
"""
En un lugar de La Mancha de cuyo nombre no quiero acordarme
"""
print(texto1,end=" ")
print(texto2)