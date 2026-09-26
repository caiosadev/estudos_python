def converter_float(str_float): #funcao de conversao para float
    str_float = float(str_float)
    return str_float

try:
    entrada = input("Digite um número: ")
    numero_digitado = converter_float(entrada) #chamada da funcao de conversao
    print(f"Ele virou: {numero_digitado}")

except ValueError:
    print("Entrada inválida.")