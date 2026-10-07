lista = [5, 9, 13]

x = 0 #índice começando da posição 0

#mostra o índice e o valor do elemento da lista
for numero in lista:
    print(x, numero)
    x += 1

print('')

#enumerate() retorna o índice e o valor do elemento da lista
for x, numero in enumerate(lista):
    print(x, numero)

