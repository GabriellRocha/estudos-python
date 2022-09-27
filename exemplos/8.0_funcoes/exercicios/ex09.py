'''Perfil do usuário: Comece com uma cópia de user_profile.py, da página
210. Crie um perfil seu chamando build_profile(), usando seu primeiro nome
e o sobrenome, além de três outros pares chave-valor que o descrevam.'''


def user_profile(primeiro_nome, sobrenome, **user_info):
    '''Constrói um dicionário com informações sobre um usuário'''
    profile = {}
    profile["nome"] = primeiro_nome
    profile["sobrenome"] = sobrenome
    for key, value in user_info.items():
        profile[key] = value
    return profile


usuario = user_profile('Gabriel', 'Rocha', idade=23, altura=1.75, peso=75.00)
print('Dados do usuário:')
for key, value in usuario.items():
    print(f"{key.ljust(20, '-').title()}{str(value)}")
