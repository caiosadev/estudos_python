ultimo = 10

fila = list(range(1, ultimo + 1))

while True:
    print(f'Exitem {len(fila)} clientes na fila.\n')
    print('Fila atual: ', fila)
    
    acao = int(input('\n[ 1 ] adicionar um cliente na fila,\n'
                     '[ 2 ] atender o próximo cliente,\n'
                     '[ 3 ] sair do sistema: '))
    
    if acao == 1:
        ultimo += 1
        fila.append(ultimo)
    
    elif acao == 2:
        if (len(fila)) > 0:
            atendido = fila.pop(0)
            print(f'\nCliente {atendido} atendido.\n')
            
    elif acao == 3:
        break
    
    else:
        print('\nOpção inválida, tente novamente!\n')
    