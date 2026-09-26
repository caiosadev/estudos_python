nomes = ["Lucas", "Maria", "João", "Ana", "Pedro"]
x = 0

while x < len(nomes):
    mensagem = f"Olá, tudo bem {nomes[x].title()}?"
    print(mensagem)
    x += 1