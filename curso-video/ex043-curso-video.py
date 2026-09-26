peso = float(input('Informe o seu peso (apenas números): '))
altura = float(input('Informe a sua altura (ex: 1.70): '))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print('IMC: {:.1f}, você está abaixo do peso.'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('IMC: {:.1f}, você está no peso ideal.'.format(imc))
elif imc > 25 and imc <= 30:
    print('IMC: {:.1f}, você está no sobrepeso.'.format(imc))
elif imc > 30 and imc <= 40:
    print('IMC: {:.1f}, você está obeso.'.format(imc))
else:
    print('IMC {:.1f}, você está na obesidade mórbida.'.format(imc))