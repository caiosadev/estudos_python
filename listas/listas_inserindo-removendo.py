motos = ["honda", "yamaha", "suzuki"]
print("1: ", motos)


#insere uma marca ao final da lista
motos.append("ducati")
print("2: ", motos)


#insere uma moto no índice 1
motos.insert(1, "kawazaki")
print("3: ", motos)


#removendo a moto do índice 1
del motos[1]
print("4: ", motos)


#removendo pelo item ao invés do índice
motos.remove("honda")
print("5: ", motos)


#inserindo honda novamente, mas removendo mantendo em uma variável o valor
motos.insert(0, "honda")
print("6: ", motos)


remocao_temporaria = "honda"
motos.remove(remocao_temporaria)
print("7: ", motos)
print(f"A {remocao_temporaria} foi removida temporariamente.")

motos.insert(0, remocao_temporaria) #inserindo honda novamente na lista
print(motos)


#mostra a última marca da lista, mas remove ela da lista
ultima_compra = motos.pop()
print(f"8: A última moto comprada foi uma {ultima_compra.title()}.")

#mostra a lista sem o último item pois foi removido pelo pop()
print(motos)


#insere o último item na lista novamente
motos.append(ultima_compra)
print("9: ", motos)


#organizando em ordem alfabética permanentemente
motos.sort()
print("10: ", motos)
#print(sorted(motos)) - exibe temporariamente a lista em ordem alfabética, sem mudar permanentemente