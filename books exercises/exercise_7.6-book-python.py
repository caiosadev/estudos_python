entrada1 = 'AATTCGAA'
entrada2 = 'TG'
entrada3 = 'AC'

resultado = ''

for caractere in entrada1:
    if caractere in entrada2:
        indice = entrada2.index(caractere)
        resultado += entrada3[indice]
    else:
        resultado += caractere

print(resultado)
