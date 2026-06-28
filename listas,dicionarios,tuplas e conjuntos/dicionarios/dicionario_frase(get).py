#conta a quantidade de letras em uma frase (metodo get)

palavra = input("digite uma palavra..: ")
d = {}

for letra in palavra:
    d[letra] = d.get(letra,0) + 1
    # metodo get retorna o primeiro paramentro, 
    # caso o valor associado ja exista no dicionario, 
    # caso contrario, retorna o segundo parametro.
    
print(f"{palavra} ->", end="")
print(d)