lista = [1, 7, 2, 4]

maior = 0 #maior = lista[0] caso tivesse números negativos na lista
menor = 0

for item in lista:
    if item > maior:
        maior = item
    else:
        menor = item
print('Maior número é: {}.\nMenor número é: {}.'.format(maior, menor))