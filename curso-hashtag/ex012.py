log = '20230915;1000;Transferência recebida'

data, valor, descricao = log.split(';')

data_formatada = f'{data[-2:]}/{data[4:6]}/{data[:4]}'

print('Data:', data_formatada)
print('Valor: R$ ', valor)
print('Descrição:', descricao.title())