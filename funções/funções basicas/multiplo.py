# retorna true ou false caso o segundo parametro seja multiplo do primeiro

def multiplo(a,b):
    return a % b == 0

mult = lambda a,b: a % b == 0

print(multiplo(9,3))
print(multiplo(9,4))

print(mult(9,3))
print(mult(9,4))




