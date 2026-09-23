produto = float(input("Qual o preço do produto? "))
desconto = float(input("Qual o percentual de desconto? "))
calc_desconto = produto * (desconto / 100)
valor_final = produto - calc_desconto

print("Desconto de {:.0f} e o valor a pagar é de: R$ {:.2f}".format(calc_desconto, valor_final))