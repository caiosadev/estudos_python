usuarios = ['jessica', 'anne', 'luiz', 'caio', 'admin']
novos_usuarios = ['Carlos', 'Andre', 'Anne', 'Jose', 'Amanda']

for novo_usuario in novos_usuarios: #percorre a lista de novos_usuarios
    if novo_usuario.lower() in usuarios: #cada novo usuário em minúsculo percorrendo a lista usuarios
        print('Usuário: {}, precisará informar um novo nome de usuário.'.format(novo_usuario))
    else:
        print('Nome de usuário: {}, disponível.'.format(novo_usuario))