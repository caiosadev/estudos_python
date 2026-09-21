nome_completo = input("Qual o seu nome completo? ").strip().title()

partes_do_nome = nome_completo.split()
nome = partes_do_nome[0]
sobrenome = partes_do_nome[-1]

print("Primeiro nome: {}.".format(nome))
print("Último nome: {}.".format(sobrenome))
