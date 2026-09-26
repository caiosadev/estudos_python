#Forma com if e else
age = int(input("Qual a sua idade? "))
salario = float(input("Informe o seu salário atual: "))
aprovado = age >= 18 and salario >= 1500

if aprovado:
    print(True)
else: 
    print(False)



#Teste com 3 valores e entrada de texto.
age = int(input("Qual a sua idade? "))
salario = float(input("Informe o seu salário atual: "))
imposto = (input("Pagou imposto no último ano? "))
aprovado = age >= 18 and salario >= 1200 and imposto == "Sim" or imposto == "sim"

if aprovado:
    print("Aprovado") 
else: 
    print("Não aprovado")



#Forma sem if e else
age = int(input("Qual a sua idade? "))
salario = float(input("Informe o seu salário atual: "))
aprovado_ou_nao = age >= 18 and salario >= 1500

print(aprovado_ou_nao)