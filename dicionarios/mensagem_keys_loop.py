linguagens_favoritas = {
    'ana' : 'python',
    'bruno' : 'java',
    'clara' : 'python',
    'eduardo' : 'c#',
}

amigos = ['bruno', 'eduardo']

for nome in linguagens_favoritas.keys(): #usar keys() é opcional, mas deixa o código mais legível
    print(f'Olá {nome.title()}!')

    if nome in amigos:
        linguagem = linguagens_favoritas[nome].title()
        print(f'\t{nome.title()}, eu também gosto de {linguagem}!')
