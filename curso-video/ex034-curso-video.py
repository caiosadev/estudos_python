salario = float(input('Qual é o seu salário? R$ '))

aumento1 = 10
aumento2 = 15

if salario > 1250:
    novo_salario = ((salario * aumento1) / 100) + salario
    print('O aumento foi de {}%, seu salário será de R$ {}.'.format(aumento1, novo_salario))
else:
    novo_salario = ((salario * aumento2) / 100) + salario
    print('O aumento foi de {}%, seu salário será de R$ {}.'.format(aumento2, novo_salario))