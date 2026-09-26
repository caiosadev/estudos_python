#Funciona, porém o usuário entra apenas com o valor de salário.
salario = float(input("Digite o seu salário atual: "))

#aumento = 0.4 #aumento de 40% já em decimal.
#valor_final = (salario + (salario * aumento))

aumento = 40 #aumento de 40%, divisão por 100 abaixo, para conversão em percentual.
valor_final = (salario + (salario * aumento / 100))

print("O seu salário será de R$ {:.2f}" .format(valor_final))



#Erro de formato na última linha por causa do símbolo de %
#salario = float(input("Qual o seu salário atual? "))
#aumento = float(input("Digite o aumento percentual, que gostaria de receber (apenas números): "))
#valor_final = (salario + (salario * aumento / 100))

#print("O seu salário será de R$ %5.2f, com o aumento de %f%" % (valor_final, aumento))



#Funciona
salario = float(input("Qual o seu salário atual (apenas números)? "))
aumento = float(input("Digite o aumento percentual, que gostaria de receber (apenas números): "))
valor_final = (salario + (salario * aumento / 100))

print("O seu salário será de R$ {:.2f}, com o aumento de {:.0f}" .format(valor_final, aumento))