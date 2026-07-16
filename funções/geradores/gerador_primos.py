# usa geradores para gerar os numeros primos

def numero_primo(fim):
    
    for i in range(2,fim + 1):
        primo = True

        for j in range(2,int(i**0.5) + 1):
            if i % j == 0:
                primo = False
        
        if primo:
            yield i

print(list(numero_primo(50)))
