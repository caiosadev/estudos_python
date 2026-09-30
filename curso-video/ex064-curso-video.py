numero = 0
contador = 0
soma = 0

while numero != 999:
    numero = int(input('Digite um número ou [ 999 ] para parar: '))
    
    if numero != 999:
        soma += numero
        contador += 1
    
    else:
        print('Foram digitados {} números e a soma entre eles é: {}'.format(contador, soma))
    
print('Você saiu do programa.')