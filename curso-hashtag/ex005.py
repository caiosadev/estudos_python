vendas = ['caneta', 'lápis', 'caneta', 'borracha', 'lápis', 'caneta']

canetas = vendas.count('caneta')
lapis = vendas.count('lápis')
borrachas = vendas.count('borracha')

print('Quantidade de canetas vendidas: ', canetas)
print('Quantidade de lápis vendidos: ', lapis)
print('Quantidade de borrachas vendidas: ', borrachas)

vendas_totais = dict(canetas = canetas, lapis = lapis, borrachas = borrachas)
print(vendas_totais)
