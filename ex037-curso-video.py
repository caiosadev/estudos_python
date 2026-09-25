num = int(input('Digite um número inteiro: '))
conversao = int(input('Escreva "1" para conversão binária, '
                      '"2" para octal e "3" para hexadecimal: '))

if conversao == 1:
    print(bin(num))
elif conversao == 2:
    print(oct(num))
else:
    print(hex(num))