a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

if a > b:
    print("O primeiro valor é maior.")
if b > a:
    print("O segundo valor é maior.")
#se o primeiro valor e o segundo forem iguais, o programa não retorna nenhum print, 
# pois não há if ou else para ele.



a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

if a > b:
    print("O primeiro valor é maior.")
if b > a:
    print("O segundo valor é maior.")
else:
    print("Valores incorretos, tente novamente.")