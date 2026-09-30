from random import randint
from time import sleep

computador = randint(1, 11)
jogador = 0

print('-' * 40)
print('Sorteei um número...')
print('-' * 40)

while jogador != computador:
    jogador = int(input('Qual número foi sorteado? '))

    print('JOGANDO...')
    sleep(1)
    
    if jogador != computador:
        if jogador < computador:
            print('Mais... Tente novamente!')
        else:
            print('Menos... Tente novamente!')

print('Você acertou depois de {} palpite(s), parabéns!'.format(jogador))
