preco_mercadoria = int(input("digite o valor do produto: "))
percentual_de_desconto = int(input("digite o percentual de desconto: "))
valor_desconto = preco_mercadoria * (percentual_de_desconto/100)
preco_a_pagar = preco_mercadoria - valor_desconto
print(f"valor do desconto é: {valor_desconto} reais")
print(f"preço a pagar é de: {preco_a_pagar} reais")
