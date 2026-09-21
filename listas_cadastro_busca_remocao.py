# ==========================================
# LISTAS DE USUÁRIOS
# ==========================================

ativos = []
inativos = []


# ==========================================
# CADASTRO
# ==========================================

# Função para receber e validar o nome
def cadastro_nome():
    while True:
        nome = input("Digite o nome que deseja adicionar (0 para sair): ").strip().title()

        if nome == "0":
            return nome

        if not nome.replace(" ", "").isalpha():
            print("Nome inválido. Digite apenas letras.")
            continue

        return nome


# Função responsável pelo cadastro do usuário
def cadastrar_usuario():
    nome = cadastro_nome()

    while nome != "0":
        tipo = input("Digite 'a' para ativo ou 'i' para inativo: ").strip().lower()

        if tipo == "a":
            if nome.lower() in [n.lower() for n in ativos]:
                print("Esse nome já está na lista de ativos.")
            else:
                ativos.append(nome)
                print(nome, "foi adicionado aos ativos.")
        elif tipo == "i":
            if nome.lower() in [n.lower() for n in inativos]:
                print("Esse nome já está na lista de inativos.")
            else:
                inativos.append(nome)
                print(nome, "foi adicionado aos inativos.")
        else:
            print("Tipo inválido. Digite 'a' ou 'i'.")

        nome = cadastro_nome()


# ==========================================
# LISTAGEM
# ==========================================

# Função para listar todos os usuários cadastrados
def listar_nomes():
    verificar = input("Deseja ver as listas de ativos e inativos? (s/n): ").strip().lower()

    if verificar == "s":
        print("\nLista de ativos:", ativos)
        print("Lista de inativos:", inativos)

    return verificar


# ==========================================
# BUSCA
# ==========================================

# Função para receber e validar o nome da busca
def buscar_nome():
    while True:
        buscar = input("Digite o nome que deseja buscar (0 para sair): ").strip().lower()

        if buscar == "0":
            return buscar

        if not buscar.replace(" ", "").isalpha():
            print("Nome inválido. Digite apenas letras.")
            continue
        return buscar


# Função responsável por procurar o usuário
def buscar_usuario():
    buscar = buscar_nome()

    # Cria versões das listas com todos os nomes em minúsculas
    ativos_minusculos = [nome.lower() for nome in ativos]
    inativos_minusculos = [nome.lower() for nome in inativos]

    while buscar != "0":
        if buscar in ativos_minusculos and buscar in inativos_minusculos:
            print(f"{buscar.title()} está na lista de ativos e na lista de inativos.")
        elif buscar in ativos_minusculos:
            print(f"{buscar.title()} está na lista de ativos.")
        elif buscar in inativos_minusculos:
            print(f"{buscar.title()} está na lista de inativos.")
        else:
            print(f"{buscar.title()} não está em nenhuma das listas.")

        buscar = buscar_nome()


# ==========================================
# REMOÇÃO
# ==========================================

# Função para remover um usuário
def remover_usuario():
    while True:
        nome = input("Digite o nome que deseja remover (0 para sair): ").strip().lower()

        if nome == "0":
            return

        if not nome.replace(" ", "").isalpha():
            print("Nome inválido. Digite apenas letras.")
            continue

        tipo = input("O usuário está ativo (a) ou inativo (i)? ").strip().lower()

        if tipo == "a":
            lista = ativos
        elif tipo == "i":
            lista = inativos
        else:
            print("Tipo inválido. Digite 'a' ou 'i'.")
            continue

        for usuario in lista:
            if usuario.lower() == nome:
                lista.remove(usuario)
                print(usuario, "foi removido da lista.")
                return remover_usuario()

        print("Usuário não encontrado na lista.")
        continue


# ==========================================
# NÚMERO DE USUÁRIOS
# ==========================================

# Função para listar a quantidade dos usuários cadastrados
def qnt_nomes():
    verificar_qnt = input("Deseja ver a quantidade usuários? (s/n): ").strip().lower()

    if verificar_qnt == "s":
        print("O número de usuários ativos é de: {}.\nE de usuários inativos é de: {}.".format(len(ativos), len(inativos)))

    return 0


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

# CADASTRO
cadastrar_usuario()


# LISTAGEM ANTES DA BUSCA
listar_nomes()


# BUSCA
buscar_usuario()


# REMOÇÃO
remover = input("Deseja remover um usuário? (s/n): ").strip().lower()

if remover == "s":
    remover_usuario()

# NÚMERO DE USUÁRIOS
qnt_nomes()

# LISTAGEM FINAL
listar_nomes()
