idade = int(input("Qual a idade do hóspede? "))

if idade < 0 or idade >= 116:
    input("Idade inválida, tente novamente.")
elif idade <= 13:
    input("Criança.")
elif idade <= 17:
    input("Adolecente.")
elif idade <= 59:
    input("Adulto.")
else:
    input("Idoso.")




#ideia exibindo a idade.
idade = int(input("Qual a idade do hóspede? "))
hospede = idade

if idade < 0 or idade >= 116:
    input("Idade inválida, tente novamente.")
elif idade <= 13:
    input("Seu hóspede têm {} anos e é uma criança." .format(hospede))
elif idade <= 17:
    input("Seu hóspede têm {} anos e é um adolecente." .format(hospede))
elif idade <= 59:
    input("Seu hóspede têm {} anos e é um adulto." .format(hospede))
else:
    input("Seu hóspede têm {} anos e é um idoso." .format(hospede))
