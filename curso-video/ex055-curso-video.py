menor = 0
maior = 0

for pessoa in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa (ex: 65.5)? '.format(pessoa)))
    
    if pessoa == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        else:
            maior = peso
        
    
print('O menor peso é {}kg e o maior peso é {}kg.'.format(menor, maior))