distancia = float(input('Qual a distância da viagem (apenas números)? '))

if distancia <= 200:
    curta = distancia * 0.50
    print('Para uma viagem de {}km, a passagem custa: R$ {:.2f}'.format(distancia, curta))
else:
    longa = distancia * 0.45
    print('Para uma viagem de {}km, a passagem custa: R$ {:.2f}.'.format(distancia, longa))