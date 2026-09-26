somatorio = 0
contador = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        somatorio += c

print('O somatório dos {} números é de {}.'.format(contador, somatorio))