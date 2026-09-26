valor = float(input('Digite o valor do produto: R$ '))
metodo_pag = int(input('[ 1 ] para pagamento no dinheiro/pix,\n[ 2 ] para cartão de crédito,'
                       '\n[ 3 ] para 2x no cartão ou \n[ 4 ] para 3x ou mais no cartão: '))

dinheiro_pix = valor - (valor * 10) / 100
cartao = valor - (valor * 5) / 100
cartao_2x = valor
cartao_3x = valor + (valor * 20) / 100

if metodo_pag == 1:
    print('Para pagamento no dinheiro/pix, com 10% de desconto, o valor é de: R$ {:.2f}'
          .format(dinheiro_pix))
elif metodo_pag == 2:
    print('Para pagamento em 1x no cartão, com 5% de desconto, o valor é de: R$ {:.2f}'
          .format(cartao))
elif metodo_pag == 3:
    print('Para pagamento em 2x no cartão, o valor é de: R$ {:.2f}'.format(cartao_2x))
else:
    print('Para pagamento em 3x ou mais no cartão, com 20% de juros, o valor é de R$ {:.2f}'
          .format(cartao_3x))
