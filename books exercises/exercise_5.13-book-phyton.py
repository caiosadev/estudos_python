divida_inicial = float(input("Digite o valor da dívida: R$ "))
juros = float(input("Digite a taxa de juros mensal (%): "))
valor_mensal = float(input("Digite o valor mensal que será pago: R$ "))

divida = divida_inicial
total_pago = 0
total_juros = 0
mes = 0

# Calcula o juro do primeiro mês
juro_inicial = divida * (juros / 100)

# Verifica se a parcela consegue pagar os juros
if valor_mensal <= juro_inicial:
    print("O valor mensal é insuficiente para quitar a dívida.")

else:

    while divida > 0:

        mes += 1

        # Calcula os juros do mês
        juro = divida * (juros / 100)

        # Acumula o total de juros
        total_juros += juro

        # Adiciona os juros à dívida
        divida += juro

        # Verifica se o pagamento quita a dívida
        if valor_mensal >= divida:

            total_pago += divida
            divida = 0

        else:

            divida -= valor_mensal
            total_pago += valor_mensal

print("Número de meses: {}" .format(mes))
print("Total pago: R$ {:.2f}" .format(total_pago))
print("Total de juros pagos: R$ {:.2f}" .format(total_juros))