#fazendo o exercício com loop
numero = int(input("Digite um número para ver a tabuada: "))
tabuada = 1
multiplicacao = numero * tabuada

while tabuada <= 10:
    multiplicacao = numero * tabuada
    print("{} * {} = {}" .format(numero, tabuada, multiplicacao))
    tabuada +=1

print("=" * 30)    

#fazendo o exercício como proposto
numero = int(input("Digite um número para ver a tabuada: "))
print("{} x {} = {}" .format(numero, 1, numero*1))
print("{} x {} = {}" .format(numero, 2, numero*2))
print("{} x {} = {}" .format(numero, 3, numero*3))
print("{} x {} = {}" .format(numero, 4, numero*4))
print("{} x {} = {}" .format(numero, 5, numero*5))
print("{} x {} = {}" .format(numero, 6, numero*6))
print("{} x {} = {}" .format(numero, 7, numero*7))
print("{} x {} = {}" .format(numero, 8, numero*8))
print("{} x {} = {}" .format(numero, 9, numero*9))
print("{} x {} = {}" .format(numero, 10, numero*10))