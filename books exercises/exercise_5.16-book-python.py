valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
        
        print("{} cédula(s) ou moeda(s) de R$ {:.2f}" .format(cedulas, atual))
    else:
        if apagar == 0:
            print("Você saiu do programa.")
            break
    
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
        elif atual == 1:
            atual = 0.5
        elif atual == 0.5:
            atual = 0.25
        elif atual == 0.25:
            atual = 0.1
        elif atual == 0.1:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        else:
            print("Digite um valor válido.")
            break
        
        cedulas = 0