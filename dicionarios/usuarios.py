usuarios = {
    'ana' : ['admin', 'editor'],
    'bruno' : ['usuario'],
    'anne' : ['editor']
}

print(usuarios)

usuarios['anne'].append('admin') #adicionando uma nova permissão ao usuário.
usuarios['ana'].remove('admin') #removendo uma permissão do usuário.

print(usuarios)
