#Utilizar la expresión lambda como elemento de transformación en una comprensión de listas
lista = [(lambda x:x*2)(numero) for numero in range(1,101)]

#Utilización de lambda como filtro
lista_filtrada = filter(lambda x:x%3==0,lista)

#Utilización de lambda como función a enviar a un map
map(lambda x:x-5,lista)