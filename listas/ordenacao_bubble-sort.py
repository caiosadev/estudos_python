# Lista que será ordenada
lista = [7, 4, 3, 12, 8]

# fim indica até onde a lista será analisada
# no começo, a parte não ordenada tem 5 elementos
fim = 5

# repete enquanto houver pelo menos 2 elementos para comparar
while fim > 1:
    # assume que ainda não houve troca nessa passada
    trocou = False
    x = 0

    # compara cada par de elementos vizinhos
    while x < (fim - 1):
        # se o valor da esquerda for maior que o da direita, troca
        if lista[x] > lista[x + 1]:
            trocou = True  # indica que a lista mudou nesta passada
            temp = lista[x]
            lista[x] = lista[x + 1]
            lista[x + 1] = temp

        # passa para o próximo par
        x += 1

    # se não houve troca, a lista já está ordenada
    if not trocou:
        break

    # reduz o limite porque o maior elemento já foi colocado no final
    fim -= 1

    # mostra a lista após essa passagem
for e in lista:
    print(e)
