valor = float(input("Qual o preço do produto? R$ "))
desconto = 5
valor_final = valor - (valor * desconto / 100)

print("O valor com desconto é {:.2f}" .format(valor_final))