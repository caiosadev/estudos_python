bikes = ["trek", "cannondale", "redline", "specialized", "caloi"]
x = 0

print("As bikes são: " + str(bikes)) 
#chamando a função str() para transformar a lista em string, assim podemos imprimir a lista inteira.

while True:
    escolha = int(input("De 1 a 5, qual das bikes você quer escolher? (Digite 0 para finalizar) "))
    if escolha == 0:
        break
    print("Gostaria de ter uma bike da " + bikes[escolha-1]) #contanto do índice 1 ao invés de 0.