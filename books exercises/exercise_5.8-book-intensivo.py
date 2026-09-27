usuarios = ['jessica', 'anne', 'luiz', 'caio', 'admin']

if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
            print('Olá adminstrador, gostaria de ver um relatório de status?')
        else:
            print('Olá {}, obrigado por fazer login novamente!'.format(usuario.title()))
else:
    print('Usuários não cadastrados!')