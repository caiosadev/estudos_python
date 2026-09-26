lista = [10,20,30,40]
x = 0

#substituindo: while x < 4 (tamanho da lista). Dessa forma posso trocar a lista 
#sem preocupar de trocar o tamanho dela no loop.
while x < len(lista): 
    print(lista[x])
    x += 1