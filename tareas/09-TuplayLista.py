# Dada la siguiente tupla,
# crear una lista que sólo incluya los números menor que 5 utilizando 
# un ciclo for: tupla = (13, 1, 8, 3, 2, 5, 8)

tuplas =(13,1,8,3,2,5,8)
lista = []

for tupla in tuplas:
  if tupla < 5:
    lista.append(tupla)
    print(lista)
else: 
  print("Fin del ejercicio")