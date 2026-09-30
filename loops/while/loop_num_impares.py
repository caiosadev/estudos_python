# Mosta os números ímpares

num_min = int(input("Mínimo: "))
num_max = int(input("Máximo: "))

if num_min > num_max:
    print("Instruções erradas, tente novamente.")
else:
    while num_min <= num_max:
        if num_min % 2 != 0:
            print(num_min)
            
        num_min += 1
 
