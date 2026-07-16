cigarros_dia = int(input("quantidade de cigarros fumados ao dia: "))
anos_de_fumante = int(input("quantods anos tem fumado: "))
perda_de_vida = anos_de_fumante * 365 * cigarros_dia * 10 / 1440
print(f"voce perdeu{perda_de_vida:5.0f} dias de vida")