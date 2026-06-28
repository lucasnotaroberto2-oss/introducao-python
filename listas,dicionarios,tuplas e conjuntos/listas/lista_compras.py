# simula uma lista de compras

compras = []

while True:
    produto = input("digite um produto para adicionar a lista..: ")
    if produto == "fim":
        break
    quantidade = int(input("digite a quantidade do produto............: "))
    preco = float(input("digite o preço do produto.................: "))
    compras.append([produto,quantidade,preco])

print("---------------x---------------")

for i in compras:
    print(f"nome           --> {i[0]}")
    print(f"quantidade     --> {i[1]}")
    print(f"preço(unidade) --> {i[2]}")
    print("---------------x---------------")

soma = 0
for i in compras:
    soma += i[1] * i[2]

print(f"total --> {soma}")