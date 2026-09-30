cores = ["vermelho", "verde", "azul"]

cor = input("Busque uma cor: ")

#lower() é uma função que transforma a string em minúscula, assim não importa se
#o usuário digitar a cor em maiúscula ou minúscula.
if cor.lower() in cores: 
    print("A cor existe na lista.")
else:
    print("A cor não existe na lista.")
    
    
#usando while
numeros = [15, 7, 27, 39]

numero = int(input('Digite o número que procura: '))

achou = False
contador = 0

while contador < len(numeros):
    if numeros[contador] == numero:
        achou = True
        break
    
    contador += 1
    
if achou:
    print(f'{numero} achado na posição {contador}.')
    
else:
    print(f'Número {numero} não encontrado.')