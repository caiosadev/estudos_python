numero = int(input('Escreva o primeiro termo da PA: '))
razao = int(input('Escreva a razão (quanto quer pular): '))

contador = 0

while contador < 10:
    print(numero, end=' ')
    numero += razao
    contador += 1
