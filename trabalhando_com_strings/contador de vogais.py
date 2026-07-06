#conta a quantidade de vogais em uma frase

vogais = ['a','e','i','o','u']

frase = input("digite uma frase..: ")

for i in frase.lower():
    if i in vogais:
        print(f"{i}: ",end="")
        print(frase.lower().count(i))
        vogais.remove(i)