'''Em vez de colocar um dicionário em uma lista, às vezes é conveniente
colocar uma lista em um dicionário.'''

'''No exemplo a seguir, dois tipos de informação são armazenados para
cada pizza: o tipo de massa e a lista de ingredientes.'''

pizza = {'massa': "grossa", 'ingredientes': ['calabresa', 'pimenta', 'cheese']}

'''Para usar os itens da lista, fornecemos o nome do dicionário
e a chave ingredientes'''

print(f'Você pediu uma pizza {pizza["massa"]}, com os seguintes ingredientes:')
for item in pizza['ingredientes']:
    print(item)

'''e Você pode aninhar uma lista em um dicionário
sempre que quiser que mais de um valor seja associado a uma única
chave em um dicionário.'''

linguagens_favoritas = {
    'jen': ['ruby', 'go'],
    'sarah': ['python', 'java'],
    'edward': ['java', 'python']
}

for pessoa, tec in linguagens_favoritas.items():
    print(f'{pessoa} sua primeira linguagem {tec[0]} e a secundaria {tec[1]}')
