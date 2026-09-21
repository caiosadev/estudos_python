nome_completo = input("Qual o seu nome completo? ").strip().title()

partes_do_nome = nome_completo.split() #divide o nome em uma lista
nome = partes_do_nome[0]
sobrenome = partes_do_nome[-1] #pega o último item da lista (índices negativos contam a partir do fim da lista)

print("Primeiro nome: {}.".format(nome))
print("Último nome: {}.".format(sobrenome))
