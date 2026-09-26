numero = int(input("Digite um número para ver a tabuada: "))

for c in range(1, 11):
    print("{} * {} = {}" .format(numero, c, numero * c))
