#compara os valores de duas listas

lista1 = [1,2,3,4,5]
lista2 = [4,5,6,7,8]

print("listas completas-> ",end="")
print(lista1,end="")
print(lista2)

print("valores comuns entre as duas listas-> ",end="")
print(set(lista1) & set(lista2))

print("valores que so existem na primeira lista-> ",end="")
print(set(lista1) - set(lista2))

print("valores que so existem na segunda lista-> ",end="")
print(set(lista2) - set(lista1))

print("valores não repetidos-> ",end="")
print(set(lista1) ^ set(lista2))