# ordenação de lista pelo metodo bolhas (bubble sort)

quantidade = int(input("digite a quantidade de elementos da lista.: "))

l = []

for i in range(quantidade):
    numero = int(input("digite um número para adicionar na lista.: "))
    l.append(numero)

print("lista completa: ")
print(l)

print("lista ordenada: ")

for i in range(quantidade):
    for i in range(1,quantidade):
        if l[i - 1] > l[i]:
            temp = l[i - 1] #guarda o valor em uma variavel temporaria
            l[i - 1] = l[i] #troca os valores
            l[i] = temp #retorna o valor que foi guardado

print(l)