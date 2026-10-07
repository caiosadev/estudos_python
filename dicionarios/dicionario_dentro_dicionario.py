users = {
    'jsilva' : {
        'nome' : 'João',
        'sobrenome' : 'Silva',
        'pais' : 'Brasil',
    },
    'mandrade' : {
      'nome' : 'Marina',
      'sobrenome' : 'Andrade',
      'pais' : 'Argentina',
    },
}

for username, infos in users.items():
    print(f'Usuário: {username}.')
    
    nome_completo = f'{infos['nome']} {infos['sobrenome']}'
    pais = infos['pais']
    
    print(f'Nome Completo: {nome_completo}.')
    print(f'Pais: {pais}.')
    print('')
