while True:
    n = int(input("digite um número..: "))
    soma = 2
    if n == 2:
        print("número primo")
        print("----------x----------")
    elif n != 1 and n != 2 and n % soma != 0:
        soma = 3
        while soma < n:
            if n % soma != 0:
                soma = soma + 2
        if soma == n and soma / n == 1:
            print("número primo")
            print("----------x----------")
    else:
        print("número não primo")
        print("----------x----------")
