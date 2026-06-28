# verificar o maior valor da lista

l = [1,2,7,4]
minimo = l[0]

for i in l:
    if i <= minimo:
        minimo = i

print(f"o menor valor é {minimo}")