
'''Às vezes, você vai querer armazenar um conjunto de dicionários em uma
lista ou uma lista de itens como um valor em um dicionário. Isso é
conhecido como aninhar informações.Podemos aninhar um conjunto
de dicionários em uma lista, uma lista de itens em um dicionário ou até
mesmo um dicionário em outro dicionário.'''

'''Lista de alienígenas, em que cada alienígena tem um dicionário
representando informações sobre ele'''

alien_1 = {'cor': "verde", 'pontos': 5}
alien_2 = {'cor': "amarelo", 'pontos': 10}
alien_3 = {'cor': 'vermelho', 'pontos': 15}

aliens = [alien_1, alien_2, alien_3]


'''Criando uma frota de aliens'''

lista_aliens = []
for i in range(10):
    new_alien = {'cor': "verde", 'pontos': 30}
    lista_aliens.append(new_alien)

# Trocando a cor dos 3 primeiros aliens

for alien in lista_aliens[0:3]:
    if alien['cor'] == 'verde':
        alien['cor'] = 'amarelo'
