prato = 5

pilha = list(range(1, prato + 1))

while True:
    print(f'Existem {len(pilha)} pratos na pia.')
    print('\nPilha atual: ', pilha)
    
    acao = input('\nEmpilhar, Lavar ou Sair? ').strip().lower()
    
    if acao == 'empilhar':
        prato += 1
        pilha.append(prato)
    
    elif acao == 'lavar':
        if (len(pilha)) > 0:
            lavar = pilha.pop(-1)
            print(f'\nPrato {lavar} lavado!\n')
        else:
            print('\nVocê lavou todos os pratos!')
    
    elif acao == 'sair':
        break
    
    else:
        print('\nOpção inválida, tente novamente.\n')
    