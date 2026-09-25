num1 = int(input('Escreva o primeiro número inteiro: '))
num2 = int(input('Escreva o segundo número inteiro: '))

if num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
elif num1 < num2:
    print('{} é menor que {}'.format(num1, num2))
else:
    print('Os números são iguais.')