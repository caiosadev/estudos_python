rios = {
    'nilo' : 'egito',
    'jordao' : 'brasil',
    'danubio' : 'alemanha',
    'mississipi' : 'eua',
    'volga' : 'russia',
}

for rio, pais in rios.items():
    print(f'O {rio.capitalize()} atravessa o {pais.capitalize()}.')
        
print('')
        
for rio in rios.keys():
    print(rio.title())
    
print('')
    
for pais in rios.values():
    print(pais.title())