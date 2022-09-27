'''Misturando argumentos posicionais e arbitrários.
Se quiser que uma função aceite vários tipos de argumentos, o
parâmetro que aceita um número arbitrário de argumentos deve ser
colocado por último na definição da função.Python faz a
correspondência de argumentos posicionais e nomeados antes, e depois
agrupa qualquer argumento remanescente no último parâmetro.'''


def make_pizza(tamanho, *toppings):
    '''Apresenta a pizza que estamos prestes a preparar.'''
    print(f'Fazendo uma pizza de tamanho {tamanho}')
    print('Com os seguintes ingredientes: ')
    for item in toppings:
        print('- ' + item)


'''Uso de argumento posicional com argumentos arbitrários.'''
make_pizza('M', 'Mussarela', 'Calabresa', 'Azeitona', 'Cebola')


'''Usando argumentos nomeados arbitrários
Às vezes você vai querer aceitar um número arbitrário de argumentos,
mas não saberá com antecedência qual tipo de informação será passado
para a função. Nesse caso, podemos escrever funções que aceitem tantos
pares de chave-valor(argumentos nomeados) quantos forem fornecidos pela
instrução que fez a chamada'''


def build_profile(first, last, **user_info):
    '''Constrói um dicionário contendo tudo que sabemos de um usuário.'''
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


'''espera um primeiro nome e um sobrenome e permite que o usuário passe
tantos pares nome-valor quantos ele quiser. Os asteriscos duplos antes do
parâmetro **user_info fazem Python criar um dicionário vazio chamado
user_info e colocar quaisquer pares nome-valor recebidos nesse
dicionário. Nessa função, podemos acessar os pares nome-valor em
user_info como faríamos com qualquer dicionário.
'''
usuario = build_profile('Gabriel', 'Rocha', idade=23, local='campinas')
print(usuario)
