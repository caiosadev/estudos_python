"""
try protege contra erro de entrada de dados que não forem um número inteiro.
na transformação de a para int poderia ser a = int(a).
def chama a função f que retorna o quadrado do número digitado.
except é executado pulando a chamada da função f, caso a entrada seja inválida.
""" 

try:
    numero = int(input("escreva um número:"))
        
    def num_quadrado(numero):
        return numero * numero

    print(num_quadrado(numero))
    
except ValueError:
    print("Entrada inválida.")