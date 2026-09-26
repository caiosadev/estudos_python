L = []

while True:
    try: #protege contra erros
        n = int(input("Digite um número (0 para sair): "))
        if n == 0:
            break
        L.append(n) #adiciona o número à lista que estava vazia
    except ValueError: #faz parte do try, para que o usuário digite um número inteiro
        print("Digite um número inteiro válido.")
    
    x = 0
#len é uma função que retorna o tamanho da lista, mesmo mudando o tamanho da lista.
    while x < len(L): 
        print(L[x]) #imprime a lista de números que o usuário digitou
        x += 1