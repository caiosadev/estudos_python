#calculo da multa a partir de 80km/h
#Excluíndo os 80km iniciais e calculando apenas os km acima, vezes R$ 5,00 por km.

velocidade = int(input("Qual a velocidade do carro? "))

calc_multa = (velocidade - 80) * 5

if velocidade > 80:
    print("Você foi multado em R$ {:.2f}!" .format(calc_multa))
if velocidade < 80:
        print("Você não foi multado, parabéns!")