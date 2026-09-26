from datetime import date

nascimento = int(input('Informe o seu ano de nascimento: '))
sexo = int(input('[ 1 ] para Feminino \n[ 2 ] para Masculino: '))

ano = date.today().year
idade = ano - nascimento

if sexo == 2:
    if idade < 18:
        meses = (18 - idade) * 12
        anos = meses / 12
        print('Você ainda vai se alistar, faltam {} meses [{:.0f} ano(s)].'
              .format(meses, anos))
    elif idade == 18:
        print('Já está na hora de se alistar!')
    else:
        meses = (idade - 18) * 12
        anos = meses / 12
        print('Você perdeu o tempo para se alistar. Passaram {} meses ({:.0f} anos).'
              .format(meses, anos))
else:
    print('Você não precisa se alistar!')
