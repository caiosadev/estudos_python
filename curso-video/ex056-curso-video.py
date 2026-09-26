soma_idade = 0
media = 0
maior_idade_h = 0
h_velho = ''
mulheres_20 = 0

for pessoas in range(1, 5):
    nome = input('Insira o {}ª nome: '.format(pessoas))
    idade = int(input('Insira a idade: '))
    sexo = int(input('[ 1 ] para feminino e [ 2 ] para masculino: '))
    
    soma_idade += idade #para fazer a média posteriormente
    
    if sexo == 2 and idade > maior_idade_h:
        maior_idade_h = idade
        h_velho = nome
    if sexo == 1 and idade < 20:
        mulheres_20 += 1
        
media = soma_idade / 4

print('A média de idade é de {:.1f}.'.format(media))
print('O homem mais velho tem {} anos e é o: {}.'.format(maior_idade_h, h_velho))
print('{} mulher(es) tem menos de 20 anos.'.format(mulheres_20))
