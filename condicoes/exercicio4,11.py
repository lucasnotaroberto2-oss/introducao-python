valor_casa = float(input("digite o valor da casa a comprar...:"))
salario = float(input("digite seu salarário...:"))
anos_a_pagar = int(input("digite a quantidade de anos a pagar...:"))
prestação_mensal = valor_casa / (anos_a_pagar * 12)
if prestação_mensal <= salario * 0.3:
    print(f"voçe vai pagar uma prestação mensal de: R${prestação_mensal}")
    print(f"durante {anos_a_pagar} anos")
else:
    #------------
    porcentagem_salarial = (prestação_mensal * 100) / salario
    #------------
    if porcentagem_salarial > salario * 0.3 and porcentagem_salarial <= salario * 0.4:
        nova_prestação = prestação_mensal * 0.25
        novos_anos_a_pagar = nova_prestação * (anos_a_pagar * 12)
        print(f"sua prestação mensal é de: R${nova_prestação}")
        print(f"voçe deve pagar por {novos_anos_a_pagar} meses")
    elif porcentagem_salarial > salario * 0.4 and porcentagem_salarial <= salario * 0.5:
        nova_prestação = prestação_mensal * 0.4
        novos_anos_a_pagar = nova_prestação * (anos_a_pagar * 12)
        print(f"sua prestação mensal é de: R${nova_prestação}")
        print(f"voçe deve pagar por {novos_anos_a_pagar} meses")
    elif porcentagem_salarial > salario * 0.5 and porcentagem_salarial <= salario * 0.6:
        nova_prestação = prestação_mensal * 0.5
        novos_anos_a_pagar = nova_prestação * (anos_a_pagar * 12)
        print(f"sua prestação mensal é de: R${nova_prestação}")
        print(f"voçe deve pagar por {novos_anos_a_pagar} meses")
    elif porcentagem_salarial > salario * 0.6 and porcentagem_salarial <= salario * 0.7:
        nova_prestação = prestação_mensal * 0.57
        novos_anos_a_pagar = nova_prestação * (anos_a_pagar * 12)
        print(f"sua prestação mensal é de: R${nova_prestação}")
        print(f"voçe deve pagar por {novos_anos_a_pagar} meses")
    elif porcentagem_salarial > salario * 0.7 and porcentagem_salarial <= salario * 0.8:
        nova_prestação = prestação_mensal * 0.62
        novos_anos_a_pagar = nova_prestação * (anos_a_pagar * 12)
        print(f"sua prestação mensal é de: R${nova_prestação}")
        print(f"voçe deve pagar por {novos_anos_a_pagar} meses")
    elif porcentagem_salarial > salario * 0.8 and porcentagem_salarial <= salario * 0.9:
        nova_prestação = prestação_mensal * 0.66
        novos_anos_a_pagar = nova_prestação * (anos_a_pagar * 12)
        print(f"sua prestação mensal é de: R${nova_prestação}")
        print(f"voçe deve pagar por {novos_anos_a_pagar} meses")
    elif porcentagem_salarial > salario * 0.9 and porcentagem_salarial <= salario * 1:
        nova_prestação = prestação_mensal * 0.7
        novos_anos_a_pagar = nova_prestação * (anos_a_pagar * 12)
        print(f"sua prestação mensal é de: R${nova_prestação}")
        print(f"voçe deve pagar por {novos_anos_a_pagar} meses")

