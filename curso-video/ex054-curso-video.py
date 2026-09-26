from datetime import date

ano = date.today().year
maiores = 0
menores = 0

for pessoa in range(1, 8):
    nascimento = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(pessoa)))
    idade = ano - nascimento
    
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
        
print('{} pessoas são maiores de idade.'.format(maiores))
print('{} pessoas são menores de idade.'.format(menores))