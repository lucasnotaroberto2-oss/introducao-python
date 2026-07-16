d = int(input("digite a quantidade de dias:"))
h = int(input("digite a quantidade de horas:"))
m = int(input("digite a quantidade de minutos: "))
s = int(input("digite a quantidade de segundos: "))
calculo_segundos = d * 86400 + h * 3600 + m * 60 + s
print(f"seu tempo em segundos é de:{calculo_segundos}segundos")