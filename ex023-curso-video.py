numero = int(input("Digite um número de 0 à 9999: "))

num = str(numero).zfill(4)#zfill completa a string com zeros

unidade = num[3]
dezena = num[2]
centena = num[1]
milhar = num[0]

print("Unidade: {}.\nDezena: {}.\nCentena: {}.\nMilhar: {}." .format(unidade, dezena, centena, milhar))