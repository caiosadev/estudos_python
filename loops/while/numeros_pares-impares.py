numero = 1
par = 0
impar = 0

while numero != 0: #enquanto o numero for diferente de zero
    try:
        numero = int(input('Digite um número inteiro (0 para sair): '))
    except ValueError: #tratando erros, caso o usuário entre com uma letra
        print('Digite um número válido!')
        continue
    
    if numero != 0:
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1

print('Você digitou {} número(s) par(es) e {} número(s) ímpar(es).'.format(par, impar))