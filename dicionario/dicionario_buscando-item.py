livros = {'drácula' : 'stoker',
          'felizes por enquanto' : 'geni núñez',
          'saudade do infinito' : 'gabriel loureiro',
          'a paixão segundo gh' : 'clarice lispector'}

autor_busca = input('Qual autor você busca? ').strip().lower()

for livro, autor in livros.items():
    if autor == autor_busca:
        print('Livro encontrado: {}.'.format(livro.title()))
        break
else:
    print('Nenhum livro desse autor encontrado!')
