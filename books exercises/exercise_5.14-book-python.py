soma = 0
qnt_numeros = 0

while True:
    numero_digitado = int(input("Digite um número a somar (ou 0 para sair): "))
    if numero_digitado == 0:
        break
    soma += numero_digitado
    qnt_numeros += 1
    
if qnt_numeros > 0:
    media = soma / qnt_numeros

    print("Quantidade de números digitados: {}" .format(qnt_numeros))
    print("Soma: {}" .format(soma))
    print("Média aritmética: {:.2f}" .format(media))

else:
    print("Nenhum número foi digitado.")