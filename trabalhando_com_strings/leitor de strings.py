#retorna a ocorrencia da 2 string dentro da primeira

string_1 = input("1 string..: ")
string_2 = input("2 string..: ")

if string_2 in string_1:
    print(f"Resultado: {string_2} encontrado na posição {string_1.find(string_2) + 1} de {string_1}")
else:
    print("string não encontrada!")