nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('O aluno ficou com média de {:.1f}, então foi aprovado!'.format(media))
elif media >= 5 and media <= 6.9:
    print('O aluno ficou com média de {:.1f}, então está em recuperação.'.format(media))
else:
    print('O aluno ficou com média de {:.1f}, então foi reprovado!'.format(media))