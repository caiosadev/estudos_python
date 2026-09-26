dias = int(input("Insira o número de dias: "))
horas = int(input("Insira o número de horas: "))
minutos = int(input("Insira o número de minutos: "))
segundos = int(input("Insira o número de segundos: "))

conversao_dias = dias * 86440
conversao_horas = horas * 3600
conversao_minutos = minutos * 60
conversao_final = conversao_dias + conversao_horas + conversao_minutos + segundos

print("A conversão resultou em {} segundos." .format(conversao_final))



#Ainda não funciona a parte da conversão por falta do int em input.
dias, horas, minutos, segundos = input("Escreva os dias, horas, minutos e segundos: ").split()

conversao_dias = dias * 86440
conversao_horas = horas * 3600
conversao_minutos = minutos * 60
conversao_final = conversao_dias + conversao_horas + conversao_minutos + segundos

print("Você escreveu:", dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos")
print("A conversão resultou em {} segundos." .format(conversao_final))
