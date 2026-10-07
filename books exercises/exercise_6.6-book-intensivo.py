linguagens_favoritas = {
    'ana' : 'python',
    'bruno' : 'java',
    'clara' : 'python',
    'eduardo' : 'c#',
}

novos = ['anne', 'luiz', 'gustavo', 'bruno', 'clara']

for nome in novos:
    if nome not in linguagens_favoritas:
        print(f'{nome.title()}, você precisa participar da pesquisa!')

print('')

for nome in linguagens_favoritas:
    print(f'{nome.title()}, obrigado por responder nossa pesquisa!')
