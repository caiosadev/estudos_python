#Modelo do livro, usando if e else dentro de else
minutos = int(input("Quantos minutos utilizados no mês? "))
if minutos < 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15
print("O seu plano é de R$ {:.2f}" .format(minutos * preco))




#Meu modelo usando elif
minutos = int(input("Quantos minutos utilizados no mês? "))

if minutos < 200:
    plano = minutos * 0.20
elif minutos < 400:
    plano = minutos * 0.18
else:
    plano = minutos * 0.15

print("O valor do seu plano é de R$ {:.2f}" .format(plano))