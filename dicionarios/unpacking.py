funcionarios = {
    'primeiro': {
        'nome' : 'João',
        'especialidade' : 'Engenheiro de Software',
    },
    'segundo': {
        'nome' : 'Maria',
        'especialidade' : 'Analista de Dados',
    },
}

while True:
    for key, value in funcionarios.items():
        print('Olá {nome}! Sua especialidade é {especialidade}.'.format(**value))
    break