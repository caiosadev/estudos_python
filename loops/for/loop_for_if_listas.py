disponiveis = ['cogumelo', 'azeitona', 'pimentão', 'pepperoni', 'abacaxi', 'queijo']

pedidos = ['cogumelo', 'batata frita', 'queijo']

for pedido in pedidos:
    if pedido in disponiveis:
        print('Ingrediente adicionado: {}.'.format(pedido))
    else:
        print('Ingrediente: {}, não disponível.'.format(pedido))