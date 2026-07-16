#contagem de números primos
n = int(input('digite um número..:'))
quantidade = 0
numero_primo = 2
soma = 0
print(f"os {n} primeiros números primos são..:", end="")
while quantidade <= n:
    if numero_primo == 2:
        print(f"{numero_primo}", end=";")
        numero_primo += 1
        soma += 1
        quantidade += 1
    if numero_primo == 3:
        print(f"{numero_primo}", end=";")
        numero_primo += 1
        soma += 1
        quantidade += 1
    while soma <= n:
        if numero_primo % 2 != 0 and numero_primo % 3 != 0:
            print(f"{numero_primo}", end=";")
            numero_primo += 1
            soma += 1
            quantidade += 1
        else:
            numero_primo += 1
    quantidade += 1
    print(".", end="")