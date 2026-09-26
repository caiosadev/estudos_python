km_usado = float(input("Informe a kilometragem utilizada: "))
dias_alugado = int(input("Você está há quantos dias com o automóvel? "))
custo_dia = 60
custo_km = 0.15

aluguel_final = custo_km * km_usado + dias_alugado * custo_dia

print("O valor à pagar é: R$ {:.2f}" .format(aluguel_final))