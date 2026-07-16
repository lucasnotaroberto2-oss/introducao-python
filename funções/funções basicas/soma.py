# soma os valores de uma lista

def soma_lista(lista):
    total = 0
    for i in lista:
        total += i
    return total

soma = lambda l: sum(l)

lista = [x for x in range(4)]

print(soma_lista(lista))
print(soma(lista))
