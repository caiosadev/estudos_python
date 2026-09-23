produtos = {
    1: 0.50,
    2: 1.00,
    3: 4.00,
    4: 7.00,
    5: 8.00
}

def calcular_total(produto, quantidade_vendida):
    total = produtos[produto] * quantidade_vendida #usando lista no cálculo da função.
    return total

total_compras = 0


while True:
    produto = int(input("Digite o código do produto (0 para sair): "))

    if produto == 0:
        break

#não muda conforme o número de produtos, pois está usando a lista (dicionário).
    elif produto not in produtos: 
        print("Código de produto inválido.")

    else:
        quantidade_vendida = int(input("Digite a quantidade vendida: "))

        total = calcular_total(produto, quantidade_vendida) #chamando a função.

        total_compras += total #somando o total da compra ao total geral.


print("Total das compras: R$ {:.2f}" .format(total_compras))