instalacao = input("Qual o tipo de instalação?"
                   "(R para residências, I para indústrias e C para comércios) ")
consumo_kwh = float(input("Quantos kWh consumidos? "))
preco = 0

if instalacao == "R" and consumo_kwh < 500:
    preco = consumo_kwh * 0.40
elif instalacao == "R" and consumo_kwh > 500:
    preco = consumo_kwh * 0.65
elif instalacao == "I" and consumo_kwh < 5000:
    preco = consumo_kwh * 0.55
elif instalacao == "I" and consumo_kwh > 5000:
    preco = consumo_kwh * 0.60
elif instalacao == "C" and consumo_kwh < 1000:
    preco = consumo_kwh * 0.55
elif instalacao == "C" and consumo_kwh > 1000:
    preco = consumo_kwh * 0.60
else:
    print("Erro, tente novamente")
print("O preço a pagar é: R$ {:.2f}" .format(preco))
