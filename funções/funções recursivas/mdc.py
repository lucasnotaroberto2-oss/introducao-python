# calcula o mdc entre dois numeros

def MDC(a, b):
    if b == 0:
        return a
    return MDC(b, a % b)
