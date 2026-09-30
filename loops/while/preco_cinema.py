idade = input('Qual a idade? (apenas números) ').strip().lower()
idade = int(idade.replace(' ', '').replace('anos', ''))

ingresso = 0

while True:
    if idade < 3:
        print('O ingresso é gratuito!')
        break
    
    elif idade >= 3 and idade <= 12:
        ingresso = 10
        print(f'O ingresso custa: R$ {ingresso}.')
        break
    
    else:
        ingresso = 15
        print(f'O ingresso custa: R$ {ingresso}.')
        break
