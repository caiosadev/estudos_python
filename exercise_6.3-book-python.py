L1 = [1, 2, 3]
L2 = [3, 4, 5]
L3 = L1 + L2
L4 = []

x = 0

while x < len(L3):
# not in é uma função que verifica se o elemento está na lista, caso não esteja, ele adiciona na lista.
    if L3[x] not in L4: 
        L4.append(L3[x])
    x += 1

x = 0
while x < len(L4):
    print(L4[x])
    x += 1