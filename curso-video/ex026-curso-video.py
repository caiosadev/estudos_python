import unicodedata # biblioteca de acentuação

frase = input("Digite uma frase: ").strip().upper()

frase = ''.join( #usado para remover acentuação das letras
    letra for letra in unicodedata.normalize('NFD', frase)
    if unicodedata.category(letra) != 'Mn'
)

letra = frase.count('A')
print("A letra A aparece: {} vezes." .format(letra))

posicao_inicial = frase.find('A') + 1
print("Posição em que a letra A aparece a primeira vez: {}." .format(posicao_inicial))

posicao_final = frase.rfind('A')
print("Posição em que a letra A aparece uma última vez: {}." .format(posicao_final))