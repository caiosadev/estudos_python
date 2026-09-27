numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numero in numeros:
    if numero == 1:
        print('{}st'.format(numero))
    elif numero == 2:
        print('{}nd'.format(numero))
    elif numero == 3:
        print('{}rd'.format(numero))
    else:
        print('{}th'.format(numero))