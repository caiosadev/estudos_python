#importando biblioteca math para o segundo exemplo
from math import sqrt, ceil #sqrt é raiz quadrada e ceil arredonda pra cima. floor arredonda pra baixo.

numero = int(input("Digite um número inteiro: "))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print("O dobro é {}, o triplo é {} e a raiz quadrada é {:.3f}." .format(dobro, triplo, raiz))

#fazendo com biblioteca
numero = int(input("Digite um número inteiro: "))
raiz = sqrt(numero) #math.sqrt seria usado caso eu importasse a biblioteca completa com import math.

print("A raiz quadrada de {} é {:.3f}." .format(numero, ceil(raiz)))