numero = int(input('Escreva um número inteiro: '))
razao = int(input('Escreva a razão (quanto quer pular): '))

decimo = numero + (10 - 1) * razao

#decimo + razao para mostrar 10 termos
for c in range(numero, decimo + razao, razao):
    print(c, end=' ')