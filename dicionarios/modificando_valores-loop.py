alien0 = {
    'cor': 'verde', 
    'pontos': 5,
    'posicao_x': 0,
    'posicao_y': 25,
    'velocidade': 'media',
}

print(f"A posição original do alienígena é: {alien0['posicao_x']}")

if alien0['velocidade'] == 'lenta':
    incremento_x = 1
elif alien0['velocidade'] == 'media':
    incremento_x = 2
else:
    incremento_x = 3

alien0['posicao_x'] += incremento_x

print(f"A nova posição do alienígena é: {alien0['posicao_x']}")
