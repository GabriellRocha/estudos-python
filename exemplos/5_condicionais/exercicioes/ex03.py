usuarios = ['Gabriel', 'Luiz', 'Pedro', 'João', 'Lucas']
novos_usuarios = ['Matheus', 'Jose', 'Gabriel', 'Felipe']
for user in novos_usuarios:
    if user.title() in usuarios:
        print('Usuário já utilizado. Forneça um novo nome.')
    else:
        print('Usuário disponível!')
