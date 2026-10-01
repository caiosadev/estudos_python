dados = ['Ana', 25, 'Luiz', 30, 'Clara', 28]

nomes = dados[::2]
idades = dados[1::2]

print(nomes)
print(idades)

tupla = list(zip(nomes, idades))
print(tupla)

dicionario = dict(zip(nomes, idades))
print(dicionario)