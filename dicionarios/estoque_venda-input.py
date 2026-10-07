estoque = {
    'tomate': [1000, 2.30],
    'alface': [500, 0.45],
    'batata': [2001, 1.20],
    'feijão': [100, 1.50],
}

produto = input('Qual produto foi vendido? ').strip().lower()
quantidade = int(input(f'Quanto de: {produto}, foram vendidos? (apenas números) '))

if produto not in estoque:
    print('Produto não encontrado no estoque.')
else:
    if quantidade > estoque[produto][0]:
        print(f'Quantidade indisponível. No estoque há apenas {estoque[produto][0]} unidades.')
    else:
        preco = estoque[produto][1]
        custo = preco * quantidade
        estoque[produto][0] -= quantidade

        print('Vendas:')
        print(f'{produto.capitalize()}: {quantidade} x R$ {preco:.2f} = R$ {custo:.2f}')
        print(f'Vendas Totais: R$ {custo:.2f}.')

        print('\nEstoque:')
        for chave, valores in estoque.items():
            print('Descrição: ', chave.capitalize())
            print('Quantidade: ', valores[0])
            print(f'Preço: R$ {valores[1]:.2f}')
            print('')
