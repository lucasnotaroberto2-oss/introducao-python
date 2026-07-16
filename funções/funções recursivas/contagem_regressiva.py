# retorna uma contagem regressiva do parametro

def contagem_regressiva(i):
    print(i)
    if i <= 1:
        return
    else:
        contagem_regressiva(i - 1)

contagem_regressiva(15)