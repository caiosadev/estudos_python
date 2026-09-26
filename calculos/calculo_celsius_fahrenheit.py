temp_fah = float(input("Qual a temperatura em Fahrenheit? "))
temp_cel = float(((temp_fah - 32) / 9) * 5)

print("A temperatura em Celsius é: {:.1f} graus." .format(temp_cel))

#convertendo Celsius para Fahrenheit
temp_cel = float(input("Qual a temperatura em Celsius? "))
temp_fah = float(((9 * temp_cel) / 5) + 32)

print("A temperatura em Fahrenheit é {:.1f} graus." .format(temp_fah))