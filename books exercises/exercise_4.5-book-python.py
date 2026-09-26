#programa feito com mensagem de erro se for incluído números menores que zero.
idade = int(input("Qual a idade do seu automóvel? "))

if idade < 0:
    print("Idade inválida, tente novamente.")
elif idade <= 3:
    print("Seu automóvel é novo!")
elif idade >= 4:
    print("Seu automóvel é antigo.")