n1 = float(input("digite um número...:"))
n2 = int(input("digite outro número:"))
operacao = input("qual operação deseja realizar..:")
if n2 != 0 and n1>n2:
    if operacao == ("+"):
        print(n1 + n2)
    elif operacao == ("-"):
        print(n1 - n2)
    elif operacao == ("*"):
        print(n1 * n2)
    elif operacao == ("/"):
        print(n1 / n2)
else:
    print("não pertence aos numeros reais")


