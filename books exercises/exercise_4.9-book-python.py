valor_casa = float(input("Qual o valor do imóvel? "))
anos = int(input("Quantos anos ficará pagando? "))
salario = float(input("Qual o seu salário? "))

meses = anos * 12
prestacao = valor_casa / meses

if prestacao <= salario * (30 / 100):
    print("A prestação será de R$ {:.2f}" .format(prestacao))
else:
    print("Prestação maior que o recomendado para o seu salário: R$ {:.2f}".format(prestacao))