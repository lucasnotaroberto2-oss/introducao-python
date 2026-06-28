# simulação de pesquisa em lista por indice

l = [15,19,43,95,10,40,0,5]

p = int(input("digite o número da lista a procurar.: "))
v = int(input("digite outro valor a procurar.......: "))

for p1 in range(len(l)):
    if l[p1] == p:
        print(f"{p} achado na posição {p1 + 1}")
        break

for p2 in range(len(l)):
    if l[p2] == v:
        print(f"{v} achado na posição {p2 + 1}")
        break

if p in l or v in l:
    if p1 > p2:
        print(f"o primeiro valor a ser achado foi {v}")
    else:
        print(f"o primeiro valor a ser achado foi {p}")
else:
    print("valor não encontrado!")