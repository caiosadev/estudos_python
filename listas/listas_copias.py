minhas_comidas = ['pizza', 'macarrão', 'sushi']
amigo_comidas = minhas_comidas[:] #copiando a lista completa, do índice zero ao final

minhas_comidas.append('sorvete') #adicionando itens na lista
amigo_comidas.append('falafel')

print('Minhas comidas favoritas são: {}.'.format(minhas_comidas))
print('As comidas favoritas do meu amigo são: {}.'.format(amigo_comidas))

print('\nAs 3 primeiras comidas que gosto são: {}.'.format(minhas_comidas[:3]))
print('As 3 primeiras comidas que meu amigo gosta são: {}'.format(amigo_comidas[:3]))

print('\nAs comidas do meio da primeira lista são: {}.'.format(minhas_comidas[1:3]))
print('As comidas do meio da segunda lista são: {}.'.format(amigo_comidas[1:3]))

print('\nAs 3 últimas comidas que gosto são: {}.'.format(minhas_comidas[1:]))
print('As 3 últimas comidas que meu amigo gosta são: {}.'.format(amigo_comidas[1:]))