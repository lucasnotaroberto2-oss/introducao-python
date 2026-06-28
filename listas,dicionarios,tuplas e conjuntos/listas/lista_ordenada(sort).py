#lista ordenada (metodo sort)

quantidade = int(input("digite a quantidade de elementos da lista.: "))

l = []

for i in range(quantidade):
    numero = int(input("digite um número para adicionar na lista.: "))
    l.append(numero)

print("lista completa: ")
print(l)

print("lista ordenada: ")

l.sort()

print(l)