lista = []

for cubos in range(1, 11):
    conta = cubos ** 3
    lista.append(conta)
    
print(lista)


#list comprehensions
lista = [cubos ** 3 for cubos in range(1, 11)]
print(lista)