#retorna as letras comuns as duas strings

string_1 = input("1 string: ")
string_2 = input("2 string: ")

print("resultado: ",end="")

for i in set(string_1) & set(string_2):
    print(i,end="")