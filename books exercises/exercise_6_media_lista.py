notas = [6,7,5,8,9]
soma = 0
x = 0 #índice 0, início da lista

while x < 5: #são 5 elementos na lista de notas: 0 à 4 (índices).
    soma += notas[x]
    #loop até x, que representa os índices, passar de 5 (x < 5), ou seja, 
    #finalizar a contagem dos itens na lista.
    x += 1 
print("Média: {:.2f}" .format(soma/x))