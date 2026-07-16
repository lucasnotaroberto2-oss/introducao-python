distancia = float(input("digite a distancoa da viagem(km): "))
v_media = float(input("digite a velocidade media esperada da viagem(m/s): "))
tempo_viagem = distancia / (v_media * 3.6)
print(f"o tempo da viagem é de: {tempo_viagem:5.1f} horas")