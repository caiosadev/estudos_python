numeros = [7, 9, 10, 12]

busca = int(input('Digite um número que gostaria de buscar: '))

for numero in numeros:
    if numero == busca:
        print('Número {} encontrado!'.format(busca))
        break #necessário para encontrar e parar a busca e não passar para o else fora.
else:
    print('Número {}, não encontrado.'.format(busca))
