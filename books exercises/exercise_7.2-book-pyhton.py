entrada1 = 'AAACTBF'
entrada2 = 'CBT'

caracteres_comuns = []

for caractere in entrada1:
	if caractere in entrada2 and caractere not in caracteres_comuns:
		caracteres_comuns.append(caractere)

print(''.join(caracteres_comuns))
