def fun_dividir(resultado1):
    resultado1 = a / 2
    return resultado1
    
def fun_multiplicar(resultado2):
    resultado2 = resultado1 * 4
    return resultado2

try:
    a = int(input("Digite o primeiro número: "))
    resultado1 = fun_dividir(a)
    resultado2 = fun_multiplicar(resultado1)
    print(f"Resultado 1: {resultado1}")
    print(f"Resultado 2: {resultado2}")

except ValueError:
    print("Entrada inválida.")