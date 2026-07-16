#programa de adivinhação de numero aleatorio

import random

def procura_valor():
    numero_aleatorio = random.randint(0,100) #gera um numero aleatorio entre 0 e 100
    while True:
        numero = int(input("digite um número de 0 a 100..: "))
        if numero > numero_aleatorio:
            print("valor muito alto")
        elif numero < numero_aleatorio:
            print("valor muito baixo")
        else:
            print(numero_aleatorio)
            print("acertou")
            return

procura_valor()