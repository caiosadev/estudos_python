refeicoes = ('café da manhã', 'almoço', 'sobremesa', 'lanche da tarde', 'jantar')

print('As refeições oferecidas são:')
for refeicao in refeicoes:
    print(refeicao.title())
    

#unica forma de modificar um item em uma tupla, é reescrevendo.
refeicoes = ('desjejum', 'café da manhã', 'almoço', 'lanche', 'jantar')

print('\nAs novas refeições oferecidas são:')
for refeicao in refeicoes:
    print(refeicao.title())