vendedor = {
    'nome' : 'João',
    'idade' : 25,
    'salario' : 1500,
    'total_vendas' : 15000,
    'tempo_trabalho' : 5,
    'total_receber' : 0,
    'nivel' : 2,
}

bonus_tempo = 0

if vendedor['tempo_trabalho'] >= 5:
    bonus_tempo = .2

elif vendedor['tempo_trabalho'] >= 3 and vendedor['nivel'] > 1:
    bonus_tempo = .1
    
elif vendedor['tempo_trabalho'] >= 5:
    bonus_tempo = .05
    

else:
    print('Nenhuma bonificação de tempo, disponível.')


total_bonus_tempo = vendedor['salario'] * bonus_tempo
total_salario = vendedor['salario'] + total_bonus_tempo
    
print(f'Bônus por tempo: R$ {total_bonus_tempo:.2f}.')



#segunda parte
bonus_vendas = 0

if vendedor['total_vendas'] >= 50000:
    bonus_vendas = .3

elif vendedor['total_vendas'] >= 20000:
    bonus_vendas = .2

elif vendedor['total_vendas'] >= 10000:
    bonus_vendas = .1

else:
    print('Nenhuma bonificação de vendas, disponível.')


total_bonus_vendas = vendedor['salario'] * bonus_vendas
total_salario = vendedor['salario'] + total_bonus_vendas

print(f'Bônus pelas vendas: R$ {total_bonus_vendas:.2f}.')

print(f'Salário final de {vendedor["nome"]}: ' 
      f'R$ {vendedor["salario"] + total_bonus_tempo + total_bonus_vendas:.2f}.')



#atualizando o dicionário
vendedor['salario'] = vendedor['salario'] + total_bonus_tempo + total_bonus_vendas
print(f'\n{vendedor}')
