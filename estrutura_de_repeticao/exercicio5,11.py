soma = 0
meses = 1
y = 0
deposito = int(input("digite o valor do depósito inicial..:"))
deposito_mensal = int(input("digite o deposito mensal..:"))
juros = int(input("digite a taxa de juros ao més(%)..:"))
taxa_juros = juros / 100
while meses <= 24:
    y = y + deposito_mensal
    z = deposito + y
    x = z * taxa_juros
    soma = soma + x
    print(f"a soma dos juros do més {meses} é..: {soma:5.2f}")
    meses = meses + 1
print(f"o ganho mensal com juros é de..:{soma:5.2f}")
