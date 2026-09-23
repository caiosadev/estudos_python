cores = ["vermelho", "verde", "azul"]

cor = input("Busque uma cor: ")

#lower() é uma função que transforma a string em minúscula, assim não importa se
#o usuário digitar a cor em maiúscula ou minúscula.
if cor.lower() in cores: 
    print("A cor existe na lista.")
else:
    print("A cor não existe na lista.")