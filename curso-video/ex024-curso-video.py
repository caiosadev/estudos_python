cidade = input("Qual o nome da cidade? ").strip().upper()

busca = cidade.startswith('SANTO') #busca se existe SANTO no início da lista
print(busca)


#segunda forma de fazer
cidade = input("Qual o nome da cidade? ").strip()

print(cidade[:5].upper() == 'SANTO')