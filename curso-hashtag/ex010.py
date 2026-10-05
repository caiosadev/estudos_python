email = 'funcionario1@empresa.com.br'

usuario, dominio = email.split('@')

mascara = usuario[:2] + ('*' * (len(usuario) - 4)) + usuario[-2:] +'@' + dominio

print(mascara)