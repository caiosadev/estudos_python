num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

opcao = 0

maior = 0
menor = 0

while opcao != 5:
    opcao = int(input('[ 1 ] para somar,\n[ 2 ] para multiplicar,\n[ 3 ] para maior'
                  '\n[ 4 ] para novos números e\n[ 5 ] para sair: '))
    
    if opcao == 1:
        resultado = num1 + num2
        print('\nO resultado de {} + {} é {}.'.format(num1, num2, resultado))
    
    else:
        if opcao == 2:
            resultado = num1 * num2
            print('\nO resultado de {} x {} é {}.'.format(num1, num2, resultado))
        
        elif opcao == 3:
            if num1 == num2:
                print('\nOs dois números são iguais.')
                
            else:
                maior = max(num1, num2)
                menor = min(num1, num2)
                print('\nO maior número é {} e o menor número é {}.'.format(maior, menor))
            
        elif opcao == 4:
            num1 = float(input('Digite o primeiro valor: '))
            num2 = float(input('Digite o segundo valor: '))

        elif opcao == 5:
            print('\nVocê saiu do programa.')
        
        else:
            print('\nOpção inválida, tente novamente.')
