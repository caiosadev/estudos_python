numero = int(input('Quantos números da sequência de Fibonacci você quer mostrar? '))

contador = 0
anterior = 0
atual = 1

while contador < numero:
    if contador < numero - 1:
        print(anterior, end=' ')
    
    else:
        print(anterior)
        
    proximo = anterior + atual
    anterior = atual 
    atual = proximo
    contador += 1