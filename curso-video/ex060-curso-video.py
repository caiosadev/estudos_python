#usando módulos
from math import factorial

numero = int(input('Digite um número inteiro: '))

fatorial = factorial(numero)

print('O fatorial de {} é {}.'.format(numero, fatorial))


#while
numero = int(input('Digite um número inteiro: '))

fatorial = 1
contador = numero

while contador > 0:
    fatorial *= contador
    contador -= 1
    
print('O fatorial de {} é {}.'.format(numero, fatorial))


#for
numero = int(input('Digite um número inteiro: '))

for fatorial in range(1, numero, -1):
    fatorial *= numero
    numero -= 1

print('O fatorial de {} é {}.'.format(numero, fatorial))