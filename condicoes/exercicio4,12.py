quantidade_kwh = int(input("informe a quantidade de kWh consumida: "))
tipo_instalação = input("informe o tipo de instalação(i,c,r): ")

if tipo_instalação == "r" and quantidade_kwh <= 500:
    preco = 0.4 * quantidade_kwh
if quantidade_kwh > 500:
    preco = 0.65 * quantidade_kwh
elif tipo_instalação == "c" and quantidade_kwh <= 1000:
    preco = 0.55 * quantidade_kwh
if quantidade_kwh > 1000:
    preco = 0.6 * quantidade_kwh
elif tipo_instalação == "i" and quantidade_kwh <=5000:
    preco = 0.55 * quantidade_kwh
if quantidade_kwh > 5000:
    preco = 0.6 * quantidade_kwh
else:
    print("tipo de instalação invalida")
print(f"o preço a ser pago é de: R${preco:5.2f}")