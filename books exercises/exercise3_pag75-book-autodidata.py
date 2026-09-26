"""
primeiro criei a função f que recebe os valores e calcula o total, depois subtrai o desconto.
apenas os dois primeiros parâmetros são obrigatórios, os demais são opcionais e recebem o valor 0.
try protege contra erro de entrada que não forem um número inteiro ou float, except é executado nesse caso.
print chama a função f com os valores digitados e imprime o resultado.
or 0 substitui escrever a conversão dos números como exemplo seria depois das variáveis dentro de try:
    b = float(b) if b else 0
    b1 = int(b1) if b1 else 0
    c = float(c) if c else 0
    c1 = int(c1) if c1 else 0
    d = int(d) if d else 0
"""

def valor_total(valor1, peca1, valor2 = 0, peca2 = 0, valor3 = 0, peca3 = 0, desconto = 0):
    total = (valor1 * peca1) + (valor2 * peca2) + (valor3 * peca3)
    total = total - (total * desconto / 100)
    return total

try:   
    valor1 = float(input("escreva o primeiro valor: "))
    peca1 = int(input("escreva o número de peças: "))
    valor2 = float(input("escreva o segundo valor: ") or 0)
    peca2 = int(input("escreva o número de peças: ") or 0)
    valor3 = float(input("escreva o terceiro valor: ") or 0)
    peca3 = int(input("escreva o número de peças: ") or 0)
    desconto = int(input("escreva o desconto em porcentagem: ") or 0)

    print(valor_total(valor1, peca1, valor2, peca2, valor3, peca3, desconto))
    
except ValueError:
    print("Entrada inválida.")