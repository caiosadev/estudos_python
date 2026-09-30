prompt = '\nSeja muito bem-vindo(a) ao nosso sistema!'
prompt += '\nDigite seu nome ou "sair": '

mensagem = ''

while mensagem != 'sair':
    mensagem = input(prompt).strip().lower()
    
    if mensagem != 'sair':
        print(mensagem)
        

#usando flags
ativo = True

while ativo:
    mensagem = input(prompt).strip().lower()
    
    if mensagem == 'sair':
        ativo = False
    else:
        print(mensagem)