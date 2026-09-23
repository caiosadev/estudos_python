#lista de usuários que serão cadastrados
ativos = []
inativos = []

def cadastro_nome(): #função criada para não ter que repetir no loop ao final
    #strip() remove espaços em branco no início e no final
    nome = input("Digite o nome que deseja adicionar (0 para sair): ").strip().capitalize() 
    return nome
# chamando a função para funcionar, ou seja, é como se escrevesse o input para o usuário 
#cadastrar o nome do usuário
nome = cadastro_nome() 

while nome != "0": #diferente de 0 executa o loop
    if nome == "":
        print("Nome inválido. Por favor, digite um nome válido.")
    else:
        tipo = input("Digite 'a' para ativo ou 'i' para inativo: ").lower()
        if tipo == "a":
            if nome.lower() in [n.lower() for n in ativos]: #verifica se o nome já está na lista
                print("Esse nome já está na lista de ativos.")
            else:
                ativos.append(nome) #se o nome não estiver, ele insere na lista
                print(nome, "foi adicionado aos ativos.")
        elif tipo == "i":
            if nome.lower() in [n.lower() for n in inativos]: #verifica se o nome já está na lista
                print("Esse nome já está na lista de inativos.")
            else:
                inativos.append(nome) #adiciona o nome na lista caso ele não exista
                print(nome, "foi adicionado aos inativos.")
        else: #se o usuário não digitar a ou i, mostra a mensagem abaixo
            print("Tipo inválido. Digite 'a' ou 'i'.")
            
#chamando a função para não ter que repetir o input completo, aqui repete o 
#cadastro do próximo nome no loop
    nome = cadastro_nome() 

#lower() transforma em minúsculo o que o usuário digitar, substitui if 
#verificar == "s" or verificar == "S"
verificar = input("Deseja ver as listas de ativos e inativos? (s/n): ").lower() 

if verificar == "s":
    print("Lista de ativos:", ativos)
    print("Lista de inativos:", inativos)
#sem necessidade de else para N, pois já finaliza essa etapa do programa automaticamente

buscar = input("Digite o nome que deseja buscar: ").strip().lower()

ativos_minusculos = [nome.lower() for nome in ativos] #transforma tudo em minúsculo
inativos_minusculos = [nome.lower() for nome in inativos]

#verifica em qual lista o nome foi cadastrado
if buscar in ativos_minusculos and buscar in inativos_minusculos: 
    #capitalize() padroniza os nomes digitados
    print(f"{buscar.capitalize()} está na lista de ativos e na lista de inativos.") 
elif buscar in ativos_minusculos:
    print(f"{buscar.capitalize()} está na lista de ativos.")
elif buscar in inativos_minusculos:
    print(f"{buscar.capitalize()} está na lista de inativos.")
else:
    print(f"{buscar.capitalize()} não está em nenhuma das listas.")