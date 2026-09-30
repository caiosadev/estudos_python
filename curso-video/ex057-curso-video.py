sexo = ''

while sexo not in ('M', 'F'):
    sexo = input('Qual o seu sexo? [F/M] ').strip().upper()[0]
    #[0] pega só a primeira letra caso o usuário escreva feminino ou masculino, completos.
    
    if sexo not in ('M', 'F'):
        print('Opção inválida, tente novamente!')

print(f'Sexo {sexo} salvo com sucesso!')
