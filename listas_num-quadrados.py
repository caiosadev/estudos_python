numeros_quadrados = []

for num in range(1, 11):
    numeros = num ** 2
    numeros_quadrados.append(numeros)
    
print(numeros_quadrados)


#segunda forma
numeros_quadrados = []

for num in range(1, 11):
    numeros_quadrados.append(num ** 2)
    
print(numeros_quadrados)


#terceira forma = list comprehensions
numeros_quadrados = [numeros ** 2 for numeros in range(1, 11)]
print(numeros_quadrados)
