soma = 0
contador = 0

for c in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        contador += 1
        soma += numero

print('O somatório dos {} pares é: {}.'.format(contador, soma))
