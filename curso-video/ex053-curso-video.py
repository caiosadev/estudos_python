#usando for
frase = input('Digite uma frase: ').strip().lower()

frase_lista = frase.split()
frase_junto = ''.join(frase_lista)
frase_invertida = ''

#O range(len(frase) - 1, -1, -1) começa no último índice, vai até o índice 0 e diminui de um em um.
for letra in range(len(frase_junto) -1, -1, -1):
    frase_invertida += frase_junto[letra]
    
if frase_junto == frase_invertida:
    print('A frase: "{}", é um palíndromo.'.format(frase))
else:
    print('A frase: "{}", não é um palíndromo.'.format(frase))