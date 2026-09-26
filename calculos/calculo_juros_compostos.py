pv = float(input("Qual o valor atual? "))
i = float(input("Qual a taxa de juros? "))
n = int(input("Qual o prazo para pagamento (em meses)? "))

fv = pv * pow((1 + i / 100), n)

print("O valor futuro (FV) é: R$ {:.2f}" .format(fv))
