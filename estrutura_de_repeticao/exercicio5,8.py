n1 = int(input("digite um número.....: "))
n2 = int(input("digite outro número..: "))
soma = 0
print(n1,"x",n2,"=", end="")
while n1 > 0:
    print(n2, end="")
    if n1 != 1:
        print("+",end="")
    #o comando END indica algo que vai ser escrito no final do comando, caso esteja vazio so organiza o programa em linha;
    else:
        print("=",end="")
    soma = soma + n2
    n1 = n1 - 1
print(soma)

