numeros = [0,0,0,0]
x = 0

while x < 4:
    numeros[x] = int(input("Insira a posição {}: " .format(x+1)))
    x += 1
    
while True: #loop em repetição até o usuário digitar 0 para sair.
    escolha = int(input("Qual das 4 posições você quer mostrar? (Digite 0 para finalizar) "))
    if escolha == 0:
        break
    print("O número escolhido foi: {} " .format(numeros[escolha-1]))