n = 0
soma = 0

while n < 100:
    n = int(input("Escreva um número: "))
    soma += n
    n += 1
    
else: #poderia ser também: if n > 100
    print(soma)