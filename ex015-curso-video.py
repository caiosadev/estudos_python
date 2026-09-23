km = float(input("Quantos km foram rodados? "))
dias = int(input("Quantos dias foram alugados? "))

preco_carro = 60 * dias
preco_km = 0.15 * dias
valor_final = preco_carro + preco_km

print("Você alugou o carro por {} dias, o valor a pagar é de R$ {:.2f}".format(dias, valor_final))
