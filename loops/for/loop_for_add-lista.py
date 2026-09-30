precos = []

taxa_10 = .1
taxa_15 = .15

total_imposto = 0
total_precos = 0

for add_lista in range (1, 5): #loop para digitar 4 valores, começando pelo 1
#lendo entrada como str para converter depois, assim remove emtradas de vírgula e cifrão
    preco = input(f'Digite o preço do {add_lista}º produto (apenas números): R$ ')
    
#troca vírgula por ponto e remove cifrão caso seja, digitados. Transformando a str em float
    preco = float(preco.replace(',', '.').replace('R$', ''))
    
    precos.append(preco) #adicionando na lista ao final

for preco in precos:
    if preco <= 1000:
        imposto = preco * taxa_10
        tot_preco_imposto = preco + imposto
        print(f'Imposto de 10% sob R$ {preco:.2f} é de R$ {imposto:.2f}, '
              f'total R$ {tot_preco_imposto:.2f}\n')
    else:
        imposto = preco * taxa_15
        tot_preco_imposto = preco + imposto
        print(f'Imposto de 15% sob R$ {preco:.2f} é de R$ {imposto:.2f}, '
              f'total R$ {tot_preco_imposto:.2f}\n')
    
#pega o último valor do imposto total e o preço total, e soma com o novo, no loop for no primeiro if
    total_imposto += imposto #incremento
    total_precos += preco #incremento
    
print('Preços armazenados: ', precos) #exibição da lista

print(f'\nTotal dos produtos: R$ {total_precos:.2f}, total de imposto: R$ {total_imposto:.2f}.')
