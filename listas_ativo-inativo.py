ativos = ["João", "Maria", "Pedro", "Ana"]
inativos = ["Lucas", "Carla", "Paulo", "Fernanda"]

buscar = input("Digite o nome que deseja buscar: ").lower()

#transforma todos os nomes da lista de ativos em minúsculos para facilitar a busca,
#independente de como o usuário digitar o nome.
ativos_minusculos = [nome.lower() for nome in ativos] 

#transforma todos os nomes da lista de inativos em minúsculos para facilitar a busca, 
#independente de como o usuário digitar o nome.
inativos_minusculos = [nome.lower() for nome in inativos] 

if buscar in ativos_minusculos:
    print(f"{buscar} está na lista de ativos.")
elif buscar in inativos_minusculos:
    print(f"{buscar} está na lista de inativos.")
else:
    print(f"{buscar} não está em nenhuma das listas.")