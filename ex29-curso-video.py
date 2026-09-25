velocidade = float(input('Qual a velocidade do carro? '))

limite = 80
multa = 7

if velocidade > limite:
    calc_multa = (velocidade - limite) * multa
    print('Você excedeu o limite de velocidade de {}km/h, sua multa é de R$ {:.2f}'
          .format(limite, calc_multa))
else:
    print('Você não excedeu o limite de velocidade de {}km/h, então você não foi multado.'
          .format(limite))