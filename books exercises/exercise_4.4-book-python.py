salario = float(input("Qual o seu salário atual? "))

base_salario = salario

if base_salario > 1250:
    base_salario = base_salario * (10 / 100)
else:
    base_salario = base_salario * (15 /100)

print("Para o salário de R$ {:.2f}" .format(salario))
print("O aumento é de: R$ {:.2f}" .format(base_salario))