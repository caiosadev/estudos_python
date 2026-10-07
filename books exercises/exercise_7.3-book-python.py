entrada1 = 'CTA'
entrada2 = 'ABC'

caracteres_unicos = []

for caractere in entrada1:
    if caractere not in entrada2 and caractere not in caracteres_unicos:
        caracteres_unicos.append(caractere)
        
for caractere in entrada2:
    if caractere not in entrada1 and caractere not in caracteres_unicos:
        caracteres_unicos.append(caractere)

print(''.join(caracteres_unicos))
