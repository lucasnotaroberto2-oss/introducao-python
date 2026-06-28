#simulação de louça

pratos = 5
louca = list(range(1,pratos + 1))

while True:
    print(louca)
    print(f"existem {len(louca)} pratos na pia")
    print("digite L para lavar um prato")
    print("digite E para adicionar mais um prato")
    print("digite S para sair do programa")
    operacao = input("operação(L , E , S)..: ")

    if operacao == "L":
        if len(louca) > 0:
            lavado = louca.pop(-1) # -1 indica o ultimo elemento da lista
            print(f"prato {lavado} lavado!")
        else:
            print("louça vazia!")
    elif operacao == "E":
        pratos += 1
        louca.append(pratos)
        print("prato adicionado na louça")
    elif operacao == "S":
        break
    else:
        print("operação invalida!")