#testando métodos
entrada = input("Digite algo: ")
print("O tipo primitivo é: ", type(entrada))

print("O que foi digitado são espaços? ", entrada.isspace())
print("É um número ou pode ser convertido? ", entrada.isnumeric())
print("É um número decimal ou pode ser convertido? ", entrada.isdecimal())
print("É alfabético? ", entrada.isalpha())
print("É alfanumérico? ", entrada.isalnum())
print("Está em letras maíusculas? ", entrada.isupper())
print("Está em letras minúsculas? ", entrada.islower())
print("Está capitalizada? ", entrada.istitle())