quantidade_km_percorridos = float(input("digite a quantidade de km percorridos pelo carro alugado: "))
quantidade_dias_alugados = int(input("digite a quantidade de dias que o carro foi alugado: "))
preco_a_pagar = (quantidade_km_percorridos * 0.15) + (quantidade_dias_alugados * 60)
print(f"seu preço a pagar é de: {preco_a_pagar} reais")