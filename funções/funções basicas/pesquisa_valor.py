# pesquisa um valor em uma lista

def pesquisa(lista,valor):
    for i in range(len(lista)):
        if valor == lista[i]:
            print(f"valor {valor} achado na posição {i + 1}")
            return

l = [x for x in range(10)]

print(l)

pesquisa(l,5)