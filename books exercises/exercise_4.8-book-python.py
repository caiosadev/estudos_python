num01 = float(input("Escreva o primeiro número: "))
num02 = float(input("Escreva o segundo número: "))
operacao = (input("Qual a operação desejada? (+, -, * ou /)"))

if operacao == "+":
    print(num01 + num02)
elif operacao == "-":
    print(num01 - num02)
elif operacao == "*":
    print(num01 * num02)
elif operacao == "/":
    print(num01 / num02)
else:
    print("Opção não disponível, tente novamente")
