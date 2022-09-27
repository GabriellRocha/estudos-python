'''Camiseta: Escreva uma função chamada make_shirt() que aceite um
tamanho e o texto de uma mensagem que deverá ser estampada na camiseta.
A função deve exibir uma frase que mostre o tamanho da camiseta e a
mensagem estampada.
Chame a função uma vez usando argumentos posicionais para criar uma
camiseta. Chame a função uma segunda vez usando argumentos nomeados.'''


def make_shirt(tamanho: str, txt: str) -> str:
    '''Exibe personalização de camiseta'''
    return f'Camiseta de tamanho {tamanho} com a frase {txt}.'


print(make_shirt('M', 'Deus é fiel'))  # Argumentos posicionais
print(make_shirt(tamanho='M', txt='Deus é fiel.'))  # Argumentos nomeados
