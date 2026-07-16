soma = 0
quantidade = 0
while True:
    numero = int(input("digite um número..: "))
    if numero != 0:
        soma = soma + numero
        quantidade = quantidade + 1
    else:
        print(f"a quantidade de números digitados é de..: {quantidade}")
        print(f"a soma dos números digitados é de.......: {soma}")
        print(f"a média dos números digitados é de......: {soma / quantidade:5.1f}")
        break