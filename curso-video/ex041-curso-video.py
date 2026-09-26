from datetime import date

nascimento = int(input('Informe o ano de nascimento: '))

ano = date.today().year
idade = ano - nascimento

if idade <= 9:
    print('O atleta tem {} anos, então está na categoria Mirim.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos, então está na categoria Infantil.'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos, então está na categoria Junior.'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos, então está na categoria Sênior.'.format(idade))
else:
    print('O atleta tem {} anos, então está na categoria Master.'.format(idade))