# jogo da forca

palavra = list(input("digite a palavra secreta..: ").lower())
palavra_secreta = palavra[:]

for i in range(len(palavra_secreta)):
    palavra_secreta[i] = "_"

vidas = 5
letras_erradas = []

while True:
    
    print(f"vidas restantes..: {vidas}")
    print("palavra..: ",end="")
    
    for i in range(len(palavra_secreta)):
        print(palavra_secreta[i],end="")
    
    print()
    print(f"erros..: {letras_erradas}")
    letra = input("digite uma letra..: ")
    
    if letra in palavra:
        for i in range(len(palavra)):
            if letra == palavra[i]:
                palavra_secreta[i] = letra

    else:
        vidas -= 1
        letras_erradas.append(letra)
        if vidas == 0:
            print("enforcado!")
            break

    if palavra_secreta == palavra:
        print(palavra)
        print("venceu o jogo!")
        break