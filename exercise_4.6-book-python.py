viagem = float(input("Qual a distância que gostaria de percorrer? "))

base_viagem = viagem
if base_viagem <= 200:
    print("A passagem é: R$ {:.2f}" .format(viagem * 0.50))
else:
    print("A passagem é: R$ {:.2f}" .format(viagem * 0.45))




#Usando variáveis para os cálculos de acordo com a quilometragem, 
#caso no futuro esses valores mudem, tornando fácil a atualização.
viagem = float(input("Qual a distância que gostaria de percorrer? "))

base_viagem = viagem
viagem_200 = viagem * 0.50
viagem_acima200 = viagem * 0.45

if base_viagem <= 200:
    print("A passagem é: R$ {:.2f}" .format(viagem_200))
else:
    print("A passagem é: R$ {:.2f}" .format(viagem_acima200))

