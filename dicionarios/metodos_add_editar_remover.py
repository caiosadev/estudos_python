produtos = {
    'ipad' : 7000,
    'iphone' : 10000,
    'airpods' : 2000,
    'apple watch' : 5000,
}


#adicionar um produto
produtos['macbook'] = 15000
print(produtos)
#ou
novos_produtos = [('ipad pro', 12000), ('mac mini', 10000)]
produtos.update(dict(novos_produtos)) #adiciona uma lista de tuplas ao dicionário
#ao buscar com .items() a listagem dada será de tuplas.


#editar um produto
produtos['ipad'] = 7500
print(produtos)


#remover um produto
remover = produtos.pop('apple watch')
print(produtos)
print(f'Apple Watch: R$ {remover}, removido.')


#verificar se um produto existe
if 'iphone' in produtos: #busca sempre nas chaves do dicionário
    print('O produto iphone cadastrado.')
else:
    print('O produto iphone não cadastrado.')
    
    
if 'ipad' in produtos.keys(): #busca apenas nas chaves do dicionário
    print('O produto ipad cadastrado.')
else:
    print('O produto ipad não cadastrado.')
  
    
if 2000 in produtos.values(): #busca apenas nos valores do dicionário
    print('O produto de valor R$ 2000 cadastrado.')
else:
    print('O produto de valor R$ 2000 não cadastrado.')
    
    
#Quantidade de produtos cadastrados
qnt_produtos = len(produtos)
print(f'Quantidade de produtos cadastrados: {qnt_produtos}')


#Ver produtos cadastrados
produtos_cadastrados = list(produtos)
print(f'Produtos cadastrados: {produtos_cadastrados}')
#ou
cadastrados = produtos.items() #Retorna uma lista de tuplas com os produtos e seus respectivos preços
print(f'Produtos cadastrados: {cadastrados}') 


#Buscar produtos cadastrados
produto_buscado = input('Digite o nome do produto que deseja buscar: ').strip().lower()
if produto_buscado in produtos:
    preco_produto = produtos[produto_buscado]
    print(f'O produto {produto_buscado.title()} está disponível e custa R$ {preco_produto}.')
else:
    print(f'O produto {produto_buscado.title()} não está cadastrado/disponível.')
