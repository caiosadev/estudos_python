numeros = []

while True:
    numero = int(input('Digite um número inteiro ou [ 0 ] para parar: '))
    
    if numero == 0:
        break
        
    numeros.append(numero)
    
    continuar = int(input('\n[ 1 ] para digitar mais números ou\n[ 0 ] para parar: '))
    
    if continuar == 0:
        break
    
if numeros:
    media = sum(numeros) / len(numeros)
    print('Foram digitados {} números e a média entre eles é de: {:.1f}.'
          .format(len(numeros), media))
    print('O menor número digitado: {} e o maior número digitado: {}.'
          .format(min(numeros), max(numeros)))
            
else:
    print('Opção inválida, tente novamente.')
