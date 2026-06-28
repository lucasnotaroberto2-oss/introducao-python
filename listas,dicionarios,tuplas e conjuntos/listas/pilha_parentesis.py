#pilha de parenteses

aberto = 0
fechado = 0
l = []

expressao = input("digite a expressão.: ")

for letra in expressao: #percorre toda a expressão
    #adiciona cada letra da expressão em 1 indice da lista
    l.append(letra)

nova_lista = []

for i in l: 
# o "i" estava em formato de número quando estav no range(len(l)),
# dessa forma ele irá passar por todos os elementos da lista
    if i == "(":
        nova_lista.append(1)
    elif i == ")":
        if len(nova_lista) == 0:
            nova_lista.append(1)
        else:
            nova_lista.pop(0)

if len(nova_lista) == 0:
    print("OK")
else:
    print("ERRO")