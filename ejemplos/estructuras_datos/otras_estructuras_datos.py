lista = [] #Modificable
tupla = () #Inmutable

print("***LISTA***")
lista = ["Item 1","Item 2", "Item 3", "Item 2"]
lista.append("Item 4")
print(lista)
print(lista[2])
print(lista[2:])

print("***TUPLA***")
tupla = ("Item 1", "Item 2", "Item 3", "Item 2")
#tupla.append("Item 5") #ERROR-->Las tuplas no se pueden modificar
print(tupla)
print(tupla[2])
print(tupla[2:])

print("***CONJUTO o SET***")
set = {"Item 1", "Item 2", "Item 3", "Item 2"}
set.add("Item 4")
print(set)
#print(set[2])#ERROR --> No tiene orden
#print(set[2:])#ERROR --> No tiene orden

print("***DICCIONARIO o MAPA o ARRAY ASOCIATIVO***")
diccionario = {2:"Item 2",1:"Item 1",3:"Item 3"}
diccionario[4]="Item 4"
print(diccionario)
print(diccionario[2])
#print(diccionario[2:])#ERROR. No es una estructura posicional

info_luis = ("Luis Viadero", 24, "Madrid")
info_juan_luis = ("Juan Luis Roca", 58, "Barcelona")
info_ricardo = ("Ricardo Ruiz", 22, "Madrid")
info_alejandra = ["Alejandra Aceves", 22, "Madrid"]
info_fernando = ("Fernando Paniagua", 50, "Madrid")

diccionario_humanos = {"Luis Viadero":info_luis, "Juan Luis Roca":info_juan_luis, 
    "Ricardo Ruiz":info_ricardo, "Alejandra Aceves":info_alejandra, info_fernando[0]:info_fernando}

diccionario_humanos.get("Alejandra Aceves")[2]="Barcelona"

humano_buscado = input("Introduce el nombre de un humano:")
print(diccionario_humanos.get(humano_buscado))

