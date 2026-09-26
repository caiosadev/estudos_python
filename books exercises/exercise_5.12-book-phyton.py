mes = 1
saldo = 0
total_juros = 0

juros = float(input("Digite a taxa de juros: "))

while mes <= 5:
    deposito = int(input("Digite o depósito do mês {}: " .format(mes)))
    saldo += deposito
    calculo = saldo * (juros / 100)
    saldo += calculo
    total_juros += calculo
    print("Valor no mês {}: R$ {:.2f}" .format(mes, saldo))
    mes += 1
    
print("Valor ganho com juros: R$ {:.2f}" .format(total_juros))

print("Valor total: R$ {:.2f}" .format_map(saldo))