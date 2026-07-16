n = int(input("tabuada de: "))
inicio = int(input("digite o inicio da tabuada: "))
fim = int(input("digite o fim da tabuada: "))
x = inicio
while x <= fim:
    y = n * x
    print(f"{n}x{x}={y}")
    x = x + 1