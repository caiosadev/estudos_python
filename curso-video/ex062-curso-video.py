numero = int(input('Escreva o primeiro termo da PA: '))
razao = int(input('Escreva a razão (quanto quer pular): '))

contador = 0
termos = 10

while contador < termos:
    print(numero, end=' ')
    numero += razao
    contador += 1

termos_novos = int(input('\n[ 1 ] para mostrar mais termos,\n[ 0 ] para sair: '))

while termos_novos != 0:
    if termos_novos == 1:
        qnt = int(input('Quantos termos a mais você quer mostrar? '))
        termos += qnt
        
        while contador < termos:
            print(numero, end=' ')
            numero += razao
            contador += 1
            
    else:
        print('Opção inválida, tente novamente.')
            
    termos_novos = int(input('\n[ 1 ] para mostrar mais termos,\n[ 0 ] para sair: '))
    
print(f'Finalizamos com {contador} termos.\n')    
print('Você saiu do programa.')
    