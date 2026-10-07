bikes = ["trek", "cannondale", "redline", "specialized", "caloi"]

print("As bikes são: " + str(bikes))

while True:
    escolha = input("Qual bike você quer escolher? (Digite 0 para finalizar) ")
    if escolha == "0":
        break

    if escolha.lower() in bikes:
        print("Gostaria de ter uma bike da " + escolha.lower())
    else:
        print("Erro: essa bike não existe. Tente novamente.")