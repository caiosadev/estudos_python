casa = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual o seu salário atual? R$ '))
anos = float(input('Em quantos anos você pagará o imóvel (apenas números)? '))

limite_prestacao = salario - (salario * 30) / 100
parcela = casa / (anos * 12) #anos * 12 transforma em meses

if limite_prestacao >= parcela:
    print('Você pode financiar este imóvel, pagando em {:.0f} anos. '
          'As parcelas mensais serão de R$ {:.2f}'.format(anos, parcela))
else:
    print('Você não pode financiar esse imóvel, pois as prestações (R$ {:.2f}) estão '
          'ultrapassando 30% do seu salário.'.format(parcela))