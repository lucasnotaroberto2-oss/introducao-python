soma = 0
while True:
    codigo = int(input("digite o codigo do produto..: "))
    if codigo != 0:
        if codigo == 1:
            soma += 0.5
            print(soma)
        elif codigo == 2:
            soma += 1
            print(soma)
        elif codigo == 3:
            soma += 4
            print(soma)
        elif codigo == 5:
            soma += 7
            print(soma)
        elif codigo == 9:
            soma += 8
            print(soma)
        else:
            print("codigo invalido")
    else:
        print(f"o total das compras é de..: {soma}")
        break

    