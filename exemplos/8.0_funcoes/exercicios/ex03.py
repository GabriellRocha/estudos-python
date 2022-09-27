'''Camisetas grandes: Modifique a função make_shirt() de modo que as
camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
uma camiseta grande e outra média com a mensagem default, e uma camiseta
de qualquer tamanho com uma mensagem diferente.
'''


def make_shirt(txt='Eu amo Python', tamanho='G') -> str:
    '''Exibe personlização de camiseta'''

    return f'Camiseta de tamanho {tamanho} com a frase {txt}'


camiseta_media = make_shirt(tamanho='M')
camiseta_grande = make_shirt()
camiseta_pequena = make_shirt(txt='Deus é fiel', tamanho='P')

print(camiseta_pequena)
print(camiseta_media)
print(camiseta_grande)
