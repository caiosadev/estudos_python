ingrediente = ''

while ingrediente != 'sair':
    ingrediente = input('Escreva um ingrediente para a pizza ou [ sair ]: ').strip().lower()
    
    if ingrediente != 'sair':
        print(f'\nIngrediente {ingrediente} adicionado!\n')
    else:
        print('\nPedido finalizado.\n')
        

#usando flags

loop = True

while loop:
    ingrediente = input('Escreva um ingrediente para a pizza ou [ sair ]: ').strip().lower()
    
    if ingrediente == 'sair':
        loop = False
        print('\nPedido finalizado.\n')
    else:
        print(f'\nIngrediente {ingrediente} adicionado!\n')


#usando break

loop = True

while loop:
    ingrediente = input('Escreva um ingrediente para a pizza ou [ sair ]: ').strip().lower()
    
    if ingrediente == 'sair':
        print('\nPedido finalizado.\n')
        break
    else:
        print(f'\nIngrediente {ingrediente} adicionado!\n')