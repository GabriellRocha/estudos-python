usuarios = ['Gabriel', 'Pedro', 'Luiz', 'Ana', 'Admin']
if usuarios:  # Verifica se a lista não está vazia.
    for user in usuarios:
        if user == 'Admin':
            print('Olá Admin, gostaria de ver um relatório de status? ')
        else:
            print(f'Seja bem-vindo(a) de volta {user}.')
else:
    print('Precisamos encontrar alguns usuários!')
