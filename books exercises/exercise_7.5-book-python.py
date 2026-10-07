entrada1 = 'AATTGGAA'
entrada2 = 'TG'

caracteres = ''

for caractere in entrada1:
    if caractere not in entrada2:
        caracteres += caractere
        
print(caracteres)
