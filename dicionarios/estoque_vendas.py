estoque = {
    'tomate' : [1000, 2.30],
    'alface' : [500, 0.45],
    'batata' : [2001, 1.20],
    'feijão' : [100, 1.50],
}

vendas = [['tomate', 5], ['batata', 10], ['alface', 5]]

total_vendas = 0

print('Vendas:')
for venda in vendas:
    produto, quantidade = venda
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f'{produto.capitalize()}: {quantidade} x R$ {preco:.2f} = R$ {custo:.2f}')
    estoque[produto][0] -= quantidade
    total_vendas += custo

print(f'Vendas Totais: R$ {total_vendas}.')


print('\nEstoque:')
for chave, valores in estoque.items():
    print('Descrição: ', chave.capitalize())
    print('Quantidade: ', valores[0])
    print(f'Preço: R$ {valores[1]:.2f}')
    print('')
