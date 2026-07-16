# calculadora usando operator e partial

import operator
from functools import partial

def calcula(operacao, simbolo, operando1, operando2):
    resultado = operacao(float(operando1), float(operando2))
    print(f"{operando1} {simbolo} {operando2} = {resultado}")

operacoes = {
    "+" : partial(calcula, operator.add, "+"),
    "-" : partial(calcula, operator.sub, "-"),
    "*" : partial(calcula, operator.mul, "x"),
    "/" : partial(calcula, operator.truediv, "/")
}

operando1 = input("operador 1..: ")
operando2 = input("operador 2..: ")
operacao = input("operação..: ").strip()

if operacao in operacoes:
    operacoes[operacao](operando1, operando2)
else:
    print("operação invalida!")