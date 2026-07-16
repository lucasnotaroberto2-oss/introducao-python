# valida uma variavel do tipo string

def valida_string(string,min,max):
    return min <= len(string) <= max

valida = lambda string,min,max: min <= len(string) <= max

x = "banana"

print(valida_string(x,2,6))