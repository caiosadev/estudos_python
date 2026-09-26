#Fiz diferente do exercício do livro, pois não gostei como é a saída.
#4.4 elif, página 83, livro python
categoria = int(input("Informe o número da categoria do produto: "))

preco01 = 10
preco02 = 18
preco03 = 23
preco04 = 26
preco05 = 31

if categoria == 1:
    print("O preço do produto é R$ {:.2f}" .format(preco01))
elif categoria == 2:
    print("O preço do produto é R$ {:.2f}" .format(preco02))
elif categoria == 3:
    print("O preço do produto é R$ {:.2f}" .format(preco03))
elif categoria == 4:
    print("O preço do produto é R$ {:.2f}" .format(preco04))
elif categoria == 5:
    print("O preço do produto é R$ {:.2f}" .format(preco05))
else:
    print("Categoria não cadastrada, tente novamente.")




#Formato simplificado, sem declaração das variáveis e valores, com menos print
#Porém ao digitar valores diferentes, como zero, mostra o último print também, como no exemplo do livro
categoria = int(input("Informe o número da categoria do produto: "))

preco = 0

if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print("Categoria não cadastrada, tente novamente.")
print("O preço do produto é R$ {:.2f}" .format(preco))
