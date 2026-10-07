linguagens_favoritas = {
    'luiz' : ['python', 'java'],
    'amanda' : ['c', 'java'],
    'andre' : ['javascript'],
    'carla' : ['rust', 'go', 'r'],
    'eduardo' : ['python', 'c++'],
}

for nome, linguagens in linguagens_favoritas.items():
    print(f'\n{nome.title()} gosta de:')
    
    for linguagem in linguagens:
        print(linguagem.title())
