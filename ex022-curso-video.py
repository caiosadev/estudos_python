nome = input("Qual o seu nome completo? ").strip()

maiusculas = nome.upper() #nome em letras maiúsculas
print("Seu nome maiúsculo: {}." .format(maiusculas))
#print("Seu nome maiúsculo: {}.".format(nome.upper())) funciona sem criar variável

minusculas = nome.lower() #nome em letrar minúsculas
print("Seu nome minúsculo: {}." .format(minusculas))


#primeira forma de fazer
qnt_letras = nome.split() #divide o nome em listas sem os espaços
novo_nome = "".join(qnt_letras) #une a lista sem espaços
print("Seu nome completo tem {} letras.".format(len(novo_nome))) #quantidade de caracteres sem os espaços

#segunda forma de fazer
print("Seu nome completo tem {} letras.".format(len(nome) - nome.count(' ')))


#primeira forma de fazer
primeiro_nome = nome.split() #divide o nome em listas sem os espaços
nome_caracteres = len(primeiro_nome[0]) #para contabilizar quantos caracteres tem a primeira lista
print("O seu primeiro nome tem: {} letras." .format(nome_caracteres))

#segunda forma de fazer
print("O seu primeiro nome tem: {} letras.".format(nome.find(' ')))