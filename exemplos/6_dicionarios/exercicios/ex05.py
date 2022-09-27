'''Crie três dicionários que represente pessoas diferentes e
armazene os em uma lista, percorra essa lista exibindo informações'''

user_1 = {
    'nome': 'Gabriel',
    'idade': 23,
}

user_2 = {
    'nome': 'Joao',
    'idade': 26,
}

user_3 = {
    'nome': 'Pedro',
    'idade': 35,
}

pessoas = [user_1, user_2, user_3]

for user in pessoas:
    print(f'Nome: {user["nome"]}, idade: {user["idade"]}')
