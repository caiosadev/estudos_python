nome_completo = input("Qual o seu nome completo? ")

primeiro_nome = nome_completo[:5]
ultimo_nome = nome_completo[-8:]

mensagem = "Olá " + primeiro_nome + ultimo_nome

print(mensagem)

# básico, para funcionar com outros nomes, precisa mudar o número entre os colchetes.
# talvez funcionaria com a contagem de caracteres digitados pelo usuário e substituição nos colchetes.