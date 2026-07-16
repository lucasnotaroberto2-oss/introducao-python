# retorna uma lista utilizando geradores

def faixa(stop,start = 0,cond = 1): # os parametros das funções podem possuir valores padrões
    for x in range(start,stop + 1,cond):
        yield x
