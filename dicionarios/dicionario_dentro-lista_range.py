aliens = []

for numero_aliens in range(10):
    novo_alien = {'cor' : 'verde', 'pontos' : 5, 'speed' : 'slow'}
    aliens.append(novo_alien)

print(f'Aliens criados: {len(aliens) - 1}.')
    
for alien in aliens[3:6]:
    if alien['cor'] == 'verde':
        alien['cor'] = 'amarelo'
        alien['pontos'] = 10
        alien['speed'] = 'medium'
        
for alien in aliens[6:]:
    if alien['cor'] == 'verde':
        alien['cor'] = 'vermelho'
        alien['pontos'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:9]:
    print(alien)
