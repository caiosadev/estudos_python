def calc_aumento(salario, aumento):
    salario = float(salario)
    aumento = float(aumento)
    valor_final = (salario + (salario * aumento / 100))

    return valor_final


salario = float(input("Qual o seu salário atual (apenas números)? "))
aumento = float(input("Digite o aumento percentual, que gostaria de receber (apenas números): "))
valor_final = calc_aumento(salario, aumento)
print("O seu salário será de R$ {:.2f}, com o aumento de {:.2f}" .format(valor_final, aumento))