funcionarios = {
    'funcionario 1': {'nome': 'Amanda Santos', 'idade': 28, 'salario': 3500.00},
    'funcionario 2': {'nome': 'Carlos Silva', 'idade': 32, 'salario': 4200.00},
    'funcionario 3': {'nome': 'Daniela Oliveira', 'idade': 25, 'salario': 3800.00},
    'funcionario 4': {'nome': 'Eduardo Costa', 'idade': 30, 'salario': 4000.00}
}

print(f'{"Nome":^16} | {"Idade":^7} | {"Salário":^10}')
print('-' * 40)

print(f'{funcionarios["funcionario 1"]["nome"]:^16} |' 
      f'{funcionarios["funcionario 1"]["idade"]:^8} |' 
      f'{funcionarios["funcionario 1"]["salario"]:^10.2f}')

print(f'{funcionarios["funcionario 2"]["nome"]:^16} |'
      f'{funcionarios["funcionario 2"]["idade"]:^8} |'
      f'{funcionarios["funcionario 2"]["salario"]:^10.2f}')

print(f'{funcionarios["funcionario 3"]["nome"]:^16} |'
      f'{funcionarios["funcionario 3"]["idade"]:^8} |'
      f'{funcionarios["funcionario 3"]["salario"]:^10.2f}')

print(f'{funcionarios["funcionario 4"]["nome"]:^16} |'
      f'{funcionarios["funcionario 4"]["idade"]:^8} |'
      f'{funcionarios["funcionario 4"]["salario"]:^10.2f}')

print('-' * 40)