#lista sem valores pois o usuário vai digitar as notas para serem armazenadas aqui.
notas = [0,0,0,0,0,0,0] 
soma = 0
x = 0 #iniciando a contagem do índice da lista, sempre em 0.

while x < 7:
    notas[x] = float(input("Nota {}: " .format(x))) #o %d indica em qual índice a contagem está.
    soma += notas[x]
    x += 1 #adiciona +1 na contagem/loop dos índices da lista (para pular de indíce em índice).
    
x = 0 #variável x reiniciada para voltar a contagem da lista, índice 0.

while x < 7:
    print("Nota %d: {:.2f}" .format(x, notas[x]))
    x +=1 #nova repetição com novos valores inseridos na lista pelo usuário.

#exibe a soma dos valores e a divisão pelo número total de índices na lista = média das notas.
print("Média: {:.2f}" .format(soma/x)) 