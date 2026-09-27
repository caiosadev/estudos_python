lista = [-10, -8, 0, 1, 2, 5, -2, -4]

maior = lista[0]
menor = lista[0]

for item in lista:
    if item > maior:
        maior = item
    if item < menor:
        menor = item

print('Maior número é: {}.\nMenor número é: {}.'.format(maior, menor))
