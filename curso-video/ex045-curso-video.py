from random import randint
from time import sleep

computador = randint(1, 3)

print('-' * 30)
print('Eu já escolhi o meu...')
print('-' * 30)

jogador = int(input('"1" para pedra, \n"2" para papel, \n"3" para tesoura: '))

print('JOGANDO...')
sleep(2)

if jogador == 1 and computador == 3:
    print('Você ganhou, pedra quebra tesoura!')
elif jogador == 3 and computador == 2 :
    print('Você ganhou, tesoura corta papel!')
elif jogador == 2 and computador == 1:
    print('Você ganhou, papel embrulha pedra!')
elif jogador == computador:
    print('Empatamos, jogue novamente!')
else:
    print('Você perdeu! Eu escolhi: {}.'.format(computador))
    