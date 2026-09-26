sujeito = ['Eu ', 'Tu ', 'Ele/Ela ', 'Nós ', 'Vós ', 'Eles/Elas ']
ar = ['o', 'as', 'a', 'amos', 'ais', 'am']
er = ['o', 'es', 'e', 'emos', 'eis', 'em']
ir = ['o', 'es', 'e', 'imos', 'is', 'em']

verbo = input("Escreva o verbo: ")

final_verbo = verbo[-2:]
sobra_verbo = verbo[:-2]

if final_verbo == 'ar':
    for n in range(6): #loop for com função range
        print(sujeito[n] + sobra_verbo + ar[n])
elif final_verbo == 'er':
    for n in range(6):
        print(sujeito[n] + sobra_verbo + er[n])
elif final_verbo == 'ir':
    for n in range(6):
        print(sujeito[n] + sobra_verbo + ir[n])
else:
    print("Algo deu errado, tente novamente.")

