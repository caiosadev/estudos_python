# Mosta os números ímpares

num_min = int(input("Mínimo: "))
num_max = int(input("Máximo: "))

while num_min <= num_max:
    if num_min % 2 != 0:
        print(num_min)

    num_min += 1
else: #mostra a mensagem no final, ainda não encontrei a solução para ocultar
    print("Instruções erradas, tente novamente.")
