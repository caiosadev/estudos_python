from math import floor, trunc #floor arredonda para baixo

numero = float(input("Digite um número real: "))
print("Sua parte inteira é: {}" .format(floor (numero)))

#usando trunc
numero = float(input("Digite um número real: "))
print("Sua parte inteira é: {}" .format(trunc (numero)))

#código sem importação da biblioteca
numero = float(input("Digite um número real: "))
print("Sua parte inteira é: {}" .format(int(numero)))