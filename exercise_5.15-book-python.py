produto1 = 1
preco1 = 0.50
produto2 = 2
preco2 = 1.00
produto3 = 3
preco3 = 4.00
produto4 = 4
preco4 = 7.00
produto5 = 5
preco5 = 8.00

#função que calcula o total de cada produto vendido.
def calcular_total(produto, quantidade_vendida): 
    if produto == 1:
        total = preco1 * quantidade_vendida

    elif produto == 2:
        total = preco2 * quantidade_vendida

    elif produto == 3:
        total = preco3 * quantidade_vendida

    elif produto == 4:
        total = preco4 * quantidade_vendida

    elif produto == 5:
        total = preco5 * quantidade_vendida

    else:
        return None

    return total

total_compras = 0


while True:
    produto = int(input("Digite o código do produto (0 para sair): "))

    if produto == 0:
        break

#precisa mudar se mudar o número de produtos. Mas pode ser feito com dicionário (lista).
    elif produto < 1 or produto > 5: 
        print("Código de produto inválido.")

    else:
        quantidade_vendida = int(input("Digite a quantidade vendida: "))

        total = calcular_total(produto, quantidade_vendida) #chamando a função.

        total_compras += total


print("Total das compras: R$ {:.2f}" .format(total_compras))