salario = float(input("Qual o seu salário atual? "))
base = salario #definição de uma nova variável pois o salário precisa ficar fixo no print, 
#porém ele muda conforme o cálculo de imposto
imposto = 0 #declaração inicial

#1000 isento
#1000 a 3000 paga 20%
#acima de 3000 paga 35%

if base > 3000:
    imposto = imposto + ((base - 3000) * (35 / 100))
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * (20 / 100))
    base = 1000

print("Salário de: R${:.2f}, imposto à pagar: R${:.2f}" .format(salario, imposto))

#dúvidas, sem entendimento completo no formato do cálculo em si.