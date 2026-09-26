#Forma simplificada
salario = float(input("Qual é o seu salário atual? "))
paga_ounao_imposto = salario >= 1200

print(paga_ounao_imposto)



#Forma com if e else
salario = float(input("Qual é o seu salário atual? "))
imposto = salario >= 1200

if imposto:
   print(True)
else:
    print(False)



#Forma com texto no final
salario = float(input("Qual é o seu salário atual? "))
imposto = salario >= 1200

if imposto:
    print("Você deve pagar o imposto")
else:
    print("Você está insento do imposto")



#Forma de fazer sem informar o salário em números
salario = (input("Seu salário é superior à R$ 1.200,00? "))
imposto = "Sim"

if imposto:
    print("Então você deve pagar o imposto.")
else: 
    print("Você está insento do imposto.")
