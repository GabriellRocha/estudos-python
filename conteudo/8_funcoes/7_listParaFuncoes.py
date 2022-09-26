'''Com frequencia você achará útil passar uma lista para
uma função, seja uma lista de nome, numeros ou de objetos
mais complexos como dicionários. Se passarmos uma lista
a uma função, ela terá acesso direto ao conteúdo
dessa lista'''


def greet_users(names: list) -> None:
    '''Recebe uma lista de nomes e exibe de forma elegante.'''
    for name in names:
        print('Olá, ' + name.title())


names = ['Gabriel', 'José', 'Pedro', 'Raimundo']

greet_users(names)
