arquivo = 'relatorio_vendas_final.xlsx'

extensao = arquivo.split('.')[-1] #encontrou o ponto e entregou o último elemento da lista (extensão), depois do ponto.
print('Extensão: ', extensao)

extensao = arquivo.endswith('.xlsx')
print('É um arquivo Excel? ', extensao)