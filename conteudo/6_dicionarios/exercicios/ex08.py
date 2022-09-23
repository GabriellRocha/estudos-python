'''Crie um dicionário chamado cities. Use os nomes de três
cidades como chaves em seu dicionário. Crie um dicionário com informações
sobre cada cidade e inclua o país em que a cidade está localizada, a
população aproximada. As chaves do dicionário
de cada cidade devem ser algo como country, population. Apresente o
nome de cada cidade e todas as informações que você armazenou sobre ela.'''

cities = {
    'São paulo': {'pais': "Brasil", 'populacao': 12000000},
    'Nova Iorque': {'pais': "Estados Unidos", 'populacao': 8380000},
    'Toquio': {'pais': "Japão", 'populacao': 14000000}
}


for chave, valor, in cities.items():
    print(
        f'Cidade: {chave}. País: {valor["pais"]}. População: {valor["populacao"]}')
