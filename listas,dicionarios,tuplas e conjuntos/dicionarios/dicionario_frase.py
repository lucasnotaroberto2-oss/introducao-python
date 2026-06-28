#conta a quantidade de letras em uma frase (dicionario sem valor padrão)

palavra = input("digite uma palavra..: ")
d = {}

for letra in palavra:
    if letra in d:
        d[letra] += 1 # adiciona 1 na quantidade de usos
    else:
        d[letra] = 1 # gera a chave no dicionario, caso a letra não esteja no dicionario
    
print(f"{palavra} ->", end="")
print(d)