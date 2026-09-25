print('\33[4;36;43mOlá mundo!\33[m')

print('-' * 20)


nome = input('Digite o seu nome: ')

cores = {'semformatacao' : '\033[m', #cores em dicionário
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretobranco' : '\033[7;30m'}

print('Olá, muito prazer {}{}{}.'.format(cores['amarelo'], nome, cores['semformatacao']))