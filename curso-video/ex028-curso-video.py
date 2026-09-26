from random import choice

print('Sorteei em um número...')

numero = int(input('Qual número foi sorteado? '))

numeros = [0, 1, 2, 3, 4, 5]
num_escolhido = choice(numeros)

if numeros == 0:
    print('Você acertou, parabéns!')
else:
    print('Você errou! O número sorteado foi: {}.'.format(num_escolhido))
    
    
#segunda forma de fazer
from random import randint
from time import sleep

computador = randint(1, 5)

print('-' * 20)
print('Sorteei um número...')
print('-' * 20)

jogador = int(input('Qual número foi sorteado? '))

print('PROCESSANDO...')
sleep(2)

if jogador == computador:
    print('Você acertou, parabéns!')
else:
    print('Você errou! O número sorteado foi: {}.'.format(computador))